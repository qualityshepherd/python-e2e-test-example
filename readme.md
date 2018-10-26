[ ![Codeship Status for qualityshepherd/python-e2e-test-example](https://app.codeship.com/projects/46773060-bb86-0136-d63d-1e1992c1cf6f/status?branch=master)](https://app.codeship.com/projects/312669)

# Python E2E Test Example
Example Selenium/Webdriver e2e tests (some quite silly) that aim to illustrate solutions for common issues when writing e2e tests

### These Tests:
* run python selenium e2e tests against an existing site
* make use of a page object pattern
* run on Firefox or Chrome
* run tests in parallel (via [pytest-parallel](https://pypi.org/project/pytest-parallel/) (requires python3.6+)

## Install
1. install pip: `sudo easy_install pip`
1. install [Pytest](https:pytest.org): `pip install -U pytest`
1. install/update selenium: `pip install -U selenium` (3.14.1)
1. download drivers and copy to your path (eg. `/usr/local/bin`)
    - https://github.com/mozilla/geckodriver/releases (v0.23.0)
    - https://sites.google.com/a/chromium.org/chromedriver/downloads (2.43)
1. instaly pytest-parallel `pip3 install pytest-parallel` (assuming you're running python3.6+)

## Run Tests
1. in Chrome (default): `pytest`
1. in Firefox `pytest --driver firefox`
1. in parallel `pytest --workers 2