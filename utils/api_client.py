import requests

class OrangeHRMApiClient:
    def __init__(self):
        self.base_url = "https://opensource-demo.orangehrmlive.com"
        self.login_path = "/web/index.php/auth/login"

    def get_base_page(self):
        return requests.get(self.base_url)

    def get_login_page(self):
        return requests.get(f"{self.base_url}{self.login_path}")
