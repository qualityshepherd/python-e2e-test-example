import pytest
from requests import get
from qs_page import QsPage


@pytest.fixture(scope="module", autouse=True)
def setup(driver):
  global qsPage
  qsPage = QsPage(driver)

def test_qualityshepherd_site_returns_status_200(driver):
  res = get(qsPage.get_base_url())

  assert res.status_code == 200

def test_non_existant_page_returns_404(driver):
  res = get(qsPage.get_base_url() + '/this_page_no_exits.php')

  assert res.status_code == 404