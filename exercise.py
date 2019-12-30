from selenium.webdriver.common.action_chains import ActionChains
from helpers import login, submit
import sqlite3

def exercise(level, course, username, password, accuracy, option):
    driver = login(username, password)
    accuracy = int(accuracy)
    course = int(course)
    level = str(level)

    level_str = "level" + level
    url = "https://www.memrise.com/course/5572813/francais-3/" if course else "https://www.memrise.com/course/5538726/daccord-2/"
    driver.get(url + level + ("/garden/classic_review/?source_element=level_details_session&source_screen=level_details" if option == 2 else "/garden/learn/?source_element=level_details_session&source_screen=level_details"))

    prev_question = ""
    conn = sqlite3.connect("french3.db" if course else "french2.db")
    cursor = conn.cursor()

    while True:
        try:
            driver.find_element_by_id("session-complete-banner")
            break
        except:
            pass

        try:
            question = driver.find_element_by_class_name("qquestion").text
            submit(driver, level_str, cursor, question, accuracy)
        except:
            try:
                btn = driver.find_element_by_class_name("next-button")
                ActionChains(driver).move_to_element(btn).click(btn).perform()
            except:
                pass

    conn.close()
    driver.close()

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    exercise(*args)
