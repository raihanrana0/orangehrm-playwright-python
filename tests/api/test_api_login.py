import pytest
from utils.api_client import OrangeHRMApiClient

@pytest.mark.parametrize(
    "fetch_method",
    [
        "get_base_page",
        "get_login_page",
    ],
)
def test_api_page_status(fetch_method):
    api = OrangeHRMApiClient()
    response = getattr(api, fetch_method)()

    assert response.status_code == 200
    assert "OrangeHRM" in response.text

def test_login_page_has_login_path():
    api = OrangeHRMApiClient()
    response = api.get_login_page()

    assert api.login_path in response.url