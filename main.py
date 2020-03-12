import webScrapping as ws
from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
path = 'C:/Users/Vinicius/Desktop/webScrapping'
browser = webdriver.Chrome(options = options)

browser.get("https://qacademico.ifce.edu.br/qacademico/index.asp?t=1001")

#first login
ws.loginInQAcademico(browser, "matricula", "senha")

# go to diary page
browser.get("https://qacademico.ifce.edu.br/qacademico/index.asp?t=2071")
notas = ws.getGrades(browser)

print(notas)
