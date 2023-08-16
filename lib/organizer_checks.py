import logging


class OrganizerChecks():
    '''
    This is the "ORG" checks, the goal of this file is to verify cfp specific
    things. There should be ERRORs mainly here.
    '''

    def __init__(self, error_list, yaml_file, file, warn_list):
        self.error_list = error_list
        self.yaml_file = yaml_file
        self.file = file
        self.warn_list = warn_list

    def check_organizer_email(self):
        if 'organizer_email' in self.yaml_file.keys():
            logging.debug(f'---> organizer_email was found in {self.file} <---')
            if self.yaml_file['organizer_email'] == "":
                logging.debug(f'---> organizer_email was found in {self.file} but blank <---')
        else:
            self.error_list.append(f"[ORG-001] ---> {self.file} is missing 'organizer_email' <--- ")
            logging.debug(f"[ORG-001] ---> {self.file} is missing 'organizer_email' <--- ")
        return

    def check_sponsors_accepted(self):
        if 'sponsors_accepted' in self.yaml_file.keys():
            if self.yaml_file['sponsors_accepted'] in ["false", "no", "true", "yes", "Yes"]:
                logging.debug(f'---> sponsors_accepted is not blank in {self.file} <---')
            else:
                self.warning_details.append(f"[ORG-002] ---> {self.file} has sponsors_accepted blank <--- ")
                logging.debug(f"[ORG-002] ---> {self.file} has sponsors_accepted blank <--- ")
        return
