import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_size():
    browser.config.window_height = 1080
    browser.config.window_width = 680
    print("Изменение размера окна браузера!")

    yield
    browser.quit()
    print("Закрываем браузер!")
