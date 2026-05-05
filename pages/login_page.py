from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.page.fill("#user-name", username)

    def enter_password(self, password):
        self.page.fill("#password", password)

    def click_login(self):
        self.page.click("#login-button")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()