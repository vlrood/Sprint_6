import allure
import pytest
from data import Urls, TextQuestions
from locators.main_page_locators import MainLocators
from pages.main_page import ListQuestion


class TestListQuestions:

    @pytest.mark.parametrize('question, answer, text_answer', [
        (MainLocators.FIRST_QUESTION, MainLocators.FIRST_ANSWER, TextQuestions.FIRST_TEXT),
        (MainLocators.SECOND_QUESTION, MainLocators.SECOND_ANSWER, TextQuestions.SECOND_TEXT),
        (MainLocators.THIRD_QUESTION, MainLocators.THIRD_ANSWER, TextQuestions.THIRD_TEXT),
        (MainLocators.FOURTH_QUESTION, MainLocators.FOURTH_ANSWER, TextQuestions.FOURTH_TEXT),
        (MainLocators.FIFTH_QUESTION, MainLocators.FIFTH_ANSWER, TextQuestions.FIFTH_TEXT),
        (MainLocators.SIXTH_QUESTION, MainLocators.SIXTH_ANSWER, TextQuestions.SIXTH_TEXT),
        (MainLocators.SEVENTH_QUESTION, MainLocators.SEVENTH_ANSWER, TextQuestions.SEVEN_TEXT),
        (MainLocators.EIGHT_QUESTION, MainLocators.EIGHT_ANSWER, TextQuestions.EIGHT_TEXT)
    ])
    @allure.title('Проверка соответствия текста ответа тексту вопроса')
    @allure.description('Нажимаем на вопрос и проверяем текст ответа')
    def test_question_answer_text_answer_ratio_must_match(self, driver, question, answer, text_answer):
        main_page = ListQuestion(driver)
        main_page.open_page(Urls.Scooter)
        main_page.scroll_to_the_questions()
        main_page.click_questions(question)
        assert main_page.get_text_of_answer(answer) == text_answer
