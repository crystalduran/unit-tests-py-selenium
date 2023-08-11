import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from data import ElementosPagina
# pytest pages/test_pagina.py --html=results/reporte_registro.html


@pytest.fixture
def firefox_driver():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
    firefox_driver_path = os.path.join('..', 'drivers', 'geckodriver.exe')

    options = FirefoxOptions()
    options.add_argument(f'--user-agent={user_agent}')
    # options.add_argument("--headless")

    firefox_service = FirefoxService(executable_path=firefox_driver_path)
    firefox_driver = webdriver.Firefox(service=firefox_service, options=options)

    yield firefox_driver
    firefox_driver.quit()


def test_iniciar_sesion_failed(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/login?returnUrl=/')
    elementos = ElementosPagina()

    time.sleep(4)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL)
    campo_email.click()
    campo_email.send_keys('12@outlook.es')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_CONTRASENA)
    campo_contrasena.send_keys('lokop')
    time.sleep(2)

    boton_login = firefox_driver.find_element(*elementos.BOTON_LOGIN)
    boton_login.click()

    firefox_driver.save_screenshot('results/screenshot_failed_login.png')


def test_iniciar_sesion_success(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/login?returnUrl=/')
    elementos = ElementosPagina()

    time.sleep(4)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL)
    campo_email.click()
    campo_email.send_keys('12@outlook.es')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_CONTRASENA)
    campo_contrasena.send_keys('password')
    time.sleep(2)

    boton_login = firefox_driver.find_element(*elementos.BOTON_LOGIN)
    boton_login.click()

    time.sleep(10)
    firefox_driver.save_screenshot('results/screenshot_success_login.png')
