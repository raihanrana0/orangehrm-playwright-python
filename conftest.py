from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def auth_state(tmp_path_factory, browser):
    state_path = Path(tmp_path_factory.mktemp("auth")) / "state.json"

    if not state_path.exists():
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        login.open()
        login.login("Admin", "admin123")
        page.wait_for_url("**/dashboard/*")
        context.storage_state(path=state_path)
        context.close()

    return state_path

@pytest.fixture
def auth_context(browser, auth_state):
    context = browser.new_context(storage_state=auth_state)
    yield context
    context.close()

@pytest.fixture
def auth_page(auth_context):
    page = auth_context.new_page()
    yield page