import pytest
import allure


@allure.title("[WeatherPage] 테스트 진행을 위해 백그라운드 케이스 실행")
@pytest.fixture(scope="function")
def setup_weather_page(page_objects):
    main_page = page_objects["main_page"]
    weather_page = page_objects["weather_page"]
    main_page.click_weather_link_text()
    main_page.check_weather_logo()
    return weather_page


class TestWeatherPage:
    @allure.title("[WeatherPage] 테스트 환경 초기화")
    @pytest.fixture(autouse=True)
    def setup(self, setup_weather_page):
        self.weather_page = setup_weather_page

    @allure.title("네이버 날씨 - 홈 탭 표시 확인하기")
    def test_weather_home_tap_displayed(self):
        self.weather_page.check_weather_home_tap()

    @allure.title("네이버 날씨 - 예보비교 탭 표시 확인하기")
    def test_weather_compare_tap_displayed(self):
        self.weather_page.check_weather_compare_tap()

    @allure.title("네이버 날씨 - 미세먼지 탭 표시 확인하기")
    def test_weather_air_tap_displayed(self):
        self.weather_page.check_weather_air_tap()

    @allure.title("네이버 날씨 - 지도 탭 표시 확인하기")
    def test_weather_map_tap_displayed(self):
        self.weather_page.check_weather_map_tap()
