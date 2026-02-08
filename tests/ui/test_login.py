import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_with_valid_credentials(page):
    login = LoginPage(page)
    login.open()
    login.login("Admin", "admin123")

    page.wait_for_url("**/dashboard/*")
    assert "/dashboard" in page.url

@pytest.mark.parametrize(
    ("username", "password", "error_count"),
    [
        ("", "", 2),
        ("Admin", "", 1),
        ("", "admin123", 1),
    ],
)
def test_login_with_empty_fields(page, username, password, error_count):
    login = LoginPage(page)
    login.open()
    login.login(username, password)

    expect(login.required_error).to_have_count(error_count)

@pytest.mark.parametrize(
    ("username", "password"),
    [
        ("Admin", "wrongPassword"),
        ("wrongUser", "admin123"),
        ("wrongUser", "wrongPassword"),
    ],
)
def test_login_with_wrong_credentials(page, username, password):
    login = LoginPage(page)

    login.open()
    login.login(username, password)

    expect(login.invalid_credentials_message).to_be_visible(timeout=10000)
    expect(login.invalid_credentials_message).to_have_text("Invalid credentials")