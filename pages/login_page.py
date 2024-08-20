from base.base_page import BasePage
import pages.page_elements as pe
import utilities.custom_logger as cl


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_id(self, text):
        if text == "<empty>":
            text = ""
        BasePage.input_element(self, pe.id_input_field, text)
        cl.allure_logs("아이디 입력")

    def input_password(self, text):
        if text == "<empty>":
            text = ""
        BasePage.input_element(self, pe.password_input_field, text)
        cl.allure_logs("비밀번호 입력")

    def click_login_page_button(self):
        BasePage.click_element(self, pe.login_page_button)
        cl.allure_logs("로그인 버튼 클릭")

    def check_error_message(self, error_message):
        BasePage.is_displayed(self, pe.error_message)
        cl.allure_logs("에러 메시지 표시 확인")
