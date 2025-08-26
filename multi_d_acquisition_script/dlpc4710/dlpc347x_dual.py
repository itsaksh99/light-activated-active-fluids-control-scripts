#-------------------------------------------------------------------------------
# Copyright (c) 2024 Texas Instruments Incorporated - http://www.ti.com/
#-------------------------------------------------------------------------------
#
# NOTE: This file is auto generated from a command definition file.
#       Please do not modify the file directly.                    
#
# Command Spec Version : 1.0
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the
#   distribution.
#
#   Neither the name of Texas Instruments Incorporated nor the names of
#   its contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import struct
from enum import Enum

import sys, os.path
python_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__))))
sys.path.append(python_dir)
from packer import *

class OperatingMode(Enum):
    ExternalVideoPort = 0
    TestPatternGenerator = 1
    SplashScreen = 2
    SensExternalPattern = 3
    SensInternalPattern = 4
    SensSplashPattern = 5
    Standby = 255

class ChromaInterpolationMethod(Enum):
    ChromaInterpolation = 0
    ChromaCopy = 1

class ChromaChannelSwap(Enum):
    Cbcr = 0
    Crcb = 1

class ImageCurtainEnable(Enum):
    Disable = 0
    Enable = 1

class ControllerDeviceId(Enum):
    Dlpc3430 = 0
    Dlpc3433 = 1
    Dlpc3432 = 2
    Dlpc3434 = 3
    Dlpc3435 = 4
    Dlpc3438 = 5
    Dlpc3436 = 6
    Dlpc3437 = 7
    Dlpc3472 = 8
    Dlpc3439 = 9
    Dlpc3440 = 10
    Dlpc3478 = 11
    Dlpc3479 = 12
    Dlpc3470 = 15

class ExternalVideoFormat(Enum):
    Dsi = 0
    ParallelRgb565Bw16 = 64
    ParallelRgb666Bw18 = 65
    ParallelRgb888Bw8 = 66
    ParallelRgb888Bw24 = 67
    ParallelYcbcr666Bw18 = 80
    ParallelYcbcr888Bw24 = 81
    ParallelYcbcr422Bw8 = 96
    ParallelYcbcr422Bw16 = 97
    Bt656 = 160

class Color(Enum):
    Black = 0
    Red = 1
    Green = 2
    Blue = 3
    Cyan = 4
    Magenta = 5
    Yellow = 6
    White = 7

class DiagonalLineSpacing(Enum):
    Dls3 = 3
    Dls7 = 7
    Dls15 = 15
    Dls31 = 31
    Dls63 = 63
    Dls127 = 127
    Dls255 = 255

class TestPattern(Enum):
    SolidField = 0
    HorizontalRamp = 1
    VerticalRamp = 2
    HorizontalLines = 3
    DiagonalLines = 4
    VerticalLines = 5
    Grid = 6
    Checkerboard = 7
    Colorbars = 8

class PixelFormats(Enum):
    Rgb565 = 2
    Ycbcr422 = 3

class CompressionTypes(Enum):
    Uncompressed = 0
    RgbRleCompressed = 1
    Unused = 2
    YuvRleCompressed = 3

class ColorOrders(Enum):
    Rgb = 0
    Grb = 1

class ChromaOrders(Enum):
    CrFirst = 0
    CbFirst = 1

class ByteOrders(Enum):
    LittleEndian = 0
    BigEndian = 1

class ImageFlip(Enum):
    ImageNotFlipped = 0
    ImageFlipped = 1

class BorderEnable(Enum):
    Disable = 0
    Enable = 1

class LedControlMethod(Enum):
    Manual = 0
    Automatic = 1

class LabbControl(Enum):
    Disabled = 0
    Manual = 1
    Automatic = 2

class CaicGainDisplayScale(Enum):
    P1024 = 0
    P512 = 1

class BorderColorSource(Enum):
    Command = 0
    Flash = 1

class SystemInit(Enum):
    NotComplete = 0
    Complete = 1

class Error(Enum):
    NoError = 0
    Error = 1

class SensingError(Enum):
    NoError = 0
    IlluminationTimeNotSupported = 1
    PreIlluminationTimeNotSupported = 2
    PostIlluminationTimeNotSupported = 3
    TriggerOut1DelayNotSupported = 4
    TriggerOut2DelayNotSupported = 5
    MaxPatternOrderTableEntriesExceeded = 6
    ExternalPatternPeriodError = 7

class FlashErase(Enum):
    Complete = 0
    NotComplete = 1

class Application(Enum):
    BootApp = 0
    MainApp = 1

class LedState(Enum):
    LedOff = 0
    LedOn = 1

class PowerSupply(Enum):
    SupplyVoltageNormal = 0
    SupplyVoltageLow = 1

class ControllerConfiguration(Enum):
    Single = 0
    Dual = 1

class MasterOrSlaveOperation(Enum):
    Master = 0
    Slave = 1

class WatchdogTimeout(Enum):
    NoTimeout = 0
    Timeout = 1

class DmdDataSelection(Enum):
    DmdDeviceId = 0
    DmdFuseGroup0 = 1
    DmdFuseGroup1 = 2
    DmdFuseGroup2 = 3
    DmdFuseGroup3 = 4

class TriggerType(Enum):
    Trigger1 = 0
    Trigger2 = 1

class TriggerEnable(Enum):
    Disable = 0
    Enable = 1

class TriggerInversion(Enum):
    NotInverted = 0
    Inverted = 1

class TriggerPolarity(Enum):
    ActiveLow = 0
    ActiveHi = 1

class SequenceType(Enum):
    OneBitMono = 0
    OneBitRgb = 1
    EightBitMono = 2
    EightBitRgb = 3

class IlluminatorEnable(Enum):
    Disable = 0
    Enable = 1

class PatternControl(Enum):
    Start = 0
    Stop = 1
    Pause = 2
    Step = 3
    Resume = 4
    Reset = 5

class WriteControl(Enum):
    Continue = 0
    Start = 1
    ReloadFromFlash = 2

class PatternReadyStatus(Enum):
    NotReady = 0
    Ready = 1

class PatternMode(Enum):
    External = 0
    Internal = 1
    Splash = 2

class ExposureTimeSupported(Enum):
    No = 0
    Yes = 1

class ZeroDarkTimeSupported(Enum):
    No = 0
    Yes = 1

