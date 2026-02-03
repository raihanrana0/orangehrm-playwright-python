from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import re

def test_valid_login(page: Page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open()
    login.login("Admin", "admin123")

    dashboard.verify_dashboard_loaded()
    #expect(page).to_have_url_containing("/dashboard")
    expect(page).to_have_url(re.compile(".*/dashboard.*"))
