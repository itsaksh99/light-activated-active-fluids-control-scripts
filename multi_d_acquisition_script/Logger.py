import os
import datetime
import csv

class Logger():
    def __init__(self, root_folder):
        self.root = root_folder  # the main data folder
        self.daily_folder = self.create_base_folder(self.root) # returns the name of data folder for each day (creates a new folder if it doesnt exist)      
        self.experiment = None
        self.create_new_exp() 

    # create a new experiment folder and logfile
    def create_new_exp(self):
        self.new_log = True

        experiment_number = 1
        while os.path.exists(os.path.join(self.daily_folder, f"experiment_{experiment_number}")):
            experiment_number += 1
        experiment_folder = os.path.join(self.daily_folder, f"experiment_{experiment_number}")
        os.makedirs(experiment_folder)

        log_filename = f"log_{self.date}_{experiment_number}.csv"
        log_path = os.path.join(experiment_folder, log_filename)

        self.experiment = {"experiment_folder": experiment_folder, 'experiment_number': experiment_number, 'experiment_logfile': log_path }

    # creates/returns a data folder for each day using the date in yyyymmdd format
    def create_base_folder(self, root_folder):
        base_date = self.date
        base_folder = os.path.join(root_folder, base_date)
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)
        return base_folder
    

    def log(self,data):
        if self.new_log:
            with open(self.logfile, mode='a', newline='') as f:
                csv.writer(f).writerow(data.keys())
                csv.writer(f).writerow(data.values())
            self.new_log = False
        else:
            with open(self.logfile, mode='a', newline='') as f:
                csv.writer(f).writerow(data.values())

    
    @property
    def date(self):
        return datetime.datetime.now().strftime("%Y%m%d")
    
    @property
    def experiment_folder(self):
        return self.experiment['experiment_folder']

    @property
    def experiment_number(self):
        return self.experiment['experiment_number']
        
    @property
    def logfile(self):
        return self.experiment['experiment_logfile']
        

