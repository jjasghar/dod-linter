# dod-linter

## Scope

This ~~app~~ linter goes through our hugo instance, and finds the open event yamls
and looks suggests possible fixes or missed configurations. This is so we can
have some expected standardizations for the yamls.


## Usage


1. Have a `venv` python environment working
```bash
git clone git@github.com:jjasghar/dod-linter.git
cd dod-linter/
python3 -m venv venv && source venv/bin/activate
```

2. Set up the `dod_path` in the `config.toml`, this is where you have the `devopsdays-web`
repository checked out.
Note:
```
# Do NOT put the ~ in this (home needs to be expanded by python)
# This should be relitive to your home directory
```

3. Example Run the main script
```bash
python main.py -a # for all
python main.py -f 2023-austin.yml # for a specific one
```

4. Check the other options via:
```bash
python main.py -h
```

## Checks

### CFP

| Code | Reason | Error/Warning |
| ---- | ---- | ---- |
| [CFP-001] |  The key is blank | WARNING |
| [CFP-002] |  Date format is not explicit, or expected | ERROR |
| [CFP-003] |  "cfp_date_start_key" is missing | ERROR |
| [CFP-004] |  "cfp_date_endkey" is missing | ERROR |
| [CFP-005] |  "cfp_open" is missing | ERROR |
| [CFP-006] |  "cfp_data_annouce" is missing | ERROR |

### NAME

| Code | Reason | Error/Warning |
| ---- | ---- | ---- |
| [NAM-001] | 'name' is missing | ERROR |
| [NAM-002] | 'year' is missing | ERROR |
| [NAM-003] | 'city' is missing | ERROR |
| [NAM-004] | 'description' is missing | ERROR |
| [NAM-005] | 'startdate' is missing | ERROR |
| [NAM-006] | 'enddate' is missing | ERROR |

### ORG

| Code | Reason | Error/Warning |
| ---- | ---- | ---- |
| [ORG-001] |  'organizer_email' is missing | ERROR |
| [ORG-002] |  'sponsors_accepted' is blank | WARNING |

### REG

| Code | Reason | Error/Warning |
| ---- | ---- | ---- |
| [REG-001] |  The key is blank | WARNING |
| [REG-002] |  Date format is not explicit, or expected | ERROR |
| [REG-003] |  'registration_closed' is missing | ERROR |
| [REG-004] |  'registration_start' is missing | ERROR |
| [REG-005] |  'registration_date_end' is missing | ERROR |


## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2023- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[web]: https://github.com/devopsdays/devopsdays-web/

