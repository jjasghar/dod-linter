import logging
from datetime import datetime


class RegistrationChecks():
    '''
    This is the "REG" checks, the goal of this file is to verify cfp specific
    things. There should be both ERRORS and WARNS.
    '''

    def __init__(self, error_list, yaml_file, file, warn_list):
        self.error_list = error_list
        self.yaml_file = yaml_file
        self.file = file
        self.warn_list = warn_list

    def check_registration_closed(self):
        if 'registration_closed' in self.yaml_file.keys():
            logging.debug(f'---> registration_closed is found in {self.file} <---')

            if self.yaml_file['registration_closed'] == "":
                logging.debug(f'---> registration_closed is blank in {self.file} <---')
                self.warn_list.append(f"[REG-001] ---> {self.file} has registration_closed blank <--- ")
            else:
                fmt = ["%Y-%m-%d", '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%dT%H:%M:%S%z']
                fmt_errors = 0
                for i in fmt:
                    try:
                        self.check_reg_start_object = datetime.strptime(str(self.yaml_file['registration_closed']), i)
                    except ValueError:
                        fmt_errors += 1

                if fmt_errors == len(fmt):
                    self.error_list.append(f"[REG-002] ---> {self.file} the date format registration_closed is not explicit: example: '2023-05-06 23:59:59-03:00'")
                    logging.debug(f"[REG-002] ---> {self.file} the date format registration_closed is not explicit: example: '2023-05-06 23:59:59-03:00'")
                else:
                    logging.debug(f"---> {self.file} date format registration_closed is expected")
        else:
            self.error_list.append(f"[REG-003] ---> {self.file} is missing the registration_closed key <---")
            logging.debug(f'---> registration_closed is missing in {self.file} <--')
        return

    def check_registration_start(self):
        if 'registration_date_start' in self.yaml_file.keys():
            logging.debug(f'---> registration_date_start is found in {self.file} <---')

            if self.yaml_file['registration_date_start'] == "":
                logging.debug(f'[REG-001] ---> registration_date_start is blank in {self.file} <---')
                self.warn_list.append(f"[REG-001] ---> {self.file} has registration_date_start blank <--- ")
            else:
                fmt = ["%Y-%m-%d", '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%dT%H:%M:%S%z']
                fmt_errors = 0
                for i in fmt:
                    try:
                        self.check_reg_start_object = datetime.strptime(str(self.yaml_file['registration_date_start']), i)
                    except ValueError:
                        fmt_errors += 1

                if fmt_errors == len(fmt):
                    self.error_list.append(f"[REG-002] ---> {self.file} the date format registration_date_start is not explicit: example: '2023-05-06 23:59:59-03:00'")
                    logging.debug(f"[REG-002] ---> {self.file} the date format registration_date_start is not explicit: example: '2023-05-06 23:59:59-03:00'")
                else:
                    logging.debug(f"---> {self.file} date format registration_date_start is expected")
        else:
            self.error_list.append(f"[REG-004] ---> {self.file} is missing the registration_date_start key <---")
            logging.debug(f'[REG-004] ---> registration_date_start is missing in {self.file} <--')
        return

    def check_registration_end(self):
        if 'registration_date_end' in self.yaml_file.keys():
            logging.debug(f'---> registration_date_end is found in {self.file} <---')

            if self.yaml_file['registration_date_end'] == "":
                logging.debug(f'[REG-001] ---> registration_date_end is blank in {self.file} <---')
                self.warn_list.append(f"[REG-001] ---> {self.file} has registration_date_end blank <--- ")
            else:
                fmt = ["%Y-%m-%d", '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%dT%H:%M:%S%z']
                fmt_errors = 0
                for i in fmt:
                    try:
                        self.check_reg_start_object = datetime.strptime(str(self.yaml_file['registration_date_end']), i)
                    except ValueError:
                        fmt_errors += 1

                if fmt_errors == len(fmt):
                    self.error_list.append(f"[REG-002] ---> {self.file} the date format registration_date_end is not explicit: example: '2023-05-06 23:59:59-03:00'")
                    logging.debug(f"[REG-002] ---> {self.file} the date format registration_date_end is not explicit: example: '2023-05-06 23:59:59-03:00'")
                else:
                    logging.debug(f"---> {self.file} date format registration_date_end is expected")
        else:
            self.error_list.append(f"[REG-005] ---> {self.file} is missing the registration_date_end key <---")
            logging.debug(f'[REG-005] ---> registration_date_end is missing in {self.file} <--')
        return

    def check_registration_link(self):
        if 'registration_link' in self.yaml_file.keys():
            logging.debug(f'--> registration_link is found in {self.file} <--')
            if self.yaml_file['registration_link'] == "":
                logging.debug(f'[REG-001] --> registration_link is blank in {self.file} <--')
                self.warn_list.append(f"[REG-001] ---> {self.file} has registration_link blank <--- ")
        return
