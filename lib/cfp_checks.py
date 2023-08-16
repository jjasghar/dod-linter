import logging
from datetime import datetime


class CFPChecks():
    '''
    This is the "CFP" checks, the goal of this file is to verify cfp specific
    things. There should be both ERRORS and WARNS.
    '''

    def __init__(self, error_list, yaml_file, file, warn_list):
        self.error_list = error_list
        self.yaml_file = yaml_file
        self.file = file
        self.warn_list = warn_list

    def check_cfp_start(self):
        if 'cfp_date_start' in self.yaml_file.keys():
            logging.debug(f'---> cfp_date_start is found in {self.file} <---')

            if self.yaml_file['cfp_date_start'] == "":
                logging.debug(f'---> cfp_date_start is blank in {self.file} <---')
                self.warn_list.append(f"[CFP-001] ---> {self.file} has cfp_date_start blank <--- ")
            else:
                fmt = ["%Y-%m-%d", '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%dT%H:%M:%S%z']
                fmt_errors = 0
                for i in fmt:
                    try:
                        self.check_cfp_start_object = datetime.strptime(str(self.yaml_file['cfp_date_start']), i)
                    except ValueError:
                        fmt_errors += 1

                if fmt_errors == len(fmt):
                    self.error_list.append(f"[CFP-002] ---> {self.file} the date format cfp_date_start is not explicit: example: '2023-05-06 23:59:59-03:00'")
                    logging.debug(f"[CFP-002] ---> {self.file} the date format cfp_date_start is not explicit: example: '2023-05-06 23:59:59-03:00'")
                else:
                    logging.debug(f"---> {self.file} date format cfp_date_start is expected")
        else:
            self.error_list.append(f"[CFP-003] ---> {self.file} is missing the cfp_date_startkey <---")
            logging.debug(f'[CFP-003] ---> cfp_date_start is missing in {self.file} <---')
        return

    def check_cfp_end(self):
        if 'cfp_date_end' in self.yaml_file.keys():
            logging.debug(f'---> cfp_date_end is found in {self.file} <--')

            if self.yaml_file['cfp_date_end'] == "":
                logging.debug(f'[CFP-001] ---> cfp_date_end is blank in {self.file} <---')
                self.warn_list.append(f"[CFP-001] ---> {self.file} has cfp_date_end blank <--- ")
            else:
                fmt = ["%Y-%m-%d", '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%dT%H:%M:%S%z']
                fmt_errors = 0
                for i in fmt:
                    try:
                        self.check_cfp_start_object = datetime.strptime(str(self.yaml_file['cfp_date_end']), i)
                    except ValueError:
                        fmt_errors += 1

                if fmt_errors == len(fmt):
                    self.error_list.append(f"[CFP-002] ---> {self.file} the date format cfp_date_end is not explicit: example: '2023-05-06 23:59:59-03:00'")
                    logging.debug(f"[CFP-002] ---> {self.file} the date format cfp_date_end is not explicit: example: '2023-05-06 23:59:59-03:00'")
                else:
                    logging.debug(f"---> {self.file} date format cfp_date_end is expected")
        else:
            self.error_list.append(f"[CFP-005] ---> {self.file} is missing the cfp_date_endkey <---")
            logging.debug(f'[CFP-005] ---> cfp_date_end is missing in {self.file} <--')
        return

    def check_cfp_link(self):
        if 'cfp_link' in self.yaml_file.keys():
            logging.debug(f'---> cfp_link is found in {self.file} <---')
            if self.yaml_file['cfp_link'] == "":
                logging.debug(f'[CFP-001] ---> cfp_link is blank in {self.file} <---')
                self.warn_list.append(f"[CFP-001] ---> {self.file} has cfp_link blank <---")
        return

    def check_cfp_open(self):
        if 'cfp_open' in self.yaml_file.keys():
            logging.debug(f'---> cfp_open in {self.file} <---')
            if self.yaml_file['cfp_open'] == "":
                logging.debug(f'[CFP-001] ---> cfp_open is blank in {self.file} <---')
                self.warn_list.append(f"[CFP-001] ---> {self.file} has cfp_open blank <---")
        else:
            self.error_list.append(f"[CFP-006] ---> {self.file} is missing the cfp_open <---")
            logging.debug(f'[CFP-006] ---> cfp_open is missing in {self.file} <---')
        return

    def check_cfp_announce(self):
        if 'cfp_date_announce' in self.yaml_file.keys():
            logging.debug(f'---> cfp_date_announce is found in {self.file} <---')

            if self.yaml_file['cfp_date_announce'] == "":
                logging.debug(f'[CFP-001] ---> cfp_date_announce is blank in {self.file} <---')
                self.warn_list.append(f"[CFP-001] ---> {self.file} has cfp_date_announce blank <--- ")
            else:
                fmt = ["%Y-%m-%d", '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%dT%H:%M:%S%z']
                fmt_errors = 0
                for i in fmt:
                    try:
                        self.check_cfp_start_object = datetime.strptime(str(self.yaml_file['cfp_date_announce']), i)
                    except ValueError:
                        fmt_errors += 1

                if fmt_errors == len(fmt):
                    self.error_list.append(f"[CFP-002] ---> {self.file} the date format cfp_date_announce is not explicit: example: '2023-05-06 23:59:59-03:00'")
                    logging.debug(f"[CFP-002] ---> {self.file} the date format cfp_date_announce is not explicit: example: '2023-05-06 23:59:59-03:00'")
                else:
                    logging.debug(f"---> {self.file} date format cfp_date_announce is expected")
        else:
            self.error_list.append(f"[CFP-006] ---> {self.file} is missing the cfp_date_announce <---")
            logging.debug(f'[CFP-006] ---> cfp_date_announce is missing in {self.file} <--')
        return
