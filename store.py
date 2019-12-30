from helpers import login
import sqlite3

def store(level, course, username, password):
    driver = login(username, password)
    course = int(course)
    level = str(level)

    level_str = "level" + level
    url = "https://www.memrise.com/course/5572813/francais-3/" if course else "https://www.memrise.com/course/5538726/daccord-2/"
    driver.get(url + level)

    col_a = driver.find_elements_by_class_name("col_a")
    col_b = driver.find_elements_by_class_name("col_b")

    dict = {}

    for col_1, col_2 in zip(col_a, col_b):
        dict[col_1.text] = col_2.text

    conn = sqlite3.connect("french3.db" if course else "french2.db")
    cursor = conn.cursor()

    try:
        cursor.executescript("""
            create table if not exists """ + level_str + """ (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                french TEXT NOT NULL,
                english TEXT NOT NULL
            );
        """)
        for key in dict:
            cursor.execute("insert or replace into " + level_str + " (french, english) values (:fr, :eng)", {"fr": key, "eng": dict[key]})
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
