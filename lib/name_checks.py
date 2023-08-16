import logging

class NameChecks():
    '''
    This is the "NAM" checks, the goal of this file is to verify the default names
    and other important checks. Everything should ERROR/exit 1 here.
    '''

    def __init__(self, error_list, yaml_file, file):
        self.error_list = error_list
        self.yaml_file = yaml_file
        self.file = file

    def check_name(self):
        if 'name' in self.yaml_file.keys():
            logging.debug(f'---> name was found in {self.file} <---')
        else:
            self.error_list.append(f"[NAM-001] ---> {self.file} is missing 'name' <--- ")
            logging.debug(f"[NAM-001] ---> {self.file} is missing 'name' <--- ")
        return

    def check_year(self):
        if 'year' in self.yaml_file.keys():
            logging.debug(f'---> year was found in {self.file} <---')
        else:
            self.error_list.append(f"[NAM-002] ---> {self.file} is missing 'year' <--- ")
            logging.debug(f"[NAM-002] ---> {self.file} is missing 'year' <--- ")
        return

    def check_city(self):
        if 'city' in self.yaml_file.keys():
            logging.debug(f'---> city was found in {self.file} <---')
        else:
            self.error_list.append(f"[NAM-003] ---> {self.file} is missing 'city' <--- ")
            logging.debug(f"[NAM-003] ---> {self.file} is missing 'city' <--- ")
        return

    def check_description(self):
        if 'description' in self.yaml_file.keys():
            logging.debug(f'---> description was found in {self.file} <---')
        else:
            self.error_list.append(f"[NAM-004] ---> {self.file} is missing 'description' <--- ")
            logging.debug(f"[NAM-004] ---> {self.file} is missing 'description' <--- ")
        return

    def check_startdate(self):
        if 'startdate' in self.yaml_file.keys():
            logging.debug(f'---> startdate was found in {self.file} <---')
        else:
            self.error_list.append(f"[NAM-005] ---> {self.file} is missing 'startdate' <--- ")
            logging.debug(f"[NAM-005] ---> {self.file} is missing 'startdate' <--- ")
        return

    def check_enddate(self):
        if 'enddate' in self.yaml_file.keys():
            logging.debug(f'---> enddate was found in {self.file} <---')
        else:
            self.error_list.append(f"[NAM-006] ---> {self.file} is missing 'enddate' <--- ")
            logging.debug(f"[NAM-006] ---> {self.file} is missing 'enddate' <--- ")
        return