class FlashDataTypeSelect(Enum):
    EntireFlash = 0
    EntireFlashNoOem = 2
    MainApp = 16
    TiApp = 32
    BatchFiles = 48
    Looks = 64
    Sequences = 80
    Cmt = 96
    Cca = 112
    Gluts = 128
    Splash = 144
    OemCal = 160
    OemScratchpadFull0 = 176
    OemScratchpadPartial0 = 177
    OemScratchpadFull1 = 178
    OemScratchpadPartial1 = 179
    OemScratchpadFull2 = 180
    OemScratchpadPartial2 = 181
    OemScratchpadFull3 = 181
    OemScratchpadPartial3 = 183
    EntireSensPatternData = 208
    EntireSensSeqData = 224

class ThreeDModes(Enum):
    TwoDOperation = 0
    ThreeDOperation = 1

class ThreeDDominance(Enum):
    LeftDominantLeftEyeFirst = 0
    RightDominantRightEyeFirst = 1

class ThreeDReferencePolarity(Enum):
    CorrectNoInversionRequired = 0
    IncorrectInversionRequired = 1

class Summary:
    Command: str
    CommInterface: str
    Successful: bool

class ProtocolData:
    CommandDestination: int
    OpcodeLength: int
    BytesRead: int

class SplashScreenHeader:
     WidthInPixels: int                     # int
     HeightInPixels: int                    # int
     SizeInBytes: int                       # int
     PixelFormat: PixelFormats
     CompressionType: CompressionTypes
     ColorOrder: ColorOrders
     ChromaOrder: ChromaOrders
     ByteOrder: ByteOrders

class GridLines:
     Border: BorderEnable
     BackgroundColor: Color
     ForegroundColor: Color
     HorizontalForegroundLineWidth: int     # int
     HorizontalBackgroundLineWidth: int     # int
     VerticalForegroundLineWidth: int       # int
     VerticalBackgroundLineWidth: int       # int

class TestPatternSelect:
     PatternSelect: TestPattern
     Border: BorderEnable
     BackgroundColor: Color
     ForegroundColor: Color
     StartValue: int                        # int
     EndValue: int                          # int
     ForegroundLineWidth: int               # int
     BackgroundLineWidth: int               # int
     HorizontalSpacing: int                 # int
     VerticalSpacing: int                   # int
     HorizontalForegroundLineWidth: int     # int
     HorizontalBackgroundLineWidth: int     # int
     HorizontalCheckerCount: int            # int
     VerticalForegroundLineWidth: int       # int
     VerticalBackgroundLineWidth: int       # int
     VerticalCheckerCount: int              # int

class SequenceHeaderAttributes:
     LookRedDutyCycle: float
     LookGreenDutyCycle: float
     LookBlueDutyCycle: float
     LookMaxFrameTime: float
     LookMinFrameTime: float
     LookMaxSequenceVectors: int            # int
     SeqRedDutyCycle: float
     SeqGreenDutyCycle: float
     SeqBlueDutyCycle: float
     SeqMaxFrameTime: float
     SeqMinFrameTime: float
     SeqMaxSequenceVectors: int             # int

class ShortStatus:
     SystemInitialized: SystemInit
     CommunicationError: Error
     SystemError: Error
     FlashEraseComplete: FlashErase
     FlashError: Error
     SensingSequenceError: Error
     Application: Application

class SystemStatus:
     DmdDeviceError: Error
     DmdInterfaceError: Error
     DmdTrainingError: Error
     RedLedEnableState: LedState
     GreenLedEnableState: LedState
     BlueLedEnableState: LedState
     RedLedError: Error
     GreenLedError: Error
     BlueLedError: Error
     SequenceAbortError: Error
     SequenceError: Error
     DcPowerSupply: PowerSupply
     SensingError: SensingError
     ControllerConfiguration: ControllerConfiguration
     MasterOrSlaveOperation: MasterOrSlaveOperation
     ProductConfigurationError: Error
     WatchdogTimerTimeout: WatchdogTimeout

class CommunicationStatus:
     InvalidCommandError: Error
     InvalidCommandParameterValue: Error
     CommandProcessingError: Error
     FlashBatchFileError: Error
     ReadCommandError: Error
     InvalidNumberOfCommandParameters: Error
     BusTimeoutByDisplayError: Error
     AbortedOpCode: int                     # int

class PatternConfiguration:
     SequenceType: SequenceType
     NumberOfPatterns: int                  # int
     RedIlluminator: IlluminatorEnable
     GreenIlluminator: IlluminatorEnable
     BlueIlluminator: IlluminatorEnable
     IlluminationTime: int                  # int
     PreIlluminationDarkTime: int           # int
     PostIlluminationDarkTime: int          # int

class PatternOrderTableEntry:
     PatSetIndex: int                       # int
     NumberOfPatternsToDisplay: int         # int
     RedIlluminator: IlluminatorEnable
     GreenIlluminator: IlluminatorEnable
     BlueIlluminator: IlluminatorEnable
     PatternInvertLsword: int               # int
     PatternInvertMsword: int               # int
     IlluminationTime: int                  # int
     PreIlluminationDarkTime: int           # int
     PostIlluminationDarkTime: int          # int

class InternalPatternStatus:
     PatternReadyStatus: PatternReadyStatus
     NumPatOrderTableEntries: int           # int
     CurrentPatOrderEntryIndex: int         # int
     CurrentPatSetIndex: int                # int
     NumPatInCurrentPatSet: int             # int
     NumPatDisplayedFromPatSet: int         # int
     NextPatSetIndex: int                   # int

_readcommand = None
_writecommand = None

def DLPC347X_DUALinit(readcommandcb, writecommandcb):
    global _readcommand
    global _writecommand
    _readcommand = readcommandcb
    _writecommand = writecommandcb

    global Summary
    deviceid = ReadDmdDeviceId(DmdDataSelection.DmdDeviceId)[1]
    # print(deviceid)
    evmtype = deviceid >> 24
    if evmtype in [0x26, 0x64, 0x69, 0x8D]:
        Summary.CommInterface = "DLP2010EVM-LC"
    elif evmtype in [0x16, 0x68, 0x72, 0x87]:
        Summary.CommInterface = "DLP3010EVM-LC"
    elif evmtype == [0x6B, 0x73, 0x8A]:
        Summary.CommInterface = "DLP4710EVM-LC"

    global PortocolData
    ProtocolData.CommandDestination = 0
    ProtocolData.OpcodeLength = 0
    ProtocolData.BytesRead = 0

