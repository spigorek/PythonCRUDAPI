# Makefile for running tests with pytest

users_regression:
	pytest -v --capture=sys --tb=long src/users/ -m "regression" --html=reports/report.html --junitxml=report.xml --self-contained-html

users_smoke:
	pytest -v --capture=no --tb=long src/users/ -m "smoke"

update_users:
	pytest -v --capture=no --tb=long src/users/test_update.py
