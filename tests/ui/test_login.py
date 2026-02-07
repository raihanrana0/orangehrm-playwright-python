from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_with_valid_credentials(page):
    login = LoginPage(page)
    login.open()
    login.login("Admin", "admin123")

    expect(page).to_have_url_containing("/dashboard")

def test_login_with_empty_fields(page):
    login = LoginPage(page)
    login.open()
    login.login("", "")

    expect(login.required_error).to_have_count(2)

def test_login_with_wrong_credentials(page: Page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "wrongPassword")

    expect(login.invalid_credentials_message).to_be_visible(timeout=10000)
    expect(login.invalid_credentials_message).to_have_text("Invalid credentials")