def WriteOperatingModeSelect(OperatingMode):
    "Selects the image operating mode for the projection module."
    global Summary
    Summary.Command = "Write Operating Mode Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',5))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',OperatingMode.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadOperatingModeSelect():
    "Reads the state of the image operating mode for the projection module."
    global Summary
    Summary.Command = "Read Operating Mode Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',6))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        OperatingModeObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, OperatingMode(OperatingModeObj)

def WriteSplashScreenSelect(SplashScreenIndex):
    "Selects the index of a splash screen that is to be displayed. See also Write Splash Screen Execute."
    global Summary
    Summary.Command = "Write Splash Screen Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',13))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SplashScreenIndex)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSplashScreenSelect():
    "Returns the index of a splash screen that is to be displayed (or is being displayed)."
    global Summary
    Summary.Command = "Read Splash Screen Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',14))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        SplashScreenIndex = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SplashScreenIndex

def WriteSplashScreenExecute():
    "Retrieves the select splash screen from flash for display on the projection module. See also Write Splash Screen Select."
    global Summary
    Summary.Command = "Write Splash Screen Execute"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',53))
        ProtocolData.OpcodeLength = 1;
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadSplashScreenHeader(SplashScreenIndex):
    "Read Splash screen header"
    global Summary
    Summary.Command = "Read Splash Screen Header"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',15))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',SplashScreenIndex)))
        readbytes = _readcommand(13, writebytes, ProtocolData)
        SplashScreenHeader.WidthInPixels = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        SplashScreenHeader.HeightInPixels = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        SplashScreenHeader.SizeInBytes = struct.unpack_from ('I', bytearray(readbytes), 4)[0]
        SplashScreenHeader.PixelFormat = struct.unpack_from ('B', bytearray(readbytes), 8)[0]
        SplashScreenHeader.CompressionType = struct.unpack_from ('B', bytearray(readbytes), 9)[0]
        SplashScreenHeader.ColorOrder = struct.unpack_from ('B', bytearray(readbytes), 10)[0]
        SplashScreenHeader.ChromaOrder = struct.unpack_from ('B', bytearray(readbytes), 11)[0]
        SplashScreenHeader.ByteOrder = struct.unpack_from ('B', bytearray(readbytes), 12)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SplashScreenHeader

def WriteExternalVideoSourceFormatSelect(VideoFormat):
    "Specifies the active external video port and the source data type for the projection module."
    global Summary
    Summary.Command = "Write External Video Source Format Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',7))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',VideoFormat.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadExternalVideoSourceFormatSelect():
    "Reads the state of the active external video port and the source data type for the projection module."
    global Summary
    Summary.Command = "Read External Video Source Format Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',8))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        VideoFormatObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ExternalVideoFormat(VideoFormatObj)

