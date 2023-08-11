import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from data import ElementosPagina
# pytest pages/test_add.py --html=results/reporte_seguir.html


@pytest.fixture
def firefox_driver():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
    firefox_driver_path = os.path.join('..', 'drivers', 'geckodriver.exe')

    options = FirefoxOptions()
    options.add_argument(f'--user-agent={user_agent}')

    firefox_service = FirefoxService(executable_path=firefox_driver_path)
    firefox_driver = webdriver.Firefox(service=firefox_service, options=options)

    yield firefox_driver
    firefox_driver.quit()


def test_add_webtoon(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/login?returnUrl=/')
    elementos = ElementosPagina()

    time.sleep(5)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL)
    campo_email.click()
    campo_email.send_keys('12@outlook.es')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_CONTRASENA)
    campo_contrasena.send_keys('password')
    time.sleep(2)

    boton_login = firefox_driver.find_element(*elementos.BOTON_LOGIN)
    boton_login.click()
    time.sleep(5)

    firefox_driver.get('https://www.webtoons.com/es/action/eleceed/list?title_no=2642')
    time.sleep(2)
    firefox_driver.save_screenshot('results/screenshot_added_before.png')
    time.sleep(2)

    boton_seguir = firefox_driver.find_element(*elementos.BOTON_SEGUIR)
    boton_seguir.click()
    time.sleep(3)
    firefox_driver.save_screenshot('results/screenshot_added_after.png')


def test_deleted_webtoon(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/login?returnUrl=/')
    elementos = ElementosPagina()

    time.sleep(5)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL)
    campo_email.click()
    campo_email.send_keys('12@outlook.es')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_CONTRASENA)
    campo_contrasena.send_keys('password')
    time.sleep(2)

    boton_login = firefox_driver.find_element(*elementos.BOTON_LOGIN)
    boton_login.click()
    time.sleep(5)

    firefox_driver.get('https://www.webtoons.com/es/action/king-of-the-east/list?title_no=4683')
    time.sleep(2)
    firefox_driver.save_screenshot('results/screenshot_deleted_before.png')

    boton_seguir = firefox_driver.find_element(*elementos.BOTON_SEGUIR)
    boton_seguir.click()
    time.sleep(3)
    firefox_driver.save_screenshot('results/screenshot_deleted_after.png')

