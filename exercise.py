from selenium.webdriver.common.action_chains import ActionChains
from helpers import login, submit
import sqlite3

def exercise(level, url, username, password, accuracy, option):
    driver = login(username, password)
    accuracy = int(accuracy)
    level = str(level)

    level_str = "level" + level
    driver.get(url + level
        + ("/garden/classic_review/?source_element=level_details_session&source_screen=level_details"
        if option == 2 else
        "/garden/learn/?source_element=level_details_session&source_screen=level_details")
    )

    prev_question = ""
    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()

    while True:
        try:
            driver.find_element_by_id("session-complete-banner")
            break
        except:
            pass

        try:
            question = driver.find_element_by_class_name("qquestion").text
            submit(driver, url, cursor, question, accuracy)
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
