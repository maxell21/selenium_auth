# selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# self imports
from settings import chromedriver_path, url, email, password
import time

# Создаем сервис для Chrome
service = Service(executable_path=chromedriver_path)

# Инициализируем драйвер Chrome
driver = webdriver.Chrome(service=service)

try:
    # Открываем веб-страницу
    driver.get(url)
    # находим поле ввода email по его атрибуту id
    email_input = driver.find_element(By.ID, "")
    # вставляем email в поле
    time.sleep(5)
    email_input.send_keys(email)

    # находим кнопку "далее" по её id
    next_button = driver.find_element(By.ID, "")
    time.sleep(2)
    next_button.click()
 
    # ожидание для имитации действий пользователя
    wait = WebDriverWait(driver, 10)
    # Находим поле ввода пароля и вставляем данные
    password_input = wait.until(EC.presence_of_element_located((By.ID, "")))
    time.sleep(5)
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.ID, "")
    time.sleep(2)
    login_button.click()
    
    time.sleep(10)



finally:
    # Закрываем браузер
    driver.quit()