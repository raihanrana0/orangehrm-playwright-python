from utils.api_client import OrangeHRMApiClient

def test_login_page_api_status():
    api = OrangeHRMApiClient()
    response = api.get_login_page()

    assert response.status_code == 200
    assert "OrangeHRM" in response.text
