from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard_visible_after_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open()
    login.login("Admin", "admin123")

    expect(dashboard.is_loaded()).to_be_visible()
