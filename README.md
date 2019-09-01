## Install

`pipenv install`


## Run server

`pipenv run python run_server.py`

Set `--port`, `--host` or `--worker`  for change default value


## Run client

`pipenv run python run_client.py command params`

Set `--port` or `--host` for change default value


Example:

- `run_client.py -h`
- `run_client.py create_task reversed_string STRING`
- `run_client.py create_task reversed_string STRING STRING --batch`
- `run_client.py create_task transposition STRING`
- `run_client.py status_task UUID`
- `run_client.py result_task UUID`

