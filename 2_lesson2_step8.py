from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    #Открыть страницу
    browser.get(link)

    #Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("sobaka")
    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    myfile = browser.find_element_by_css_selector("input[type='file']")
    myfile.send_keys(file_path)
    #Нажать на кнопку "Submit"
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
