import bs4
import selenium
import time
import pyautogui

from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from login import login
from question_parse import parse_question, answer_question

option = webdriver.ChromeOptions()

option.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driver = webdriver.Chrome(executable_path=r'C:\Users\raksh\Downloads\chromedriver.exe', options=option)
driver.get("https://classroom.mcpsmd.org/")

login('155879@mcpsmd.net', 'mousekeyboard101')

while True:

    driver.get("https://mcpsmd.instructure.com/courses/546815/quizzes/959094?module_item_id=15868023")

    time.sleep(2)
    pyautogui.click(768, 433)

    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    qs = soup.find_all("div", {"class": "question_text user_content enhanced"})
    strqs = []

    for q in qs:
        q = str(q)
        start = q.index("<p>")
        end = q.index("</p>")

        strq = str(q[start+3:end])

        strq = strq.replace("<em>", "")
        strq = strq.replace("</em>", "")
        strq = strq.strip()

        strq = " ".join(strq.split())

        strqs.append(strq)

    try:
        q1_type = parse_question(strqs[0])
        q2_type = parse_question(strqs[1])
    except IndexError:
        qs = soup.find_all("div", {"class": "question_text user_content enhanced"})
        strqs = []

        for q in qs:
            q = str(q)
            start = q.index("<p>")
            end = q.index("</p>")

            strq = str(q[start+3:end])

            strq = strq.replace("<em>", "")
            strq = strq.replace("</em>", "")
            strq = strq.strip()

            strq = " ".join(strq.split())

            strqs.append(strq)
        
        q1_type = parse_question(strqs[0])
        q2_type = parse_question(strqs[1])


    q1_ans = answer_question(strqs[0], q1_type)
    q2_ans = answer_question(strqs[1], q2_type)

    time.sleep(1)

    answer_box_coor = pyautogui.locateCenterOnScreen('answer_box.png')
    pyautogui.click(answer_box_coor)

    time.sleep(1)
    pyautogui.typewrite(str(q1_ans))


    time.sleep(1)
    for _ in range(2):
        pyautogui.keyDown('tab')
        time.sleep(0.75)

    time.sleep(0.25)

    pyautogui.typewrite(str(q2_ans))

    pyautogui.scroll(-500)

    time.sleep(1)

    sub_box_coor = pyautogui.locateCenterOnScreen('quiz_submit.png')
    pyautogui.click(sub_box_coor)

    time.sleep(2)

#xpath prob 1: /html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/form[1]/div[1]/div[2]/div[2]/div[5]/div[2]
#xpath prob 2: /html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/form[1]/div[1]/div[3]/div[2]/div[5]/div[2]


#link to cfu: https://mcpsmd.instructure.com/courses/546815/quizzes/959094?module_item_id=15868023
#google sign in button coor: (910, 730)