def WriteVideoChromaProcessingSelect(ChromaInterpolationMethod,  ChromaChannelSwap,  CscCoefficientSet):
    "Specifies the characteristics of the selected YCbCr source and the type of chroma processing that will be used for the YCbCr source in the projection module."
    global Summary
    Summary.Command = "Write Video Chroma Processing Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',9))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(ChromaInterpolationMethod.value, 1, 4)
        value = setbits(ChromaChannelSwap.value, 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(int(CscCoefficientSet), 2, 0)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadVideoChromaProcessingSelect():
    "Reads the specified characteristics for the selected YCrCb source and the chroma processing used."
    global Summary
    Summary.Command = "Read Video Chroma Processing Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',10))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ChromaInterpolationMethodObj = getbits(1, 4);
        ChromaChannelSwapObj = getbits(1, 3);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        CscCoefficientSet = getbits(2, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ChromaInterpolationMethod(ChromaInterpolationMethodObj), ChromaChannelSwap(ChromaChannelSwapObj), CscCoefficientSet

def Write3DControl(ThreeDFrameDominance,  ThreeDReferencePolarity):
    "Specifies the 3D frame dominance and reference polarity."
    global Summary
    Summary.Command = "Write 3 D Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',32))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(1, 1, 1)
        value = setbits(ThreeDFrameDominance.value, 1, 5)
        value = setbits(ThreeDReferencePolarity.value, 1, 6)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def Read3DControl():
    "Reads the 3D frame dominance and reference polarity."
    global Summary
    Summary.Command = "Read 3 D Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',33))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ThreeDModeObj = getbits(1, 0);
        ThreeDFrameDominanceObj = getbits(1, 5);
        ThreeDReferencePolarityObj = getbits(1, 6);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ThreeDModes(ThreeDModeObj), ThreeDDominance(ThreeDFrameDominanceObj), ThreeDReferencePolarity(ThreeDReferencePolarityObj)

def WriteInputImageSize(PixelsPerLine,  LinesPerFrame):
    "Specifies the active data size of the external input image to the projection module."
    global Summary
    Summary.Command = "Write Input Image Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',46))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',PixelsPerLine)))
        writebytes.extend(list(struct.pack('H',LinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadInputImageSize():
    "Reads the specified data size of the external input image to the projection module."
    global Summary
    Summary.Command = "Read Input Image Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',47))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        LinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PixelsPerLine, LinesPerFrame

def WriteDisplaySize(PixelsPerLine,  LinesPerFrame):
    "Specifies the size of the active image to be displayed on the projection module."
    global Summary
    Summary.Command = "Write Display Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',18))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',PixelsPerLine)))
        writebytes.extend(list(struct.pack('H',LinesPerFrame)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplaySize():
    "Reads the state of the display size settings for the projection module."
    global Summary
    Summary.Command = "Read Display Size"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',19))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PixelsPerLine = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        LinesPerFrame = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PixelsPerLine, LinesPerFrame

def WriteDisplayImageOrientation(LongAxisImageFlip,  ShortAxisImageFlip):
    "Specifies the image orientation of the displayed image for the projection module."
    global Summary
    Summary.Command = "Write Display Image Orientation"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',20))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(LongAxisImageFlip.value, 1, 1)
        value = setbits(ShortAxisImageFlip.value, 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplayImageOrientation():
    "Reads the state of the displayed image orientation function for the projection module."
    global Summary
    Summary.Command = "Read Display Image Orientation"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',21))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        LongAxisImageFlipObj = getbits(1, 1);
        ShortAxisImageFlipObj = getbits(1, 2);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImageFlip(LongAxisImageFlipObj), ImageFlip(ShortAxisImageFlipObj)

def WriteDisplayImageCurtain(Enable,  Color):
    "Controls the display image curtain for the projection module. An image curtain fills the entire display with the selected color regardless of selected operating mode (except for Internal Pattern Streaming)."
    global Summary
    Summary.Command = "Write Display Image Curtain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',22))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(Enable.value, 1, 0)
        value = setbits(Color.value, 3, 1)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadDisplayImageCurtain():
    "Reads the state of the image curtain control function for the projection module."
    global Summary
    Summary.Command = "Read Display Image Curtain"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',23))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        EnableObj = getbits(1, 0);
        ColorObj = getbits(3, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ImageCurtainEnable(EnableObj), Color(ColorObj)

def WriteImageFreeze(Enable):
    "Enables or disables the image freeze function for the projection module. If enabled, this preserves the current image data."
    global Summary
    Summary.Command = "Write Image Freeze"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',26))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Enable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadImageFreeze():
    "Reads the state of the image freeze function for the projection module."
    global Summary
    Summary.Command = "Read Image Freeze"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',27))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        Enable = struct.unpack_from ('?', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Enable

def WriteBorderColor(DisplayBorderColor):
    "Specifies the on screen border color for the projection module. Whenever the display image size is smaller than the display active area, this color fills the unused area."
    global Summary
    Summary.Command = "Write Border Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',178))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',DisplayBorderColor.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadBorderColor():
    "Reads the state of the on screen border color for the projection module."
    global Summary
    Summary.Command = "Read Border Color"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',179))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        DisplayBorderColorObj = getbits(3, 0);
        PillarBoxBorderColorSourceObj = getbits(1, 7);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Color(DisplayBorderColorObj), BorderColorSource(PillarBoxBorderColorSourceObj)

def WriteSolidField(Border,  ForegroundColor):
    "Writes a solid field pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Solid Field"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(0, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteHorizontalRamp(Border,  ForegroundColor,  StartValue,  EndValue):
    "Writes a horizontal ramp pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Horizontal Ramp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(1, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',StartValue)))
        writebytes.extend(list(struct.pack('B',EndValue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteVerticalRamp(Border,  ForegroundColor,  StartValue,  EndValue):
    "Writes a vertical ramp pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Vertical Ramp"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(2, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',StartValue)))
        writebytes.extend(list(struct.pack('B',EndValue)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteHorizontalLines(Border,  BackgroundColor,  ForegroundColor,  ForegroundLineWidth,  BackgroundLineWidth):
    "Writes a horizontal lines pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Horizontal Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(3, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(BackgroundColor.value, 3, 0)
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',ForegroundLineWidth)))
        writebytes.extend(list(struct.pack('B',BackgroundLineWidth)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteDiagonalLines(Border,  BackgroundColor,  ForegroundColor,  HorizontalSpacing,  VerticalSpacing):
    "Writes a diagonal lines pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Diagonal Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(4, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(BackgroundColor.value, 3, 0)
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',HorizontalSpacing.value)))
        writebytes.extend(list(struct.pack('B',VerticalSpacing.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteVerticalLines(Border,  BackgroundColor,  ForegroundColor,  ForegroundLineWidth,  BackgroundLineWidth):
    "Writes a vertical lines pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Vertical Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(5, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(BackgroundColor.value, 3, 0)
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',ForegroundLineWidth)))
        writebytes.extend(list(struct.pack('B',BackgroundLineWidth)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteGridLines(GridLines):
    "Writes a grid lines pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Grid Lines"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(6, 4, 0)
        value = setbits(GridLines.Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(GridLines.BackgroundColor.value, 3, 0)
        value = setbits(GridLines.ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',GridLines.HorizontalForegroundLineWidth)))
        writebytes.extend(list(struct.pack('B',GridLines.HorizontalBackgroundLineWidth)))
        writebytes.extend(list(struct.pack('B',GridLines.VerticalForegroundLineWidth)))
        writebytes.extend(list(struct.pack('B',GridLines.VerticalBackgroundLineWidth)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteCheckerboard(Border,  BackgroundColor,  ForegroundColor,  HorizontalCheckerCount,  VerticalCheckerCount):
    "Writes a checkerboard pattern as internal test pattern for display. 0: Disable, 1: Enable"
    global Summary
    Summary.Command = "Write Checkerboard"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(7, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        packerinit()
        value = setbits(BackgroundColor.value, 3, 0)
        value = setbits(ForegroundColor.value, 3, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('H',HorizontalCheckerCount)))
        writebytes.extend(list(struct.pack('H',VerticalCheckerCount)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteColorbars(Border):
    "Writes a colorbars pattern as internal test pattern for display."
    global Summary
    Summary.Command = "Write Colorbars"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',11))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(8, 4, 0)
        value = setbits(Border.value, 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTestPatternSelect():
    "Reads back the host-specified parameters for an internal test pattern."
    global Summary
    Summary.Command = "Read Test Pattern Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',12))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        TestPatternSelect.PatternSelect = getbits(4, 0);
        TestPatternSelect.Border = getbits(1, 7);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        TestPatternSelect.BackgroundColor = getbits(4, 0);
        TestPatternSelect.ForegroundColor = getbits(4, 4);
        readdata = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        TestPatternSelect.StartValue = getbits(8, 0);
        TestPatternSelect.EndValue = getbits(8, 8);
        TestPatternSelect.ForegroundLineWidth = getbits(8, 0);
        TestPatternSelect.BackgroundLineWidth = getbits(8, 8);
        TestPatternSelect.HorizontalSpacing = getbits(8, 0);
        TestPatternSelect.VerticalSpacing = getbits(8, 8);
        TestPatternSelect.HorizontalForegroundLineWidth = getbits(8, 0);
        TestPatternSelect.HorizontalBackgroundLineWidth = getbits(8, 8);
        TestPatternSelect.HorizontalCheckerCount = getbits(11, 0);
        readdata = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
        packerinit(readdata)
        TestPatternSelect.VerticalForegroundLineWidth = getbits(8, 0);
        TestPatternSelect.VerticalBackgroundLineWidth = getbits(8, 8);
        TestPatternSelect.VerticalCheckerCount = getbits(11, 0);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TestPatternSelect

def WriteExecuteFlashBatchFile(BatchFileNumber):
    "Executes a batch file stored in the flash image."
    global Summary
    Summary.Command = "Write Execute Flash Batch File"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',45))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',BatchFileNumber)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteBatchFileDelay(DelayInMicroseconds):
    "Delays for the specified number of microseconds. Only valid within a batch file."
    global Summary
    Summary.Command = "Write Batch File Delay"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',219))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',DelayInMicroseconds)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteLedOutputControlMethod(LedControlMethod):
    "Specifies the method for controlling the LED outputs for the projection module."
    global Summary
    Summary.Command = "Write Led Output Control Method"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',80))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',LedControlMethod.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadLedOutputControlMethod():
    "Reads the state of the LED output control method for the projection module."
    global Summary
    Summary.Command = "Read Led Output Control Method"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',81))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        LedControlMethodObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LedControlMethod(LedControlMethodObj)

def WriteRgbLedEnable(RedLedEnable,  GreenLedEnable,  BlueLedEnable):
    "Enables the LEDs for the projection module."
    global Summary
    Summary.Command = "Write Rgb Led Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',82))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(int(RedLedEnable), 1, 0)
        value = setbits(int(GreenLedEnable), 1, 1)
        value = setbits(int(BlueLedEnable), 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadRgbLedEnable():
    "Reads the state of the LED enables for the projection module."
    global Summary
    Summary.Command = "Read Rgb Led Enable"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',83))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        RedLedEnable = getbits(1, 0);
        GreenLedEnable = getbits(1, 1);
        BlueLedEnable = getbits(1, 2);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedLedEnable, GreenLedEnable, BlueLedEnable

def WriteRgbLedCurrent(RedLedCurrent,  GreenLedCurrent,  BlueLedCurrent):
    "Sets the IDAC register value of the PMIC for the red, green, and blue LEDs. This value directly controls the LED current."
    global Summary
    Summary.Command = "Write Rgb Led Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',84))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',RedLedCurrent)))
        writebytes.extend(list(struct.pack('H',GreenLedCurrent)))
        writebytes.extend(list(struct.pack('H',BlueLedCurrent)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadRgbLedCurrent():
    "Reads the state of the current for the red, green, and blue LEDs. This value directly controls the LED current."
    global Summary
    Summary.Command = "Read Rgb Led Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',85))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        RedLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        GreenLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        BlueLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedLedCurrent, GreenLedCurrent, BlueLedCurrent

def ReadCaicLedMaxAvailablePower():
    "Reads the specified maximum LED power (Watts) allowed for the projection module."
    global Summary
    Summary.Command = "Read Caic Led Max Available Power"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',87))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        MaxLedPower = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 100)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, MaxLedPower

def WriteRgbLedMaxCurrent(MaxRedLedCurrent,  MaxGreenLedCurrent,  MaxBlueLedCurrent):
    "Specifies the maximum LED current allowed for each LED in the projection module."
    global Summary
    Summary.Command = "Write Rgb Led Max Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',92))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',MaxRedLedCurrent)))
        writebytes.extend(list(struct.pack('H',MaxGreenLedCurrent)))
        writebytes.extend(list(struct.pack('H',MaxBlueLedCurrent)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadRgbLedMaxCurrent():
    "Reads the specified maximum LED current allowed for each LED in the projection module."
    global Summary
    Summary.Command = "Read Rgb Led Max Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',93))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        MaxRedLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        MaxGreenLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        MaxBlueLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, MaxRedLedCurrent, MaxGreenLedCurrent, MaxBlueLedCurrent

def ReadCaicRgbLedCurrent():
    "Reads the state of the current for the red, green, and blue LEDs of the projection module."
    global Summary
    Summary.Command = "Read Caic Rgb Led Current"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',95))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        RedLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        GreenLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 2)[0]
        BlueLedCurrent = struct.unpack_from ('H', bytearray(readbytes), 4)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, RedLedCurrent, GreenLedCurrent, BlueLedCurrent

def WriteLookSelect(LookNumber):
    "Specifies the Look for the image on the projection module. A Look typically specifies a target white point."
    global Summary
    Summary.Command = "Write Look Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',34))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',LookNumber)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadLookSelect():
    "Reads the state of the Look select command for the projection module."
    global Summary
    Summary.Command = "Read Look Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',35))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(6, writebytes, ProtocolData)
        LookNumber = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        SequenceIndex = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        SequenceFrameTime = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 2)[0], 15)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LookNumber, SequenceIndex, SequenceFrameTime

def ReadSequenceHeaderAttributes():
    "Reads Look and Sequence header information for the active Look and Sequence of the projection module."
    global Summary
    Summary.Command = "Read Sequence Header Attributes"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',38))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(30, writebytes, ProtocolData)
        SequenceHeaderAttributes.LookRedDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 255)
        SequenceHeaderAttributes.LookGreenDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 2)[0], 255)
        SequenceHeaderAttributes.LookBlueDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 4)[0], 255)
        SequenceHeaderAttributes.LookMaxFrameTime = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 6)[0], 15)
        SequenceHeaderAttributes.LookMinFrameTime = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 10)[0], 15)
        SequenceHeaderAttributes.LookMaxSequenceVectors = struct.unpack_from ('B', bytearray(readbytes), 14)[0]
        SequenceHeaderAttributes.SeqRedDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 15)[0], 255)
        SequenceHeaderAttributes.SeqGreenDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 17)[0], 255)
        SequenceHeaderAttributes.SeqBlueDutyCycle = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 19)[0], 255)
        SequenceHeaderAttributes.SeqMaxFrameTime = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 21)[0], 15)
        SequenceHeaderAttributes.SeqMinFrameTime = convertfixedtofloat(struct.unpack_from ('I', bytearray(readbytes), 25)[0], 15)
        SequenceHeaderAttributes.SeqMaxSequenceVectors = struct.unpack_from ('B', bytearray(readbytes), 29)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SequenceHeaderAttributes

def WriteLocalAreaBrightnessBoostControl(LabbControl,  SharpnessStrength,  LabbStrengthSetting):
    "Controls the local area brightness boost image processing functionality for the projection module."
    global Summary
    Summary.Command = "Write Local Area Brightness Boost Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',128))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(LabbControl.value, 2, 0)
        value = setbits(int(SharpnessStrength), 4, 4)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',LabbStrengthSetting)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadLocalAreaBrightnessBoostControl():
    "Reads the state of the local area brightness boost image processing functionality for the projection module."
    global Summary
    Summary.Command = "Read Local Area Brightness Boost Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',129))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        LabbControlObj = getbits(2, 0);
        SharpnessStrength = getbits(4, 4);
        LabbStrengthSetting = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        LabbGainValue = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, LabbControl(LabbControlObj), SharpnessStrength, LabbStrengthSetting, LabbGainValue

def WriteCaicImageProcessingControl(CaicGainDisplayScale,  CaicGainDisplayEnable,  CaicMaxLumensGain,  CaicClippingThreshold):
    "Controls the CAIC functionality for the projection module."
    global Summary
    Summary.Command = "Write Caic Image Processing Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',132))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(CaicGainDisplayScale.value, 1, 6)
        value = setbits(int(CaicGainDisplayEnable), 1, 7)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('B',int(convertfloattofixed(CaicMaxLumensGain,31)))))
        writebytes.extend(list(struct.pack('B',int(convertfloattofixed(CaicClippingThreshold,63)))))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadCaicImageProcessingControl():
    "Reads the state of the CAIC functionality within the projection module."
    global Summary
    Summary.Command = "Read Caic Image Processing Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',133))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(3, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        CaicGainDisplayScaleObj = getbits(1, 6);
        CaicGainDisplayEnable = getbits(1, 7);
        CaicMaxLumensGain = convertfixedtofloat(struct.unpack_from ('B', bytearray(readbytes), 1)[0], 31)
        CaicClippingThreshold = convertfixedtofloat(struct.unpack_from ('B', bytearray(readbytes), 2)[0], 63)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CaicGainDisplayScale(CaicGainDisplayScaleObj), CaicGainDisplayEnable, CaicMaxLumensGain, CaicClippingThreshold

def WriteColorCoordinateAdjustmentControl(CcaEnable):
    "Controls the Color Coordinate Adjustment (CCA) image processing functionality for the projection module."
    global Summary
    Summary.Command = "Write Color Coordinate Adjustment Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',134))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',CcaEnable)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadColorCoordinateAdjustmentControl():
    "Reads the state of the Color Coordinate Adjustment (CCA) image processing within the projection module."
    global Summary
    Summary.Command = "Read Color Coordinate Adjustment Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',135))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        CcaEnable = struct.unpack_from ('?', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CcaEnable

def ReadShortStatus():
    "Provides a brief system status for the projection module."
    global Summary
    Summary.Command = "Read Short Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',208))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ShortStatus.SystemInitialized = getbits(1, 0);
        ShortStatus.CommunicationError = getbits(1, 1);
        ShortStatus.SystemError = getbits(1, 3);
        ShortStatus.FlashEraseComplete = getbits(1, 4);
        ShortStatus.FlashError = getbits(1, 5);
        ShortStatus.SensingSequenceError = getbits(1, 6);
        ShortStatus.Application = getbits(1, 7);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ShortStatus

def ReadSystemStatus():
    "Reads system status information for the projection module."
    global Summary
    Summary.Command = "Read System Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',209))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        SystemStatus.DmdDeviceError = getbits(1, 0);
        SystemStatus.DmdInterfaceError = getbits(1, 1);
        SystemStatus.DmdTrainingError = getbits(1, 2);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        packerinit(readdata)
        SystemStatus.RedLedEnableState = getbits(1, 0);
        SystemStatus.GreenLedEnableState = getbits(1, 1);
        SystemStatus.BlueLedEnableState = getbits(1, 2);
        SystemStatus.RedLedError = getbits(1, 3);
        SystemStatus.GreenLedError = getbits(1, 4);
        SystemStatus.BlueLedError = getbits(1, 5);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        SystemStatus.SequenceAbortError = getbits(1, 0);
        SystemStatus.SequenceError = getbits(1, 1);
        SystemStatus.DcPowerSupply = getbits(1, 2);
        SystemStatus.SensingError = getbits(5, 3);
        readdata = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        packerinit(readdata)
        SystemStatus.ControllerConfiguration = getbits(1, 2);
        SystemStatus.MasterOrSlaveOperation = getbits(1, 3);
        SystemStatus.ProductConfigurationError = getbits(1, 4);
        SystemStatus.WatchdogTimerTimeout = getbits(1, 5);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, SystemStatus

def ReadCommunicationStatus():
    "Reads I2C communication status information for the projection module."
    global Summary
    Summary.Command = "Read Communication Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',211))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0x02]
        writebytes.extend(valueArray)
        readbytes = _readcommand(2, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        CommunicationStatus.InvalidCommandError = getbits(1, 0);
        CommunicationStatus.InvalidCommandParameterValue = getbits(1, 1);
        CommunicationStatus.CommandProcessingError = getbits(1, 2);
        CommunicationStatus.FlashBatchFileError = getbits(1, 3);
        CommunicationStatus.ReadCommandError = getbits(1, 4);
        CommunicationStatus.InvalidNumberOfCommandParameters = getbits(1, 5);
        CommunicationStatus.BusTimeoutByDisplayError = getbits(1, 6);
        CommunicationStatus.AbortedOpCode = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, CommunicationStatus

def ReadSystemSoftwareVersion():
    "Reads the Arm software version (main application) information for the projection module. This application is part of the firmware image."
    global Summary
    Summary.Command = "Read System Software Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',210))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PatchVersion = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        MinorVersion = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        MajorVersion = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PatchVersion, MinorVersion, MajorVersion

def ReadControllerDeviceId():
    "Reads the controller device ID for the projection module."
    global Summary
    Summary.Command = "Read Controller Device Id"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',212))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        DeviceIdObj = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ControllerDeviceId(DeviceIdObj)

def ReadDmdDeviceId(DmdDataSelection):
    "Reads the DMD device ID or DMD fuse data for the projection module."
    global Summary
    Summary.Command = "Read Dmd Device Id"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',213))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',DmdDataSelection.value)))
        readbytes = _readcommand(4, writebytes, ProtocolData)
        DeviceId = struct.unpack_from ('I', bytearray(readbytes), 0)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, DeviceId

def ReadFirmwareBuildVersion():
    "Reads the controller firmware version for the projection module."
    global Summary
    Summary.Command = "Read Firmware Build Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',217))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PatchVersion = struct.unpack_from ('H', bytearray(readbytes), 0)[0]
        MinorVersion = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        MajorVersion = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PatchVersion, MinorVersion, MajorVersion

def ReadSystemTemperature():
    "Reads the System Temperature."
    global Summary
    Summary.Command = "Read System Temperature"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',214))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(2, writebytes, ProtocolData)
        Temperature = convertfixedtofloat(struct.unpack_from ('H', bytearray(readbytes), 0)[0], 10)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Temperature

def ReadFlashUpdatePrecheck(FlashUpdatePackageSize):
    "Verifies that a pending flash update (write) is appropriate for the specified block of the projection module flash. Must have called Write Flash Data Type Select prior."
    global Summary
    Summary.Command = "Read Flash Update Precheck"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',221))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('I',FlashUpdatePackageSize)))
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        PackageSizeStatusObj = getbits(1, 0);
        PacakgeConfigurationCollapsedObj = getbits(1, 1);
        PacakgeConfigurationIdentifierObj = getbits(1, 2);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Error(PackageSizeStatusObj), Error(PacakgeConfigurationCollapsedObj), Error(PacakgeConfigurationIdentifierObj)

def WriteFlashDataTypeSelect(FlashSelect):
    "Selects the data block that will be written/read from the flash."
    global Summary
    Summary.Command = "Write Flash Data Type Select"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',222))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',FlashSelect.value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteFlashDataLength(FlashDataLength):
    "Specifies the length in bytes of data that will be written/read from the flash."
    global Summary
    Summary.Command = "Write Flash Data Length"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',223))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('H',FlashDataLength)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteFlashErase():
    "Erases the selected flash data."
    global Summary
    Summary.Command = "Write Flash Erase"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',224))
        ProtocolData.OpcodeLength = 1;
        valueArray = [0xAA, 0xBB, 0xCC, 0xDD]
        writebytes.extend(valueArray)
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def WriteFlashStart(Data):
    "Writes data to the flash."
    global Summary
    Summary.Command = "Write Flash Start"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',225))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(Data))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFlashStart(Length):
    "Reads data from the flash."
    global Summary
    Summary.Command = "Read Flash Start"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',227))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(Length, writebytes, ProtocolData)
        Data = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def WriteFlashContinue(Data):
    "Writes data to the flash."
    global Summary
    Summary.Command = "Write Flash Continue"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',226))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(Data))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadFlashContinue(Length):
    "Reads data from the flash."
    global Summary
    Summary.Command = "Read Flash Continue"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',228))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(Length, writebytes, ProtocolData)
        Data = bytearray(readbytes)[0, 1]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, Data

def ReadSequenceBinaryVersion():
    "Reads the Light Control Sequence Binary version."
    global Summary
    Summary.Command = "Read Sequence Binary Version"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',155))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(4, writebytes, ProtocolData)
        PatchVersion = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        MinorVersion = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        MajorVersion = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PatchVersion, MinorVersion, MajorVersion

def WriteInternalPatternControl(PatternControl,  RepeatCount):
    "Specifies the control for the Internal Pattern."
    global Summary
    Summary.Command = "Write Internal Pattern Control"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',158))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PatternControl.value)))
        writebytes.extend(list(struct.pack('B',RepeatCount)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadValidateExposureTime(PatternMode,  BitDepth,  ExposureTime):
    "Checks the sequence database for support of the exposure time."
    global Summary
    Summary.Command = "Read Validate Exposure Time"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',157))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PatternMode.value)))
        writebytes.extend(list(struct.pack('B',BitDepth.value)))
        writebytes.extend(list(struct.pack('I',ExposureTime)))
        readbytes = _readcommand(13, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        ExposureTimeSupportedObj = getbits(1, 0);
        ZeroDarkTimeSupportedObj = getbits(1, 4);
        MinimumExposureTime = struct.unpack_from ('I', bytearray(readbytes), 1)[0]
        PreExposureDarkTime = struct.unpack_from ('I', bytearray(readbytes), 5)[0]
        PostExposureDarkTime = struct.unpack_from ('I', bytearray(readbytes), 9)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, ExposureTimeSupported(ExposureTimeSupportedObj), ZeroDarkTimeSupported(ZeroDarkTimeSupportedObj), MinimumExposureTime, PreExposureDarkTime, PostExposureDarkTime

def WriteTriggerInConfiguration(TriggerEnable,  TriggerPolarity):
    "Specifies the configuration for Trigger In."
    global Summary
    Summary.Command = "Write Trigger In Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',144))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(TriggerEnable.value, 1, 0)
        value = setbits(TriggerPolarity.value, 1, 1)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTriggerInConfiguration():
    "Reads the configuration for Trigger In."
    global Summary
    Summary.Command = "Read Trigger In Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',145))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        TriggerEnableObj = getbits(1, 0);
        TriggerPolarityObj = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TriggerEnable(TriggerEnableObj), TriggerPolarity(TriggerPolarityObj)

def WriteTriggerOutConfiguration(TriggerType,  TriggerEnable,  TriggerInversion,  Delay):
    "Specifies the configuration for Trigger Out1 or Trigger Out2."
    global Summary
    Summary.Command = "Write Trigger Out Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',146))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(TriggerType.value, 1, 0)
        value = setbits(TriggerEnable.value, 1, 1)
        value = setbits(TriggerInversion.value, 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('i',Delay)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadTriggerOutConfiguration(Trigger):
    "Reads the configuration for Trigger Out1 or Trigger Out2."
    global Summary
    Summary.Command = "Read Trigger Out Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',147))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',Trigger.value)))
        readbytes = _readcommand(5, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        TriggerEnableObj = getbits(1, 0);
        TriggerInversionObj = getbits(1, 1);
        Delay = struct.unpack_from ('i', bytearray(readbytes), 1)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TriggerEnable(TriggerEnableObj), TriggerInversion(TriggerInversionObj), Delay

def WritePatternReadyConfiguration(TriggerEnable,  TriggerPolarity):
    "Specifies the configuration for the Pattern Ready output signal."
    global Summary
    Summary.Command = "Write Pattern Ready Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',148))
        ProtocolData.OpcodeLength = 1;
        packerinit()
        value = setbits(TriggerEnable.value, 1, 0)
        value = setbits(TriggerPolarity.value, 1, 1)
        writebytes.extend(list(struct.pack('B',value)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPatternReadyConfiguration():
    "Reads the configuration for Pattern Ready output signal."
    global Summary
    Summary.Command = "Read Pattern Ready Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',149))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(1, writebytes, ProtocolData)
        readdata = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        packerinit(readdata)
        TriggerEnableObj = getbits(1, 0);
        TriggerPolarityObj = getbits(1, 1);
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, TriggerEnable(TriggerEnableObj), TriggerPolarity(TriggerPolarityObj)

def WritePatternConfiguration(PatternConfiguration):
    "Specifies the configuration for external and internal patterns."
    global Summary
    Summary.Command = "Write Pattern Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',150))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PatternConfiguration.SequenceType.value)))
        writebytes.extend(list(struct.pack('B',PatternConfiguration.NumberOfPatterns)))
        packerinit()
        value = setbits(PatternConfiguration.RedIlluminator.value, 1, 0)
        value = setbits(PatternConfiguration.GreenIlluminator.value, 1, 1)
        value = setbits(PatternConfiguration.BlueIlluminator.value, 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('I',PatternConfiguration.IlluminationTime)))
        writebytes.extend(list(struct.pack('I',PatternConfiguration.PreIlluminationDarkTime)))
        writebytes.extend(list(struct.pack('I',PatternConfiguration.PostIlluminationDarkTime)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPatternConfiguration():
    "Reads the configuration for external and internal patterns."
    global Summary
    Summary.Command = "Read Pattern Configuration"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',151))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(15, writebytes, ProtocolData)
        PatternConfiguration.SequenceType = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        PatternConfiguration.NumberOfPatterns = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        PatternConfiguration.RedIlluminator = getbits(1, 0);
        PatternConfiguration.GreenIlluminator = getbits(1, 1);
        PatternConfiguration.BlueIlluminator = getbits(1, 2);
        PatternConfiguration.IlluminationTime = struct.unpack_from ('I', bytearray(readbytes), 3)[0]
        PatternConfiguration.PreIlluminationDarkTime = struct.unpack_from ('I', bytearray(readbytes), 7)[0]
        PatternConfiguration.PostIlluminationDarkTime = struct.unpack_from ('I', bytearray(readbytes), 11)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PatternConfiguration

def WritePatternOrderTableEntry(WriteControl,  PatternOrderTableEntry):
    "Specifies the configuration for the Pattern Order Table."
    global Summary
    Summary.Command = "Write Pattern Order Table Entry"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',152))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',WriteControl.value)))
        writebytes.extend(list(struct.pack('B',PatternOrderTableEntry.PatSetIndex)))
        writebytes.extend(list(struct.pack('B',PatternOrderTableEntry.NumberOfPatternsToDisplay)))
        packerinit()
        value = setbits(PatternOrderTableEntry.RedIlluminator.value, 1, 0)
        value = setbits(PatternOrderTableEntry.GreenIlluminator.value, 1, 1)
        value = setbits(PatternOrderTableEntry.BlueIlluminator.value, 1, 2)
        writebytes.extend(list(struct.pack('B',value)))
        writebytes.extend(list(struct.pack('I',PatternOrderTableEntry.PatternInvertLsword)))
        writebytes.extend(list(struct.pack('I',PatternOrderTableEntry.PatternInvertMsword)))
        writebytes.extend(list(struct.pack('I',PatternOrderTableEntry.IlluminationTime)))
        writebytes.extend(list(struct.pack('I',PatternOrderTableEntry.PreIlluminationDarkTime)))
        writebytes.extend(list(struct.pack('I',PatternOrderTableEntry.PostIlluminationDarkTime)))
        _writecommand(writebytes, ProtocolData)
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful == False
    finally:
        return Summary

def ReadPatternOrderTableEntry(PatternOrderTableEntryIndex):
    "Reads the configuration for the Pattern Order Table."
    global Summary
    Summary.Command = "Read Pattern Order Table Entry"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',153))
        ProtocolData.OpcodeLength = 1;
        writebytes.extend(list(struct.pack('B',PatternOrderTableEntryIndex)))
        readbytes = _readcommand(23, writebytes, ProtocolData)
        PatternOrderTableEntry.PatSetIndex = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        PatternOrderTableEntry.NumberOfPatternsToDisplay = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        readdata = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        packerinit(readdata)
        PatternOrderTableEntry.RedIlluminator = getbits(1, 0);
        PatternOrderTableEntry.GreenIlluminator = getbits(1, 1);
        PatternOrderTableEntry.BlueIlluminator = getbits(1, 2);
        PatternOrderTableEntry.PatternInvertLsword = struct.unpack_from ('I', bytearray(readbytes), 3)[0]
        PatternOrderTableEntry.PatternInvertMsword = struct.unpack_from ('I', bytearray(readbytes), 7)[0]
        PatternOrderTableEntry.IlluminationTime = struct.unpack_from ('I', bytearray(readbytes), 11)[0]
        PatternOrderTableEntry.PreIlluminationDarkTime = struct.unpack_from ('I', bytearray(readbytes), 15)[0]
        PatternOrderTableEntry.PostIlluminationDarkTime = struct.unpack_from ('I', bytearray(readbytes), 19)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, PatternOrderTableEntry

def ReadInternalPatternStatus():
    "Reads the Status of the Internal Pattern Streaming."
    global Summary
    Summary.Command = "Read Internal Pattern Status"
    Summary.Successful = True
    global ProtocolData
    ProtocolData.CommandDestination = 0;
    try:
        writebytes=list(struct.pack('B',159))
        ProtocolData.OpcodeLength = 1;
        readbytes = _readcommand(7, writebytes, ProtocolData)
        InternalPatternStatus.PatternReadyStatus = struct.unpack_from ('B', bytearray(readbytes), 0)[0]
        InternalPatternStatus.NumPatOrderTableEntries = struct.unpack_from ('B', bytearray(readbytes), 1)[0]
        InternalPatternStatus.CurrentPatOrderEntryIndex = struct.unpack_from ('B', bytearray(readbytes), 2)[0]
        InternalPatternStatus.CurrentPatSetIndex = struct.unpack_from ('B', bytearray(readbytes), 3)[0]
        InternalPatternStatus.NumPatInCurrentPatSet = struct.unpack_from ('B', bytearray(readbytes), 4)[0]
        InternalPatternStatus.NumPatDisplayedFromPatSet = struct.unpack_from ('B', bytearray(readbytes), 5)[0]
        InternalPatternStatus.NextPatSetIndex = struct.unpack_from ('B', bytearray(readbytes), 6)[0]
    except ValueError as ve:
        print("Exception Occurred ", ve)
        Summary.Successful = False
    finally:
        return Summary, InternalPatternStatus

