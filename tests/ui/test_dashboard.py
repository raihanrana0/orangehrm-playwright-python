from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage


def test_dashboard_visible_after_login(auth_page):
    dashboard = DashboardPage(auth_page)

    dashboard.open()

    expect(dashboard.is_loaded()).to_be_visible()