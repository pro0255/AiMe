VENV = env

# Saves the current environment to requirements.txt
save:
	pip freeze > requirements.txt

virtualenv:
	python3 -m venv $(VENV)

activate:
	source $(VENV)/bin/activate

install:
	pip install -r requirements.txt

run-server: virtualenv activate install
	uvicorn api:app --reload

run-server-debug: virtualenv activate install
	uvicorn api:app --reload

