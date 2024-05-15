import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import ServiceTestData
from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажимем на кнопку "Заказать" на главной странице')
    def click_main_order_button(self):
        main_button = self.wait_and_find_element(OrderLocators.MAIN_ORDER_BUTTON)
        main_button.click()

    @allure.step('Вводим в поле "Имя" имя заказчика')
    def set_name_input(self):
        name_input = self.wait_and_find_element(OrderLocators.NAME_FILED)
        name_input.send_keys(*ServiceTestData.AUTH_NAME)

    @allure.step('Вводим в поле "Фамилия" фамилию заказчика')
    def set_last_name_input(self):
        last_name_input = self.wait_and_find_element(OrderLocators.LAST_NAME_FILED)
        last_name_input.send_keys(*ServiceTestData.AUTH_LAST_NAME)

    @allure.step('Вводим в поле "Адрес" адрес доставки')
    def set_address_input(self):
        address_input = self.wait_and_find_element(OrderLocators.ADDRESS_FILED)
        address_input.send_keys(*ServiceTestData.AUTH_ADDRESS)

    @allure.step('Нажимаем на поле "Станция метро" и выбираем необходимую станцию')
    def click_metro_station_filed(self):
        metro_station_filed = self.wait_and_find_element(OrderLocators.METRO_STATION_FILED)
        metro_station_filed.click()
        station = self.wait_and_find_element(OrderLocators.METRO_STATION)
        station.click()

    @allure.step('Вводим в поле "Телефон" номер телефона')
    def set_telephone_input(self):
        telephone_input = self.wait_and_find_element(OrderLocators.TELEPHONE_FILED)
        telephone_input.send_keys(*ServiceTestData.AUTH_PHONE)

    @allure.step('Нажимаем на кнопку далее')
    def click_further_button(self):
        further_button = self.wait_and_find_element(OrderLocators.FURTHER_BUTTON)
        further_button.click()

    @allure.step('Нажимаем на поле "Когда привезти заказ" и выбираем дату')
    def click_date_filled(self):
        date_filed = self.wait_and_find_element(OrderLocators.DATE_FILED)
        date_filed.click()
        date = self.wait_and_find_element(OrderLocators.DATE)
        date.click()

    @allure.step('Нажимаем на поле "Срок аренды" и выбираем срок')
    def click_rental_period_filed(self):
        rental_period_filed = self.wait_and_find_element(OrderLocators.RENTAL_PERIOD_FILED)
        rental_period_filed.click()
        rental_period = self.wait_and_find_element(OrderLocators.RENTAL_PERIOD)
        rental_period.click()

    @allure.step('Нажимем на кнопку "Заказать"')
    def click_order_button(self):
        order_button = self.wait_and_find_element(OrderLocators.ORDER_BUTTON)
        order_button.click()

    @allure.step('Во всплывшем окне нажимаем на кнопку "Да"')
    def click_yes_button_in_window(self):
        yes_button = self.wait_and_find_element(OrderLocators.YES_BUTTON)
        yes_button.click()

    @allure.step('Проверяем отображение всплывшего окна')
    def check_pop_up_window(self):
        pop_up_window = self.wait_and_find_element(OrderLocators.POP_UP_WINDOW)
        return pop_up_window.is_displayed()

    @allure.step('Нажимаем на кнопку статуса заказа')
    def click_button_order_status(self):
        button_order_status = self.wait_and_find_element(OrderLocators.SEE_STATUS)
        button_order_status.click()

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_on_yandex_logo(self):
        yandex_logo = self.wait_and_find_element(OrderLocators.YANDEX_LOGO)
        yandex_logo.click()

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_on_scooter_logo(self):
        scooter_logo = self.wait_and_find_element(OrderLocators.SCOOTER_LOGO)
        scooter_logo.click()

    @allure.step('Переключаемся на страницу Дзена')
    def check_yandex_widow(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ждем загрузки страницы')
    def wait_loading_page(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(OrderLocators.YANDEX_BUTTON))

    def login_to_scooter_form(self):
        self.set_name_input()
        self.set_last_name_input()
        self.set_address_input()
        self.click_metro_station_filed()
        self.set_telephone_input()
        self.click_further_button()
        self.click_date_filled()
        self.click_rental_period_filed()
        self.click_order_button()

    def placing_an_order(self):
        self.click_yes_button_in_window()
        self.click_button_order_status()
