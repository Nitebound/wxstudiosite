import os
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
from tkinter import messagebox as mbox
from datetime import datetime as date
import newstools
import refactoring as rf

root = tk.Tk()

# Define paths
home_dir = os.path.dirname(os.path.realpath(__file__))+"/"


# The base class to hold events allowing
# undo and redo
class WmEvent:
    event_count = 0

    def __init__(self, b_data):
        self.index = WmEvent.event_count
        self.backup_data = []
        WmEvent.event_count += 1


class WmManager:
    def __init__(self):
        self.events = []


def add_news_entry():
    entry = simpledialog.askstring("Input", "Entry?", parent=root)
    base_entry = entry

    if (entry is not None) and bool(entry):
        if "Home" in entry:
            print("Replaced Home with link to Home page")
            entry = entry.replace("Home", "<a href=\"home.html\" id=\"normal-link-green\" target=\"content\">"
                                  "Home</a>")

        if "News" in entry:
            print("Replaced News with link to News page")
            entry = entry.replace("News", "<a href=\"news.html\" id=\"normal-link-green\" target=\"content\">"
                                  "News</a>")

        if "Downloads" in entry:
            print("Replaced Downloads with link to Downloads page")
            entry = entry.replace("Downloads", "<a href=\"downloads.html\" id=\"normal-link-green\" target=\"content\">"
                                  "Downloads</a>")

        if "Tutorials" in entry:
            print("Replaced Tutorials with link to Tutorials page")
            entry = entry.replace("Tutorials", "<a href=\"tutorials.html\" id=\"normal-link-green\" target=\"content\">"
                                  "Tutorials</a>")

        if "About Us" in entry:
            print("Replaced About Us with link to About Us page")
            entry = entry.replace("About Us", "<a href=\"aboutus.html\" id=\"normal-link-green\" target=\"content\">"
                                  "About Us</a>")

        if "Forum" in entry:
            print("Replaced Forum with link to Forum page")
            entry = entry.replace("Forum", "<a href=\"forum.html\" id=\"normal-link-green\" target=\"content\">"
                                  "Forum</a>")

        print("Adding:", entry, "- to News")
        date_str = date.today().strftime("%A") + " "
        date_str += date.today().strftime("%d-%m-%Y")
        print("For", date_str)
        newstools.add_news(date_str, [entry])
        print("Added:", entry, "to News")
        label_text = "News Update: [ %s ]" % base_entry
        news_label = tk.Label(text=label_text)
        news_label.pack()


def ask_replace_file():
    selected_file = askopenfilename()
    print(selected_file)
    search = simpledialog.askstring("Replace", "Search for?", parent=root)
    replace = simpledialog.askstring("Replace", "Replace with?", parent=root)
    ready_check = mbox.askyesnocancel("Are you sure?", "Are your sure you want to replace %s with %s? in %s" %
                                      (search, replace, selected_file))

    if ready_check:
        print("Replacing %s with %s" % (search, replace))
        rf.refactor_file(selected_file, search, replace, rf.ALLMATCHES)


# Initialize the top menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)
menubar.config(background="grey")

# Initialize the file menu on the menu bar
filemenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Push Changes")

# Initialize the news menu on the menu bar
newsmenu = tk.Menu(menubar)
menubar.add_cascade(label="News", menu=newsmenu)
newsmenu.add_command(label="Add Entry", command=add_news_entry)

# Initialize the project menu on the menu bar
projectmenu = tk.Menu(menubar)
menubar.add_cascade(label="Project", menu=projectmenu)
projectmenu.add_command(label="Refactor", command=ask_replace_file)

# Initialize the event history for undo and redo
event_history = []

root.mainloop()
