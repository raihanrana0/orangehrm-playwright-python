import requests

class OrangeHRMApiClient:
    def __init__(self):
        self.base_url = "https://opensource-demo.orangehrmlive.com"

    def get_login_page(self):
        return requests.get(self.base_url)
