from selenium.webdriver.common.by import By
from pages.base_page import BasePage

LOGIN_URL = "https://www.hudl.com/login"


class LoginPage(BasePage):
    _USERNAME = (By.ID, "username")
    _CONTINUE_BTN = (By.CSS_SELECTOR, "[data-action-button-primary='true']")
    _PASSWORD = (By.ID, "password")
    _ERROR = (By.CSS_SELECTOR, "[class*='error'], [id*='error']")
    _LOGO = (By.ID, "prompt-logo-center")
    _HEADING = (By.XPATH, "//h1[text()='Log In']")
    _GOOGLE_BTN = (By.CSS_SELECTOR, "[data-provider='google']")
    _FACEBOOK_BTN = (By.CSS_SELECTOR, "[data-provider='facebook']")
    _APPLE_BTN = (By.CSS_SELECTOR, "[data-provider='apple']")
    _CREATE_ACCOUNT = (By.LINK_TEXT, "Create Account")
    _PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")
    _TERMS_OF_SERVICE = (By.LINK_TEXT, "Terms of Service")

    def open(self):
        super().open(LOGIN_URL)

    def wait_until_logged_in(self):
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.any_of(
            EC.url_contains("hudl.com/home"),
            EC.url_contains("app.hudl.com"),
        ))

    def login(self, username, password):
        self.type(self._USERNAME, username)
        self.click(self._CONTINUE_BTN)
        self.type(self._PASSWORD, password)
        self.click(self._CONTINUE_BTN)

    def submit_username(self, username):
        self.type(self._USERNAME, username)
        self.click(self._CONTINUE_BTN)

    def is_error_displayed(self):
        return self.is_visible(self._ERROR)

    def error_message(self):
        return self.get_text(self._ERROR)
