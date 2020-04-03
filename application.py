import tkinter as tk
from exercise import exercise
from store import store


def user_input():
    username = username_field.get()
    password = password_field.get()
    level = int(level_field.get())
    url = url_field.get()
    option = int(option_field.get())

    accuracy = None
    sessions = None
    try:
        tmp = int(accuracy_field.get())
        accuracy = tmp
        tmp = int(sessions_field.get())
        sessions = tmp
    except:
        pass

    if option == 0:
        store(level, url, username, password)
    elif accuracy and sessions:
        for i in range(sessions):
            exercise(level, url, username, password, accuracy, option)


root = tk.Tk()
tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Password").grid(row=1)
tk.Label(root, text="Level").grid(row=2)
tk.Label(root, text="Url").grid(row=3)
tk.Label(root, text="Option").grid(row=4)
tk.Label(root, text="Percentage of Accuracy").grid(row=7)
tk.Label(root, text="Sessions").grid(row=8)

username_field = tk.Entry(root)
password_field = tk.Entry(root)
level_field = tk.Entry(root)
url_field = tk.Entry(root)
option_field = tk.IntVar()
accuracy_field = tk.Entry(root)
sessions_field = tk.Entry(root)

username_field.grid(row=0, column=1)
password_field.grid(row=1, column=1)
level_field.grid(row=2, column=1)
url_field.grid(row=3, column=1)
tk.Radiobutton(root, value=0, variable=option_field, text="Store", indicatoron=0).grid(row=4, column=1)
tk.Radiobutton(root, value=1, variable=option_field, text="Learn", indicatoron=0).grid(row=5, column=1)
tk.Radiobutton(root, value=2, variable=option_field, text="Review", indicatoron=0).grid(row=6, column=1)
accuracy_field.grid(row=7, column=1)
sessions_field.grid(row=8, column=1)

tk.Button(root, text="Submit", command=user_input).grid(row=9, column=1)

root.mainloop()
