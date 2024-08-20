import pytest
import base64
import allure


@allure.title("[LoginPage] 테스트 진행을 위해 백그라운드 케이스 실행")
@pytest.fixture(scope="function")
def setup_login_page(page_objects):
    main_page = page_objects["main_page"]
    login_page = page_objects["login_page"]
    main_page.click_login_button()
    main_page.check_login_page_logo()
    return login_page


class TestLoginPage:
    @allure.title("[LoginPage] 테스트 환경 초기화")
    @pytest.fixture(autouse=True)
    def setup(self, setup_login_page):
        self.login_page = setup_login_page

    @allure.title("비유효한 값으로 로그인 시도한다.")
    @pytest.mark.parametrize("username, password, error_message", [
        # username, password 모두 공백으로 로그인 시도하는 케이스
        ("<empty>", base64.b64encode(b"").decode('utf-8'), "아이디를 입력해 주세요."),
        # username 는 invalid_username / password는 invalid_pw 를 b64로 decode한 데이터 삽입하여 로그인 시도하는 케이스
        ("invalid_username", base64.b64encode(b"invalid_pw").decode('utf-8'), "아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요."),
    ])
    def test_login(self, username, password, error_message):
        if username == "<empty>":
            username = ""
        self.login_page.input_id(username)
        decrypted_password = base64.b64decode(password).decode('utf-8')
        self.login_page.input_password(decrypted_password)
        self.login_page.click_login_page_button()
        self.login_page.check_error_message(error_message)
