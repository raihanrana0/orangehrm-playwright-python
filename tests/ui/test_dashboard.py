from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_dashboard_title(page: Page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "admin123")

    expect(page.locator("h6")).to_have_text("Dashboard")
