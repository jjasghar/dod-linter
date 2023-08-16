#!/usr/bin/env python

import os
import re
import yaml
import logging
from datetime import datetime
from lib.name_checks import NameChecks
from lib.registration_checks import RegistrationChecks
from lib.cfp_checks import CFPChecks
from lib.organizer_checks import OrganizerChecks
from pathlib import Path
import argparse
import tomllib

error_details = []
warning_details = []


def main(file, all_files, error_flag, warning_flag):

    with open('config.toml', 'rb') as t:
        data = tomllib.load(t)

    dod_path = data['dod']['dod_path']

    if all_files:
        files = [f for f in os.listdir(f'{Path.home()}/{dod_path}/data/events') if re.match('202[3-4]+.*\.yml', f)]
    else:
        files = []
        files.append(file)

    if debug:
        logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        output_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        logging.debug("-----------")
        logging.debug(f"----> started at {output_date}")
        logging.debug("-----------")

    for file in files:
        with open(f'{Path.home()}/{dod_path}/data/events/{file}', "r") as stream:
            try:

                yaml_file = yaml.safe_load(stream)

            except yaml.YAMLError as exc:
                print(exc)
                exit

        event_name = NameChecks(error_details, yaml_file, file)

        event_name.check_name()
        event_name.check_year()
        event_name.check_city()
        event_name.check_description()
        event_name.check_startdate()
        event_name.check_enddate()

        event_registration = RegistrationChecks(error_details, yaml_file, file, warning_details)

        event_registration.check_registration_closed()
        event_registration.check_registration_start()
        event_registration.check_registration_end()
        event_registration.check_registration_link()

        event_cfp = CFPChecks(error_details, yaml_file, file, warning_details)

        event_cfp.check_cfp_open()
        event_cfp.check_cfp_start()
        event_cfp.check_cfp_end()
        event_cfp.check_cfp_link()
        event_cfp.check_cfp_announce()

        event_organizer = OrganizerChecks(error_details, yaml_file, file, warning_details)
        event_organizer.check_organizer_email()
        event_organizer.check_sponsors_accepted()

    if error_flag:
        for err in event_name.error_list:
            print("")
            print(" ----- Errors ----- ")
            print(err)
            print(" ----- Errors ----- ")
            print("")

    if warning_flag:
        for war in event_registration.warn_list:
            print("")
            print(" ----- Warnings ----- ")
            print(war)
            print(" ----- Warnings ----- ")
            print("")

    print("")
    print(f"Total Errors: {len(event_name.error_list)}")
    print(f"Total Warnings: {len(event_registration.warn_list)}")

    if len(event_name.error_list) > 0:
        exit_code = 1

    return exit_code

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--all', action="store_true", help="Run against \
                        all the files in devopsdays-web/data/events")
    parser.add_argument('-d', '--debug', action="store_true", help="Output the \
                       debug details to debug.log")
    parser.add_argument('-e', '--errors', action="store_false", help="Suppress \
                        found errors.")
    parser.add_argument('-f', '--file', help="Run linter against one file \
                        specificly, example: 2024-nova-lima.yml")
    parser.add_argument('-w', '--warnings', action="store_true", help="Output \
                        found warnings.")

    args = parser.parse_args()

    target_file = args.file
    all_files = args.all
    debug = args.debug
    error_flag = args.errors
    warning_flag = args.warnings

    if target_file is None and all_files is False:
        raise argparse.ArgumentError(target_file, "Error: You need to give a file or -a")
        exit(1)

    exit_code = main(target_file, all_files, error_flag, warning_flag)

    if exit_code == 1:
        exit(1)
    else:
        exit(0)
