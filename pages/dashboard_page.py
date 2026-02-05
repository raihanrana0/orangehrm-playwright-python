from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_header = page.locator("h6.oxd-topbar-header-breadcrumb-module")

    def verify_dashboard_loaded(self):
        expect(self.dashboard_header).to_be_visible(timeout=10000)
        expect(self.dashboard_header).to_have_text("Dashboard")
