from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

delay = 3

def login(username, password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(delay)
    driver.get("https://www.memrise.com/login/")

    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")

    username_field.clear()
    username_field.send_keys(username)

    password_field.clear()
    password_field.send_keys(password)

    password_field.submit()
    return driver

def answer_correctly(driver, input, table, cursor, question):
    input.clear()
    query = cursor.execute("select french from " + table + " where english = :question", {"question": question})
    input.send_keys(query.fetchone()[0])
    btn = driver.find_element_by_class_name("next-button")
    ActionChains(driver).move_to_element(btn).click(btn).perform()

def answer_incorrectly(driver):
    query = cursor.execute("select french from " + table + " where english = :question", {"question": question})
    answer = query.fetchone()[0]
    btn = driver.find_element_by_class_name("next-button")
    ActionChains(driver).move_to_element(btn).click(btn).perform()

    btn2 = driver.find_element_by_class_name("next-button")
    ActionChains(driver).move_to_element(btn2).click(btn2).perform()

    input = driver.find_element_by_css_selector('input.typing-type-here')
    input.clear()
    input.send_keys(answer)

def submit(driver, table, cursor, question, accuracy):
    input = None
    try:
        tmp = driver.find_element_by_css_selector('input.typing-type-here')
        input = tmp
    except:
        pass
    if input:
        if randint(0, 100) <= accuracy:
            answer_correctly(driver, input, table, cursor, question)
        else:
            answer_incorrectly(driver)
    else:
        query = cursor.execute("select french from " + table + " where english = :question", {"question": question})
        results = query.fetchall()
        if not len(results):
            query = cursor.execute("select english from " + table + " where french = :question", {"question": question})
            results = query.fetchall()

        answer = results[0][0]

        driver.implicitly_wait(0)
        choices = driver.find_elements_by_class_name("val")
        if randint(0, 100) <= accuracy:
            for choice in choices:
                if choice.text == answer:
                    ActionChains(driver).move_to_element(choice).click(choice).perform()
                    break
        else:
            choice = choices[randint(0, len(choices)-1)]
            ActionChains(driver).move_to_element(choice).click(choice).perform()
        driver.implicitly_wait(delay)
