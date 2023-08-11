import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from data import ElementosPagina
# pytest pages/test_pagina_registro.py --html=results/reporte_registro.html


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


def test_registro_failed_email(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/join?loginType=EMAIL')
    elementos = ElementosPagina()

    time.sleep(4)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL_REGISTRO)
    campo_email.send_keys('12@outlook.es')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_PASSWORD_REGISTRO)
    campo_contrasena.send_keys('lkjh1234!')

    campo_contrasena_verify = firefox_driver.find_element(*elementos.CAMPO_VERIFY_PASSWORD_REGISTRO)
    campo_contrasena_verify.send_keys('lkjh1234!')

    campo_username = firefox_driver.find_element(*elementos.CAMPO_USERNAME_REGISTRO)
    campo_username.send_keys('kikimorie')

    time.sleep(2)
    boton_registro = firefox_driver.find_element(*elementos.BOTON_REGISTRO)
    boton_registro.click()
    time.sleep(3)

    firefox_driver.save_screenshot('results/screenshot_email_signup.png')


def test_registro_failed_empty(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/join?loginType=EMAIL')
    elementos = ElementosPagina()

    time.sleep(4)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL_REGISTRO)
    campo_email.send_keys('12@outlook.es')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_PASSWORD_REGISTRO)
    campo_contrasena.send_keys('lkjh1234!')

    campo_contrasena_verify = firefox_driver.find_element(*elementos.CAMPO_VERIFY_PASSWORD_REGISTRO)
    campo_contrasena_verify.send_keys('lkjh1234!')

    time.sleep(2)
    boton_registro = firefox_driver.find_element(*elementos.BOTON_REGISTRO)
    boton_registro.click()

    time.sleep(2)

    firefox_driver.save_screenshot('results/screenshot_empty_signup.png')


def test_registro_success(firefox_driver):
    firefox_driver.get('https://www.webtoons.com/member/join?loginType=EMAIL')
    elementos = ElementosPagina()

    time.sleep(4)
    campo_email = firefox_driver.find_element(*elementos.CAMPO_EMAIL_REGISTRO)
    campo_email.send_keys('n@gmail.com')

    campo_contrasena = firefox_driver.find_element(*elementos.CAMPO_PASSWORD_REGISTRO)
    campo_contrasena.send_keys('password')

    campo_contrasena_verify = firefox_driver.find_element(*elementos.CAMPO_VERIFY_PASSWORD_REGISTRO)
    campo_contrasena_verify.send_keys('password')

    campo_username = firefox_driver.find_element(*elementos.CAMPO_USERNAME_REGISTRO)
    campo_username.send_keys('nickname')

    time.sleep(2)
    boton_registro = firefox_driver.find_element(*elementos.BOTON_REGISTRO)
    boton_registro.click()
    time.sleep(4)

    firefox_driver.save_screenshot('results/screenshot_success_signup.png')
