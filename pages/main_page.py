import allure
from locators.main_page_locators import MainLocators
from pages.base_page import BasePage


class ListQuestion(BasePage):
    @allure.step('Прокручиваем страницу до текста "Вопросы о важном"')
    def scroll_to_the_questions(self):
        element = self.wait_and_find_element(MainLocators.IMPORTANT_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимем на вопрос')
    def click_questions(self, question):
        questions = self.wait_and_find_element(question)
        questions.click()

    @allure.step('Получаем текст вопроса')
    def get_text_of_answer(self, answer):
        answers = self.wait_and_find_element(answer)
        return answers.text
