all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

deps-dev:
	pip install -r requirements_dev.txt

deps:
	pip install -r requirements.txt

run: venv
	python seclopz-bot.py

test: venv
	SECLOPZBOT=../settings.cfg venv/bin/python -m unittest discover -s .

sdist: venv test
	venv/bin/python setup.py sdist

