VENV = env

# Saves the current environment to requirements.txt
save:
	pip freeze > requirements.txt

env:
	python3 -m venv $(VENV)

activate: $(VENV)/bin/activate
	. $(VENV)/bin/activate

install:
	pip install -r requirements.txt

run-server: env activate install
	uvicorn api:app --reload

run-server-debug: env activate install
	uvicorn api:app --reload

clean:
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete


format:
	black src/*
	isort src/*
