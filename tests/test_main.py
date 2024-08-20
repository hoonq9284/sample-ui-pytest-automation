import pytest
import allure


@allure.title("[MainPage] 테스트 진행을 위해 백그라운드 케이스 실행")
@pytest.fixture(scope="function")
def setup_main_page(page_objects):
    return page_objects["main_page"]


class TestMainPage:
    @allure.title("[MainPage] 테스트 환경 초기화")
    @pytest.fixture(autouse=True)
    def setup(self, setup_main_page):
        self.main_page = setup_main_page

    @allure.title("네이버 검색 필드 표시 확인하기")
    def test_search_field_displayed(self):
        self.main_page.check_search_field()

    @allure.title("프로필 영역 확인하기")
    def test_account_container_displayed(self):
        self.main_page.check_account_container()

    @allure.title("로그인 정보 텍스트 확인하기")
    def test_login_info_text_displayed(self):
        self.main_page.check_login_info_text()

    @allure.title("로그인 버튼 표시 확인하기")
    def test_login_button_displayed(self):
        self.main_page.check_login_button()

    @allure.title("아이디 찾기 링크 텍스트 표시 확인하기")
    def test_find_id_text_displayed(self):
        self.main_page.check_find_id_text()

    @allure.title("비밀번호 찾기 링크 텍스트 표시 확인하기")
    def test_find_password_text_displayed(self):
        self.main_page.check_find_password_text()

    @allure.title("회원가입 링크 텍스트 표시 확인하기")
    def test_register_text_displayed(self):
        self.main_page.check_register_text()

    @allure.title("로그인 버튼 클릭하기")
    def test_click_login_button(self):
        self.main_page.click_login_button()
        self.main_page.check_login_page_logo()

    @allure.title("네이버 카페 페이지로 이동하기")
    def test_click_cafe_icon(self):
        self.main_page.click_cafe_icon()
        self.main_page.check_cafe_logo()

    @allure.title("네이버 블로그 페이지로 이동하기")
    def test_click_blog_icon(self):
        self.main_page.click_blog_icon()
        self.main_page.check_blog_logo()

    @allure.title("네이버 쇼핑 페이지로 이동하기")
    def test_click_shopping_icon(self):
        self.main_page.click_shopping_icon()
        self.main_page.check_shopping_logo()

    @allure.title("네이버 뉴스 페이지로 이동하기")
    def test_click_news_icon(self):
        self.main_page.click_news_icon()
        self.main_page.check_news_logo()

    @allure.title("네이버 주식 페이지로 이동하기")
    def test_click_stock_icon(self):
        self.main_page.click_stock_icon()
        self.main_page.check_stock_logo()

    @allure.title("네이버 부동산 페이지로 이동하기")
    def test_click_real_icon(self):
        self.main_page.click_real_icon()
        self.main_page.check_real_logo()

    @allure.title("네이버 지도 페이지로 이동하기")
    def test_click_map_icon(self):
        self.main_page.click_map_icon()
        self.main_page.check_map_logo()

    @allure.title("네이버 웹툰 페이지로 이동하기")
    def test_click_webtoon_icon(self):
        self.main_page.click_webtoon_icon()
        self.main_page.check_webtoon_logo()

    @allure.title("네이버 날씨 페이지로 이동하기")
    def test_click_weather_link_text(self):
        self.main_page.click_weather_link_text()
        self.main_page.check_weather_logo()
