"""
This module uses ctypes to implement an interface to the Cypress DLL/driver.
"""

from os import path
from ctypes import c_ubyte, c_char, c_uint16, c_uint32, c_int32
from ctypes import c_void_p
from ctypes import Structure, cdll, POINTER, byref, sizeof, memset, addressof
from enum import Enum, IntEnum

# __file__=rf"C:\Users\akshitaggarwal\AppData\Roaming\Texas Instruments\DLP EVM GUI 3.2.0.7"
# cdll.LoadLibrary(path.join(path.dirname(path.abspath(__file__)), 'cyusbserial.dll'))
cdll.LoadLibrary(rf"C:\Users\FRADENLAB\AppData\Roaming\Texas Instruments\DLP EVM GUI 3.2.0.7\cyusbserial.dll")


# noinspection PyPep8Naming
class CY_DEVICE_TYPE(IntEnum):
    CY_TYPE_DISABLED = 0    # Invalid device type or interface is not CY_CLASS_VENDOR
    CY_TYPE_UART = 1        # Interface of device is of type UART
    CY_TYPE_SPI = 2         # Interface of device is of type SPI
    CY_TYPE_I2C = 3         # Interface of device is of type I2C
    CY_TYPE_JTAG = 4        # Interface of device is of type JTAG
    CY_TYPE_MFG = 5         # Interface of device is in Manufacturing mode


# noinspection PyPep8Naming
class CY_DEVICE_CLASS(Enum):
    CY_CLASS_DISABLED = 0   # None or the interface is disabled
    CY_CLASS_CDC = 0x02     # CDC ACM class
    CY_CLASS_PHDC = 0x0F    # PHDC class
    CY_CLASS_VENDOR = 0xFF  # VENDOR specific class


# noinspection PyPep8Naming
class CY_DEVICE_SERIAL_BLOCK(IntEnum):
    SerialBlock_SCB0 = 0    # Serial Block Number 0
    SerialBlock_SCB1 = 1    # Serial Block Number 1
    SerialBlock_MFG = 2     # Serial Block Manufacturing Interface.


# noinspection PyPep8Naming
class CY_SPI_PROTOCOL(IntEnum):
    CY_SPI_MOTOROLA = 0
    CY_SPI_TI = 1
    CY_SPI_NS = 2


class CypressError(Exception):  # pylint: disable E221
    """ custom errors raised by the Cypress class will be of this type """

    _status = [("CY_SUCCESS", 0, "API returned successfully without any errors."),
               ("CY_ERROR_ACCESS_DENIED", 1, "Access of the API is denied for the application"),
               ("CY_ERROR_DRIVER_INIT_FAILED", 2, "Driver initialisation failed"),
               ("CY_ERROR_DEVICE_INFO_FETCH_FAILED", 3, "Device information fetch failed"),
               ("CY_ERROR_DRIVER_OPEN_FAILED", 4, "Failed to open a device in the library"),
               ("CY_ERROR_INVALID_PARAMETER", 5, "One or more parameters sent to the API was invalid"),
               ("CY_ERROR_REQUEST_FAILED", 6, "Request sent to USB Serial device failed"),
               ("CY_ERROR_DOWNLOAD_FAILED", 7, "Firmware download to the device failed"),
               ("CY_ERROR_FIRMWARE_INVALID_SIGNATURE", 8, "Invalid Firmware signature in firmware file"),
               ("CY_ERROR_INVALID_FIRMWARE", 9, "Invalid firmware"),
               ("CY_ERROR_DEVICE_NOT_FOUND", 10, "Device disconnected"),
               ("CY_ERROR_IO_TIMEOUT", 11, "Timed out while processing a user request"),
               ("CY_ERROR_PIPE_HALTED", 12, "Pipe halted while trying to transfer data"),
               ("CY_ERROR_BUFFER_OVERFLOW", 13, "OverFlow of buffer while trying to read/write data"),
               ("CY_ERROR_INVALID_HANDLE", 14, "Device handle is invalid"),
               ("CY_ERROR_ALLOCATION_FAILED", 15, "Error in Allocation of the resource inside the library"),
               ("CY_ERROR_I2C_DEVICE_BUSY", 16, "I2C device busy"),
               ("CY_ERROR_I2C_NAK_ERROR", 17, "I2C device NAK"),
               ("CY_ERROR_I2C_ARBITRATION_ERROR", 18, "I2C bus arbitration error"),
               ("CY_ERROR_I2C_BUS_ERROR", 19, "I2C bus error"),
               ("CY_ERROR_I2C_BUS_BUSY", 20, "I2C bus is busy"),
               ("CY_ERROR_I2C_STOP_BIT_SET", 21, "I2C master has sent a stop bit during a transaction"),
               ("CY_ERROR_STATUS_MONITOR_EXIST", 22, "API Failed because the SPI/UART status monitor thread already exists")]

    @classmethod
    def _init(cls):
        for s in cls._status:
            setattr(cls, s[0], s[1])

    @classmethod
    def Name(cls, status):
        if 0 <= status < len(cls._status):
            return cls._status[status][0]
        return "Unknown Cypress Error"

    @classmethod
    def Description(cls, status):
        if 0 <= status < len(cls._status):
            return cls._status[status][2]
        return "Unknown Cypress Error"

    def __init__(self, status):
        self.status = status

    def name(self):
        return CypressError.Name(self.status)

    def description(self):
        return CypressError.Description(self.status)

    def __repr__(self):
        return "<CypressError: %s (%d) = %s>" % (self.name(), self.status, self.description())

    def __str__(self):
        return self.__repr__()


