from selenium.webdriver.common.by import By
from time import sleep

class TestItem:
    def test_guest_should_see_login_link(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"), 'Button not found!'
        sleep(3)
