# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 02:24:10 2020

@author: Vinicius
"""

## finding element by path ( matricula e senha)

def loginInQAcademico(browser, matricula, senha):
    txtloginXPath = "//input[@id='txtLogin']"
    txtsenhaXPath = "//input[@id='txtSenha']"
    btnOkXPath = "//input[@id='btnOk']"

    browser.find_element_by_xpath(txtloginXPath).send_keys(matricula)
    browser.find_element_by_xpath(txtsenhaXPath).send_keys(senha)
    browser.find_element_by_xpath(btnOkXPath).submit()

# searching grades and printing
#def getGrades(browser):
#    elements = browser.find_elements_by_class_name("conteudoTexto")
#    for element in elements:
#       print(element.text)
    


def getGrades(driver):
    elementsCourse = driver.find_elements_by_tag_name('strong')
    elementsAllContent = driver.find_elements_by_class_name('conteudoTexto')
    grades = []
    enablerList = False
    enabler = False
    selector = 0

    for e_course in elementsCourse:
        for e_all in elementsAllContent:
            if(e_all.text.count('-')==3):
                if(e_course.text == e_all.text):
                    str_txt = e_all.text
                    begin = str_txt.find( '-',str_txt.find( '-' )+1 )+2
                    end = str_txt.find('-', begin)-1
                    grades.append([str_txt[begin:end]])
                    enablerList = True
                else:
                    enablerList = False
            else:
                if(enablerList):
                    if(e_all.text[:2] == 'N1'):
                        selector = 1
                        enabler = True
                    elif(e_all.text[:2] == 'N2'):
                        selector = 2
                        enabler = True
                    elif(enabler):
                        if(selector==1):
                            idx = e_all.text.find('Nota:')
                            if(idx==-1):
                                enabler = False
                            else:
                                grades[len(grades)-1].append('N1: ' + e_all.text[idx:idx+10])
                        elif(selector==2):
                            idx = e_all.text.find('Nota:')
                            if(idx==-1):
                                enabler = False
                            else:
                                grades[len(grades)-1].append('N2: ' + e_all.text[idx:idx+10])

    gradesStr = '___NOTAS___\n'
    for grade in grades:
        for i in grade:
            if(i==grade[0]):
                gradesStr += i + ':\n'
            else:
                gradesStr+= '     ' + i + '\n'

    return gradesStr