CypressError._init()


class Cypress(object):

    """ instantiate this class to access a Cypress device, which can perform
        i2c input/output, or read/write GPIO signals on the board.

        Example:

        with Cypress(0x36) as dev:
            dev.write([0xD2])
            patch, minor, major = unpack('HBB', buffer(bytearray(dev.read(4))))
            print "ASIC Software Version: %d.%d.%d" % (major, minor, patch)

        Constructs Cypress object with I2C slave address of attached device,
        0x36 in this example.  Then writes a 1 byte command (0xD2), and then
        reads 4 bytes, which is decoded as an unsigned short, and two unsigned
        chars ('HBB').
    """

    class CYVIDPID(Structure):
        _fields_ = [("vid", c_uint16),
                    ("pid", c_uint16)]

    class CYLIBRARYVERSION(Structure):
        _fields_ = [("majorVersion", c_ubyte),
                    ("minorVersion", c_ubyte),
                    ("patch", c_uint16),
                    ("buildNumber", c_ubyte)]

    class CYFIRMWAREVERSION(Structure):
        _fields_ = [("majorVersion", c_ubyte),
                    ("minorVersion", c_ubyte),
                    ("patchNumber", c_uint16),
                    ("buildNumber", c_uint32)]

    # noinspection PyTypeChecker
    class CYDEVICEINFO(Structure):
        _fields_ = [("vid", c_uint16),
                    ("pid", c_uint16),
                    ("numInterfaces", c_ubyte),
                    ("manufacturerName", c_char * 256),
                    ("productName", c_char * 256),
                    ("serialNum", c_char * 256),
                    ("deviceFriendlyName", c_char * 256),
                    ("deviceType", c_int32 * 5),
                    ("deviceClass", c_int32 * 5),
                    ("deviceBlock", c_int32)]

    class CYDATABUFFER(Structure):
        _fields_ = [("buffer", POINTER(c_ubyte)),
                    ("length", c_uint32),
                    ("transferCount", c_uint32)]

    class CYI2CCONFIG(Structure):
        _fields_ = [("frequency", c_uint32),
                    ("slaveAddress", c_ubyte),
                    ("isMaster", c_uint32),
                    ("isClockStretch", c_uint32)]

    class CYI2CDATACONFIG(Structure):
        _fields_ = [("slaveAddress", c_ubyte),
                    ("isStopBit", c_uint32),
                    ("isNakBit", c_uint32)]

    class CYSPICONFIG(Structure):
        _fields_ = [("frequency", c_uint32),
                    ("dataWidth", c_ubyte),
                    ("protocol", c_int32),
                    ("isMsbFirst", c_uint32),
                    ("isMaster", c_uint32),
                    ("isContinuousMode", c_uint32),
                    ("isSelectPrecede", c_uint32),
                    ("isCpha", c_uint32),
                    ("isCpol", c_uint32)]

    def __init__(self, slave=0x34, instance_or_serial=0,
                 devtype=CY_DEVICE_TYPE.CY_TYPE_I2C, product=None):
        """ construct a Cypress object """
        self.dll = None
        self.handle = None
        self.slave = slave
        self.instance = instance_or_serial
        self.devtype = devtype
        self.product = product
        self.timeout = 1000  # ms
        self.retries = 3

    def __enter__(self):
        """ called when using python with statement:
                with Cypress(0x36) as dev:
                    # do something
            After the with statement, __exit__ is called to close the device
        """
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ called after using python with statement """
        self.close()
        return False

    def _find_device(self, vid, pid, instance, serial, devtype, product):
        num = self.GetListofDevices()
        count = -1
        for i in range(num):
            devInfo = self.GetDeviceInfo(i)
            if devInfo.deviceType[0] != devtype:
                # print "devtype mismatch", devInfo.deviceType[0], devtype
                continue
            if vid and pid and (devInfo.vid != vid or devInfo.pid != pid):
                # print "vid/pid mismatch", (devInfo.vid, devInfo.pid), (vid, pid)
                continue
            if serial and devInfo.serialNum != serial:
                # print "serialNum mismatch", devInfo.serialNum, serial
                continue
            if product and product not in devInfo.productName:
                # print "product mismatch", devInfo.productName, product
                continue
            if not serial:
                count += 1
                if count != instance:
                    # print "instance mismatch", count, instance
                    continue
            return i
        return -1

    def open(self):
        """ open Cypress if not opened, yet.  opens by serial-id if
            instance is given as a string, else assumes instance is 0-n
        """
        if not self.handle:
            if type(self.instance) is str:
                devnum = self._find_device(None, None, None,
                                           self.instance, self.devtype,
                                           self.product)
            else:
                devnum = self._find_device(None, None, self.instance,
                                           None, self.devtype, self.product)
            if devnum >= 0:
                self.handle = self.Open(devnum, 0)
            else:
                raise ValueError("No Cypress device found")
        else:
            raise ValueError("Cypress already open")

        self.reset()

    def close(self):
        """ close Cypress device if opened """
        if self.handle:
            self.Close(self.handle)
            self.handle = None

    def read(self, numbytes, sendbytes=None, slave=None):
        """ read from Cypress device, optionally writing 'sendbytes' before
            reading. the slave address given at construction can be overridden
            using the 'slave' parameter.  returns a list of bytes read.
        """
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        if self.devtype == CY_DEVICE_TYPE.CY_TYPE_I2C:
            if sendbytes is not None:
                self.write(sendbytes, slave)
            return self.I2cRead(self.handle, slave or self.slave,
                                numbytes, self.timeout)
        elif self.devtype == CY_DEVICE_TYPE.CY_TYPE_SPI:
            return self.SpiReadWrite(self.handle, sendbytes, numbytes, self.timeout)

    def write(self, sendbytes, bytes_to_read=0, slave=None):
        """ write 'sendbytes' to the Cypress device.  the slave address given
            at construction can be overridden using the 'slave' parameter
        """
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        if self.devtype == CY_DEVICE_TYPE.CY_TYPE_I2C:
            self.I2cWrite(self.handle, slave or self.slave, sendbytes, self.timeout)
        elif self.devtype == CY_DEVICE_TYPE.CY_TYPE_SPI:
            return self.SpiReadWrite(self.handle, sendbytes, bytes_to_read, self.timeout)

    def gpio(self, pinnums, values=None):
        """ read or write gpio pins """
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        if values is not None:  # writing
            try:
                iter(pinnums)
            except TypeError:  # single pin/value
                self.SetGpioValue(self.handle, pinnums, values)
            else:  # list of pins/values
                for pin, value in zip(pinnums, values):
                    self.SetGpioValue(self.handle, pin, value)
        elif values is None:  # reading
            try:
                iter(pinnums)
            except TypeError:  # single pin
                return self.GetGpioValue(self.handle, pinnums)
            else:  # list of pins, result is a list, too
                result = []
                for pin in pinnums:
                    result.append(self.GetGpioValue(self.handle, pin))
                return result

    def get_speed(self):
        """ return the current I2C bus speed in KHz used by Cypress """
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        if self.devtype == CY_DEVICE_TYPE.CY_TYPE_I2C:
            return self.GetI2cConfig(self.handle)[0] // 1000
        elif self.devtype == CY_DEVICE_TYPE.CY_TYPE_SPI:
            return self.GetSpiConfig(self.handle)[0] // 1000

    def set_speed(self, speed_in_khz):
        """ set the current bus speed in KHz used by Cypress """
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        if self.devtype == CY_DEVICE_TYPE.CY_TYPE_I2C:
            cfg = list(self.GetI2cConfig(self.handle))
        elif self.devtype == CY_DEVICE_TYPE.CY_TYPE_SPI:
            cfg = list(self.GetSpiConfig(self.handle))
        else:
            raise ValueError('unsupported device type')
        cfg[0] = speed_in_khz * 1000
        if self.devtype == CY_DEVICE_TYPE.CY_TYPE_I2C:
            self.SetI2cConfig(self.handle, *cfg)
        elif self.devtype == CY_DEVICE_TYPE.CY_TYPE_SPI:
            self.SetSpiConfig(self.handle, *cfg)

    def set_mode(self, mode):
        """set current SPI mode"""
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        if self.devtype != CY_DEVICE_TYPE.CY_TYPE_SPI:
            raise ValueError("Device is not SPI, cannot set mode!")
        polarity = (mode >> 1) & 1
        phase = mode & 1
        cfg = list(self.GetSpiConfig(self.handle))
        cfg[-2] = phase
        cfg[-1] = polarity
        self.SetSpiConfig(self.handle, *cfg)

    def reset(self):
        """ resets the Cypress I2C engine """
        if self.handle is None:
            raise ValueError("Device not open (call open() or 'with Cypress()')")
        self.I2cReset(self.handle, 0)  # reset read side
        self.I2cReset(self.handle, 1)  # reset write side

    def unload(self):
        """ close and 'unload' the Cypress dll """
        self.close()
        self.dll = None

    def load(self):
        """ load and define the functions in the Cypress dll """
        self.dll = cdll.cyusbserial

        self.dll.CyGetListofDevices.argtypes = [POINTER(c_ubyte)]
        self.dll.CyGetListofDevices.restype = c_int32

        self.dll.CyGetDeviceInfo.argtypes = [c_ubyte,
                                             POINTER(self.CYDEVICEINFO)]
        self.dll.CyGetDeviceInfo.restype = c_int32

        self.dll.CyOpen.argtypes = [c_ubyte, c_ubyte, POINTER(c_void_p)]
        self.dll.CyOpen.restype = c_int32

        self.dll.CyClose.argtypes = [c_void_p]
        self.dll.CyClose.restype = c_int32

        self.dll.CySetGpioValue.argtypes = [c_void_p, c_ubyte, c_ubyte]
        self.dll.CySetGpioValue.restype = c_int32

        self.dll.CyGetGpioValue.argtypes = [c_void_p, c_ubyte, POINTER(c_ubyte)]
        self.dll.CyGetGpioValue.restype = c_int32

        self.dll.CyGetLibraryVersion.argtypes = [c_void_p,
                                                 POINTER(self.CYLIBRARYVERSION)]
        self.dll.CyGetLibraryVersion.restype = c_int32

        self.dll.CyGetFirmwareVersion.argtypes = [c_void_p, POINTER(self.CYFIRMWAREVERSION)]
        self.dll.CyGetFirmwareVersion.restype = c_int32

        self.dll.CyGetI2cConfig.argtypes = [c_void_p, POINTER(self.CYI2CCONFIG)]
        self.dll.CyGetI2cConfig.restype = c_int32

        self.dll.CySetI2cConfig.argtypes = [c_void_p, POINTER(self.CYI2CCONFIG)]
        self.dll.CySetI2cConfig.restype = c_int32

        self.dll.CyI2cRead.argtypes = [c_void_p,
                                       POINTER(self.CYI2CDATACONFIG),
                                       POINTER(self.CYDATABUFFER),
                                       c_uint32]
        self.dll.CyI2cRead.restype = c_int32

        self.dll.CyI2cWrite.argtypes = [c_void_p,
                                        POINTER(self.CYI2CDATACONFIG),
                                        POINTER(self.CYDATABUFFER),
                                        c_uint32]
        self.dll.CyI2cWrite.restype = c_int32

        self.dll.CyI2cReset.argtypes = [c_void_p, c_int32]
        self.dll.CyI2cReset.restype = c_int32

        self.dll.CyGetSpiConfig.argtypes = [c_void_p, POINTER(self.CYSPICONFIG)]
        self.dll.CyGetSpiConfig.restype = c_int32

        self.dll.CySetSpiConfig.argtypes = [c_void_p, POINTER(self.CYSPICONFIG)]
        self.dll.CySetSpiConfig.restype = c_int32

        self.dll.CySpiReadWrite.argtypes = [c_void_p,
                                            POINTER(self.CYDATABUFFER),
                                            POINTER(self.CYDATABUFFER),
                                            c_uint32]
        self.dll.CySpiReadWrite.restype = c_int32

    def GetListofDevices(self):
        if self.dll is None:
            self.load()
        numDevices = c_ubyte(0)
        status = self.dll.CyGetListofDevices(byref(numDevices))
        if status:
            raise CypressError(status)
        return numDevices.value

    def GetDeviceInfo(self, device_number):
        if self.dll is None:
            self.load()
        devInfo = self.CYDEVICEINFO()
        status = self.dll.CyGetDeviceInfo(device_number, byref(devInfo))
        if status:
            raise CypressError(status)
        return devInfo

    def Open(self, device, iface):
        if self.dll is None:
            self.load()
        handle = c_void_p()
        status = self.dll.CyOpen(device, iface, byref(handle))
        if status:
            raise CypressError(status)
        return handle

    def Close(self, handle):
        if self.dll is None:
            self.load()
        status = self.dll.CyClose(handle)
        if status:
            raise CypressError(status)

    def GetLibraryVersion(self, handle):
        if self.dll is None:
            self.load()
        version = self.CYLIBRARYVERSION()
        status = self.dll.CyGetLibraryVersion(handle, byref(version))
        if status:
            raise CypressError(status)
        return (version.majorVersion, version.minorVersion,
                version.patch, version.buildNumber)

    def GetFirmwareVersion(self, handle):
        if self.dll is None:
            self.load()
        version = self.CYFIRMWAREVERSION()
        status = self.dll.CyGetFirmwareVersion(handle, byref(version))
        if status:
            raise CypressError(status)
        return (version.majorVersion, version.minorVersion,
                version.patchNumber, version.buildNumber)

    def SetGpioValue(self, handle, gpionum, value):
        if self.dll is None:
            self.load()
        status = self.dll.CySetGpioValue(handle, gpionum, value)
        if status:
            raise CypressError(status)

    def GetGpioValue(self, handle, gpionum):
        if self.dll is None:
            self.load()
        value = c_ubyte(0)
        status = self.dll.CyGetGpioValue(handle, gpionum, byref(value))
        if status:
            raise CypressError(status)
        return value.value

    def GetI2cConfig(self, handle):
        if self.dll is None:
            self.load()
        cfg = self.CYI2CCONFIG()
        status = self.dll.CyGetI2cConfig(handle, byref(cfg))
        if status:
            raise CypressError(status)
        return (cfg.frequency, cfg.slaveAddress,
                cfg.isMaster, cfg.isClockStretch)

    def SetI2cConfig(self, handle, freq, slave_addr, master, stretch):
        if self.dll is None:
            self.load()
        cfg = self.CYI2CCONFIG(freq, slave_addr, master, stretch)
        status = self.dll.CySetI2cConfig(handle, byref(cfg))
        if status:
            raise CypressError(status)

    def I2cRead(self, handle, slave_addr, bytes_to_read, timeout=2000):
        if self.dll is None:
            self.load()
        datacfg = self.CYI2CDATACONFIG(slave_addr >> 1, 0, 0)
        readbuf = (c_ubyte * bytes_to_read)(0)
        databuf = self.CYDATABUFFER(readbuf, bytes_to_read, 0)
        status = self.dll.CyI2cRead(handle, byref(datacfg),
                                    byref(databuf), timeout)
        if status:
            raise CypressError(status)
        return readbuf[:databuf.transferCount]

    def I2cWrite(self, handle, slave_addr, sendbytes, timeout=2000):
        if self.dll is None:
            self.load()
        datacfg = self.CYI2CDATACONFIG(slave_addr >> 1, 0, 0)
        # noinspection PyCallingNonCallable,PyTypeChecker
        writebuf = (c_ubyte * len(sendbytes))(*sendbytes)
        databuf = self.CYDATABUFFER(writebuf, len(sendbytes), 0)
        status = self.dll.CyI2cWrite(handle, byref(datacfg),
                                     byref(databuf), timeout)
        if status:
            raise CypressError(status)

    def I2cReset(self, handle, resetmode):
        if self.dll is None:
            self.load()
        status = self.dll.CyI2cReset(handle, resetmode)
        if status:
            raise CypressError(status)

    def GetSpiConfig(self, handle):
        if self.dll is None:
            self.load()
        cfg = self.CYSPICONFIG()
        memset(addressof(cfg), 0, sizeof(cfg))
        status = self.dll.CyGetSpiConfig(handle, byref(cfg))
        if status:
            raise CypressError(status)
        return (cfg.frequency, cfg.dataWidth, cfg.protocol, cfg.isMsbFirst,
                cfg.isMaster, cfg.isContinuousMode, cfg.isSelectPrecede,
                cfg.isCpha, cfg.isCpol)

    def SetSpiConfig(self, handle, frequency, data_width, protocol, is_msb_first,
                     is_master, is_continuous_mode, is_select_precede, is_cpha, is_cpol):
        if self.dll is None:
            self.load()
        cfg = self.CYSPICONFIG(frequency, data_width, protocol, is_msb_first,
                               is_master, is_continuous_mode, is_select_precede,
                               is_cpha, is_cpol)
        status = self.dll.CySetSpiConfig(handle, byref(cfg))
        if status:
            raise CypressError(status)

    def SpiReadWrite(self, handle, data_to_write, bytes_to_read, timeout=1000):
        if self.dll is None:
            self.load()
        readdata = readbuf = writedata = None
        if bytes_to_read:
            readbuf = (c_ubyte * bytes_to_read)(0)
            readdata = byref(self.CYDATABUFFER(readbuf, bytes_to_read, 0))
        if data_to_write:
            # noinspection PyCallingNonCallable,PyTypeChecker
            writebuf = (c_ubyte * len(data_to_write))(*data_to_write)
            writedata = byref(self.CYDATABUFFER(writebuf, len(data_to_write), 0))
        status = self.dll.CySpiReadWrite(handle, readdata, writedata, timeout)
        if status:
            raise CypressError(status)
        if readbuf:
            # noinspection PyProtectedMember
            return readbuf[:readdata._obj.transferCount]


class LightCrafterDisplay(object):

    def __init__(self, cypress):
        self.cypress = cypress
        self.enter_count = 0

    def __enter__(self):
        """ called when using python with statement:
                with Cypress(0x36) as cy, LightCrafterDisplay(cy) as lcd:
                    # do something
            After the with statement, __exit__ is called to close the device
        """
        if self.enter_count == 0:
            self.cypress.gpio([5, 9], [1, 1])
            while not self.cypress.gpio(6):
                pass
        self.enter_count += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ called after using python with statement """
        self.enter_count -= 1
        if self.enter_count == 0:
            self.cypress.gpio([5, 9], [0, 0])
        return False
