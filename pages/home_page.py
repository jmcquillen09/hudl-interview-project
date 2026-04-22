from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    _USER_DISPLAY_NAME = (By.CSS_SELECTOR, ".hui-globaluseritem__display-name span")
    _USER_MENU_TRIGGER = (By.CSS_SELECTOR, ".hui-globaluseritem__display-name")
    _USER_EMAIL = (By.CSS_SELECTOR, ".hui-globaluseritem__email")

    def get_display_name(self):
        return self.get_text(self._USER_DISPLAY_NAME)

    def open_user_menu(self):
        self.click(self._USER_MENU_TRIGGER)

    def get_user_email(self):
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.visibility_of_element_located(self._USER_EMAIL))
        return self.get_text(self._USER_EMAIL)
