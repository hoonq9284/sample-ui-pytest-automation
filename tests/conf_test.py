from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.weather_page import WeatherPage
import config.config as config
import pytest


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()

    if config.REMOTE_RUN:
        options.set_capability("browserName", "chrome")
        try:
            driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL, options=options)
        except Exception as error:
            pytest.fail(f"Remote WebDriver 초기화 실패: {error}")
    else:
        try:
            driver = webdriver.Chrome(service=service, options=options)
        except WebDriverException:
            pytest.fail("WebDriverException 발생: WebDriver를 초기화하지 못했습니다.")

    driver.get(config.BASE_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def page_objects(driver):
    try:
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        weather_page = WeatherPage(driver)
        return {
            "main_page": main_page,
            "login_page": login_page,
            "weather_page": weather_page,
        }
    except Exception as e:
        pytest.fail(f"페이지 객체 초기화 실패: {e}")


@pytest.fixture(scope="function")
def initialize_environment(page_objects):
    main_page = page_objects["main_page"]
    login_page = page_objects["login_page"]
    weather_page = page_objects["weather_page"]
    return page_objects
