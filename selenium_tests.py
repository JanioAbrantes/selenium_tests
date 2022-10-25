import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://the-internet.herokuapp.com/")

    def test_add_button(self):
        self.driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()
        delete_button = self.driver.find_element(By.CLASS_NAME, 'added-manually')
        assert delete_button.text == 'Delete'

    def test_delete_button(self):
        self.driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()
        delete_button = self.driver.find_element(By.CLASS_NAME, 'added-manually')
        assert delete_button.text == 'Delete'

        delete_button.click()

    def test_check_the_checkbox(self):
        self.driver.find_element(By.LINK_TEXT, 'Checkboxes').click()
        check_button = self.driver.find_element(By.TAG_NAME, 'input')
        check_button.click()

        assert check_button.is_selected() == True

    def test_uncheck_the_checkbox(self):
        self.driver.find_element(By.LINK_TEXT, 'Checkboxes').click()
        check_button = self.driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')
        check_button.click()

        assert check_button.is_selected() == False

    def test_dropdown_choose_option_1(self):
        self.driver.find_element(By.LINK_TEXT, 'Dropdown').click()
        select = Select(self.driver.find_element(By.ID, 'dropdown'))
        select.select_by_visible_text('Option 1')
        selected_option = self.driver.find_element(By.CSS_SELECTOR, '#dropdown > option:nth-child(2)')
        assert selected_option.text == 'Option 1'

    def test_dropdown_choose_option_2(self):
        self.driver.find_element(By.LINK_TEXT, 'Dropdown').click()
        select = Select(self.driver.find_element(By.ID, 'dropdown'))
        select.select_by_visible_text('Option 2')
        selected_option = self.driver.find_element(By.CSS_SELECTOR, '#dropdown > option:nth-child(3)')
        assert selected_option.text == 'Option 2'

    def test_insert_the_right_username_and_password(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(By.NAME, 'username').send_keys('tomsmith')
        self.driver.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(By.CLASS_NAME, 'radius').click()

        message = self.driver.find_element(By.ID, 'flash')

        assert message.text == 'You logged into a secure area!\n×'

    def test_insert_the_right_username_and_wrong_password(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(By.NAME, 'username').send_keys('tomsmith')
        self.driver.find_element(By.NAME, 'password').send_keys('a!')
        self.driver.find_element(By.CLASS_NAME, 'radius').click()

        message = self.driver.find_element(By.ID, 'flash')

        assert message.text == 'Your password is invalid!\n×'

    def test_insert_the_wrong_username_and_right_password(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(By.NAME, 'username').send_keys('a')
        self.driver.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(By.CLASS_NAME, 'radius').click()

        message = self.driver.find_element(By.ID, 'flash')

        assert message.text == 'Your username is invalid!\n×'

    def test_logout(self):
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.find_element(By.NAME, 'username').send_keys('tomsmith')
        self.driver.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(By.CLASS_NAME, 'radius').click()
        self.driver.find_element(By.CLASS_NAME, 'radius').click()

        message = self.driver.find_element(By.ID, 'flash')

        assert message.text == 'You logged out of the secure area!\n×'

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
