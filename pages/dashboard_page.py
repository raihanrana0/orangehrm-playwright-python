from playwright.sync_api import Page

class DashboardPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def __init__(self, page: Page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-name")

    def open(self):
        self.page.goto(self.URL)

    def is_loaded(self):
        return self.user_dropdown