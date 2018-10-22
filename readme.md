# Python E2E Test Example
Example Selenium/Webdriver e2e tests (some quite silly) that aim to illustrate solutions for common issues when writing e2e tests

## These Tests:
* run python selenium tests locally
* make use of a page object pattern

## Install
1. install pip: `sudo easy_install pip`
1. install/update selenium: `pip install -U selenium` (3.14.1)
1. download drivers and copy to /usr/local/bin
    - https://github.com/mozilla/geckodriver/releases (v0.23.0)
    - https://sites.google.com/a/chromium.org/chromedriver/downloads (2.43)

## Run Tests
Python has a ~~stupid~~ _interesting_ way of finding modules that requires you to pass your module path...
1. run 'em: `PYTHONPATH=[PATH_TO_PROJECT]/python-e2e-test-example/pages python tests/qs_test.py`

## Optional
I found [Pytest](https:pytest.org) to be a nicer test runner...
1. install Pytest: `pip install -U pytest`
1. solve the PYTHONPATH wonkiness via an ENV var: `export PYTHONPATH=[your path here]/python-e2e-test-example/pages`
1. run 'em: `pytest`