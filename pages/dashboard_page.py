from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-name")

    def is_loaded(self):
        return self.user_dropdown
