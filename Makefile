SHELL=C:/Windows/System32/cmd.exe
ENV = env
PYBIN = $(ENV)/scripts
PYTHON = $(PYBIN)/python
PIP = $(PYBIN)/pip
PYTEST = $(PYTHON) -m pytest
COVERAGE = $(PYTHON) -m coverage
PYFLAKE8 = $(PYTHON) -m flake8
TESTDIR = tests
APPMAIN = tamaku.py
SMALL_DATA_FILE = ./data/small_data.data
LARGE_DATA_FILE = ./data/large_data.zip
RESULTS_FOLDER = .\results
MKDIR = mkdir
PROD_RESULTS = $(RESULTS_FOLDER)/results.txt
TMP_DIR = ./tmp
COVERAGE_TARGETS = --cov=data_processor --cov=solver --cov=support

environ: clean requirements-dev.txt
	virtualenv $(ENV)
	$(PIP) install -r requirements-dev.txt
	@echo "initialization complete"

.PHONY: help
help:
	@echo "make             # create virtual env and setup dependencies"
	@echo "make tests       # run tests"
	@echo "make coverage    # run tests with coverage report"
	@echo "make run_small   # run solver against small file"
	@echo "make run_large   # run solver against LARGE file"
	@echo "make run_prod    # run solver against LARGE file and produce result file"
	@echo "make lint        # check linting"
	@echo "make flake8      # alias for `make lint`"

.PHONY: run_small
run_small:
	@$(PYTHON) $(APPMAIN) -i $(SMALL_DATA_FILE)

.PHONY: run_large
run_large:
	@$(PYTHON) $(APPMAIN) -t $(TMP_DIR)  -i $(LARGE_DATA_FILE) -v -l 10000

.PHONY: run_prod
run_prod:
	@if not exist $(RESULTS_FOLDER) $(MKDIR) $(RESULTS_FOLDER)
	@$(PYTHON) $(APPMAIN) -t $(TMP_DIR) -i $(LARGE_DATA_FILE) -w -o $(PROD_RESULTS)

.PHONY: tests
tests:
	$(PYTEST) $(TESTDIR) -vv

.PHONY: coverage
coverage:
	$(PYTEST) $(TESTDIR) -vv $(COVERAGE_TARGETS)
	$(COVERAGE) html

.PHONY: lint
lint:
	$(PYFLAKE8)
	
.PHONY: flake8
flake8:
	$(PYFLAKE8)

.PHONY: clean
clean:
	if exist $(ENV) rd $(ENV) /q /s
	if exist .coverage del .coverage
	if exist htmlcov rd htmlcov /q /s	
	if exist __pycache__ rd __pycache__ /q /s		
	if exist $(PROD_RESULTS) rd $(PROD_RESULTS) /q /s			
	if exist $(TMP_DIR) rd $(TMP_DIR) /q /s		
	del /S *.pyc
	
