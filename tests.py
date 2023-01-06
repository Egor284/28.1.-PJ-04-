from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ValidData import validnumber, validpassword, validmail, validlogin, validlc, novalidnumber, novalidmail, novalidlogin,novalidlc,vname, vsname

number = validnumber
password = validpassword
novnumber = novalidnumber
mail = validmail
login = validlogin
lc = validlc
novmail = novalidmail
novlogin = novalidlogin
novlc = novalidlc
name = vname
sname =vsname

def test_TC_1(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(number)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "lk-btn")))
    Uslovie=driver_init.find_element(By.ID,"lk-btn").text

    assert Uslovie == 'Личный кабинет'
    driver_init.quit()

def test_TC_2 (driver_init):
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(novnumber)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))
    Uslovie = driver_init.find_element(By.ID, "form-error-message").text

    assert Uslovie == 'Неверный логин или пароль' or Uslovie == 'Неверно введен текст с картинки' #если вылезит капча
    driver_init.quit()

def test_TC_3(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(mail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "lk-btn")))
    Uslovie=driver_init.find_element(By.ID,"lk-btn").text

    assert Uslovie == 'Личный кабинет'
    driver_init.quit()

def test_TC_4(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(novmail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))
    Uslovie = driver_init.find_element(By.ID, "form-error-message").text

    assert Uslovie == 'Неверный логин или пароль' or Uslovie == 'Неверно введен текст с картинки'  # если вылезит капча
    driver_init.quit()

def test_TC_5(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(login)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "lk-btn")))
    Uslovie=driver_init.find_element(By.ID,"lk-btn").text

    assert Uslovie == 'Личный кабинет'
    driver_init.quit()

def test_TC_6(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(novlogin)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))
    Uslovie = driver_init.find_element(By.ID, "form-error-message").text

    assert Uslovie == 'Неверный логин или пароль' or Uslovie == 'Неверно введен текст с картинки'  # если вылезит капча
    driver_init.quit()

def test_TC_7(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(lc)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "lk-btn")))
    Uslovie=driver_init.find_element(By.ID,"lk-btn").text

    assert Uslovie == 'Личный кабинет'
    driver_init.quit()

def test_TC_8(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"username"))).send_keys(novlc)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID,"kc-login"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "form-error-message")))
    Uslovie = driver_init.find_element(By.ID, "form-error-message").text

    assert Uslovie == 'Неверный логин или пароль' or Uslovie == 'Неверно введен текст с картинки'  # если вылезит капча
    driver_init.quit()

def test_TC_9(driver_init):
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "forgot_password"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    Uslovie = driver_init.find_element(By.CLASS_NAME, "card-container__title").text

    assert Uslovie== 'Восстановление пароля'
    driver_init.quit()

def test_TC_10(driver_init):
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    Uslovie = driver_init.find_element(By.CLASS_NAME, "card-container__title").text

    assert Uslovie== 'Регистрация'
    driver_init.quit()

def test_TC_11(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(name)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(sname)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(mail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    Uslovie = driver_init.find_element(By.CLASS_NAME, "card-container__title").text

    assert Uslovie == 'Подтверждение email'
    driver_init.quit()

def test_TC_12(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(name)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(sname)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(number)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    Uslovie = driver_init.find_element(By.CLASS_NAME, "card-container__title").text

    assert Uslovie == 'Подтверждение телефона'
    driver_init.quit()

def test_TC_13(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(name)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(sname)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(mail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('Asdf')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys('Asdf')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')))
    Uslovie = driver_init.find_element(By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text

    assert Uslovie == 'Длина пароля должна быть не менее 8 символов'
    driver_init.quit()

def test_TC_14(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(name)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(sname)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(mail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('asdf12346')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys('asdf12346')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')))
    Uslovie = driver_init.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text

    assert Uslovie == 'Пароль должен содержать хотя бы одну заглавную букву'
    driver_init.quit()

def test_TC_15(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(name)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(sname)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(mail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('йцукенгшщ')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys('йцукенгшщ')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')))
    Uslovie = driver_init.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text

    assert Uslovie == 'Пароль должен содержать только латинские буквы'
    driver_init.quit()

def test_TC_16(driver_init):

    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(name)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(sname)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(mail)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.ID, "password-confirm"))).send_keys('Qwert1234')
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.NAME, "register"))).click()
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')))
    Uslovie = driver_init.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text

    assert Uslovie == 'Пароли не совпадают'
    driver_init.quit()