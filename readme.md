[ ![Codeship Status for qualityshepherd/python-e2e-test-example](https://app.codeship.com/projects/46773060-bb86-0136-d63d-1e1992c1cf6f/status?branch=master)](https://app.codeship.com/projects/312669)

# Python E2E Test Example
Example Selenium/Webdriver e2e tests (some quite silly) that aim to illustrate solutions for common issues when writing e2e tests

### These Tests:
* run python selenium e2e tests against an existing website
* make use of a page object pattern
* use [pytest](http://pytest.org/) for most of the heavy lifting
* run on Firefox or Chrome
* run tests in parallel (via [pytest-parallel](https://pypi.org/project/pytest-parallel/) (requires python3.6+)
* run api tests using [requests](http://docs.python-requests.org/en/master/)
* run on merge on [CI](https://app.codeship.com/projects/312669)

## Requirements
So... while python is a lovely language, it has a silly need for keeping python2.7 around. So silly. Down that road lies madness, so we are _only_ talking about `python3`. I'm using [Homebrew (aka `brew`)](https://brew.sh/) to install things but you do you... install however you like.
1. [python3](https://www.python.org/downloads/) `brew install python3`

## Install
1. install requirements: `pip install -r requirements --user`
1. if you want to run on firefox, [download geckodriver](https://github.com/mozilla/geckodriver/releases) and move to a folder on your path (eg. `/usr/local/bin`)

## Run Tests
1. in Chrome (default): `pytest`
1. in Firefox `pytest --driver firefox`
1. in parallel `pytest --workers 2`
