from selenium.webdriver.common.by import By


class ElementosPagina:
    # Para Test de inicio de sesion
    BOTON_LOGIN = (By.XPATH, '//*[@id="btnLogIn"]')
    CAMPO_EMAIL = (By.XPATH, '//*[@id="emailId"]')
    CAMPO_CONTRASENA = (By.XPATH, '//*[@id="password"]')

    # Para Test de registro
    CAMPO_EMAIL_REGISTRO = (By.XPATH, '//*[@id="email"]')
    CAMPO_PASSWORD_REGISTRO = (By.XPATH, '//*[@id="pw"]')
    CAMPO_VERIFY_PASSWORD_REGISTRO = (By.XPATH, '//*[@id="retype_pw"]')
    CAMPO_USERNAME_REGISTRO = (By.XPATH, '//*[@id="nickname"]')
    BOTON_REGISTRO = (By.XPATH, '//*[@id="content"]/div/div[1]/div/a')

    # Para Test de Idioma
    BOTON_LISTA = (By.XPATH, '//*[@id="languageArea"]/a')
    BOTON_ENGLISH = (By.XPATH,'//*[@id="languageArea"]/ul/li[1]/a')
    BOTON_FRENCH = (By.XPATH, '//*[@id="languageArea"]/ul/li[6]/a')


    # Para Test de busqueda
    BOTON_BUSQUEDA = (By.XPATH, '//*[@id="header"]/div/div[1]/a[3]')
    CAMPO_BUSQUEDA = (By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/span[1]/input')

    # Para Test de agregado
    BOTON_SEGUIR = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[2]/ul/li[4]/a')







