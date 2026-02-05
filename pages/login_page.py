from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.required_messages = page.locator("span.oxd-input-field-error-message")
        self.invalid_credentials_message = page.locator(".oxd-alert-content-text")


    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)

        self.login_button.click()