from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_with_empty_fields(page: Page):
    login = LoginPage(page)

    login.open()
    login.login("", "")

    expect(login.required_messages).to_have_count(2)
    expect(login.required_messages.first).to_have_text("Required")

def test_login_with_wrong_credentials(page: Page):
    login = LoginPage(page)

    login.open()
    login.login("Admin", "wrongPassword")

    expect(login.invalid_credentials_message).to_be_visible(timeout=10000)
    expect(login.invalid_credentials_message).to_have_text("Invalid credentials")