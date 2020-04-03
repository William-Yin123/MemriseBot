from helpers import login
import sqlite3


def store(level, url, username, password):
    driver = login(username, password)
    level = str(level)

    level_str = "level" + level
    driver.get(url + level)

    col_a = driver.find_elements_by_class_name("col_a")
    col_b = driver.find_elements_by_class_name("col_b")

    dict = {}

    for col_1, col_2 in zip(col_a, col_b):
        dict[col_1.text] = col_2.text

    conn = sqlite3.connect("words.db")
    cursor = conn.cursor()

    try:
        cursor.executescript("""
            create table if not exists [""" + url + """] (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                french TEXT NOT NULL,
                english TEXT NOT NULL
            );
        """)
        for key in dict:
            cursor.execute("insert or replace into [" + url + "] (french, english) values (:fr, :eng)", {"fr": key, "eng": dict[key]})
        conn.commit()
        print("Successfully stored terms")
    except:
        print("An error occurred while storing terms")

    conn.close()
    driver.close()

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    store(*args)
