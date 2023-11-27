import time

import requests
from selene import query
from selenium import webdriver
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""НАСТРАИВАЕМ ОПЦИИ ДЛЯ ЗАГРУЗКИ"""
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "/Users/aliya/PycharmProjects/Qa_guru_9.7/tmp", # - ОПРЕДЕЛЯЕМ ПУТЬ СКАЧИВАНИЯ
    "download.prompt_for_download": False # - УБИРАЕМ ВСПЛЫВАЮЩИЕ ОКНА СКАЧИВАНИЯ
}
options.add_experimental_option("prefs", prefs) # ДОБАВЛЯЕМ ОПЦИЮ КАК ЭКСПЕРИМЕНТАЛЬНУЮ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver


"""ОТКРЫВАЕМ САЙТ И СКАЧИВАЕМ ФАЙЛ"""
# browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
# s('[data-testid=download-raw-button]').click()
# time.sleep(5)

"""ВТОРОЙ ВАРИАНТ СКАЧИВАНИЯ"""
browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
download_url = s('[data-testid=raw-button]').get(query.attribute("href")) # - НАХОДИМ ССЫЛКУ НА САЙТЕ И ПОМЕЩАЕМ В ПЕРЕМЕННУЮ
content =  requests.get(url=download_url).content # - ПОЛУЧАЕМ КОНТЕНТ ПО API
with open('tmp/readme2.rst', 'wb') as file: # - СОЗДАЕМ ФАЙЛ В ПАПКЕ
    file.write(content) # - ЗАПИСЫВАЕМ КОНТЕНТ В ФАЙЛ

with open("tmp/readme2.rst") as file: # - ОТКРЫВАЕМ ФАЙЛ
    file_content_str = file.read() # - ЗАПИСЫВАЕМ В ПЕРЕМЕННУЮ ЧТЕНИЕ ФАЙЛА
    assert "test_answer" in file_content_str # - ПРОВЕРЯЕМ ЧТО В ФАЙЛЕ ЕСТЬ ПОЛЯ