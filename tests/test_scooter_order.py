import allure
from data import Urls
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Проверка появления всплывающего окна с сообщением об успешном создании заказа.')
    @allure.description('Заполняем форму заказа и нажимаем на заказ, проверяем, что всплывающее окно появилось.')
    def test_pop_up_window_appeared(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.Scooter)
        order_page.click_on_cookie_button()
        order_page.click_main_order_button()
        order_page.login_to_scooter_form()
        assert order_page.check_pop_up_window(), 'Pop-window does not exist'

    @allure.title('Проверка успешного оформления заказа.')
    def test_scooter_success_order_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.Scooter)
        order_page.click_on_cookie_button()
        order_page.click_main_order_button()
        order_page.login_to_scooter_form()
        order_page.placing_an_order()
        assert 'track' in order_page.get_current_url()

    @allure.title('Проверям, что при нажатии на логотип «Яндекс», откроется главная страница Дзена.')
    def test_click_on_yandex_logo_transition_completed(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.Scooter)
        order_page.click_main_order_button()
        order_page.click_on_yandex_logo()
        order_page.check_yandex_widow()
        order_page.wait_loading_page()
        assert 'dzen.ru/?yredirect=true' in order_page.get_current_url()

    @allure.title('Проверяем, что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_click_on_scooter_logo_transition_completed(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.Scooter)
        order_page.click_main_order_button()
        order_page.click_on_scooter_logo()
        assert order_page.get_current_url() == Urls.Scooter
