# Python E2E Test Example
Example Selenium/Webdriver e2e tests (some quite silly) that aim to illustrate solutions for common issues when writing e2e tests

## These Tests:
* run python selenium tests locally
* make use of a page object pattern
* run on Firefox or Chrome

## Install
1. install pip: `sudo easy_install pip`
1. install [Pytest](https:pytest.org): `pip install -U pytest`
1. install/update selenium: `pip install -U selenium` (3.14.1)
1. download drivers and copy to your path (eg. `/usr/local/bin`)
    - https://github.com/mozilla/geckodriver/releases (v0.23.0)
    - https://sites.google.com/a/chromium.org/chromedriver/downloads (2.43)

## Run Tests
1. in Chrome (default): `pytest`
1. in Firefox `pytest --browser firefox`