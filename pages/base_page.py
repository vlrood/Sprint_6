import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    cookie_button = (By.ID, 'rcc-confirm-button')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Нажимаем на кнопку принятия cookie')
    def click_on_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url
