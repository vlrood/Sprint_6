from selenium.webdriver.common.by import By


class OrderLocators:
    MAIN_ORDER_BUTTON = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')
    YANDEX_LOGO = (By.XPATH, '//a[@href="//yandex.ru"]')
    YANDEX_BUTTON = (By.XPATH, '//div[text()="Новости"]')
    SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    NAME_FILED = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_FILED = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FILED = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_FILED = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION = (By.XPATH, '//button[@tabindex = "-1"]')
    TELEPHONE_FILED = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    FURTHER_BUTTON = (By.XPATH, '//button[text() = "Далее"]')
    DATE_FILED = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATE = (By.XPATH, '//div[@class="react-datepicker__month-container"]//div[text() = "22"]')
    RENTAL_PERIOD_FILED = (By.XPATH, '//div[@class="Dropdown-root"]')
    RENTAL_PERIOD = (By.XPATH, '//div[@class= "Dropdown-menu"]/div[text()="сутки"]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    POP_UP_WINDOW = (By.XPATH, '//div[@class="Order_Form__17u6u"]')
    YES_BUTTON = (By.XPATH, '//button[text()= "Да"]')
    SEE_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')
