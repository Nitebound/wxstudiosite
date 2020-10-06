import os
import os.path
from pathlib import Path

home_dir = os.path.dirname(os.path.realpath(__file__))

EXACTMATCHES = 0
ALLMATCHES = 1

def refactor_file(filepath, search_text, replace_text, flag=ALLMATCHES):
    """This function will replace all occurances of a certain string with another"""
    file_lines = []
    filepath = Path(filepath)
    print(filepath)
    with open(filepath, mode="r") as f:
        file_lines = f.readlines()

    if flag == ALLMATCHES:
        if file_lines:
            print("\nReplacing all occurances of \"" + search_text + "\" with \"" + replace_text + "\"")
            print("In:",  filepath)

            try:
                with open(filepath, mode='w') as f:
                    counter = 0
                    match_counter = 0
                    for line in file_lines:
                        if search_text in line:
                            print("changing line:", counter, "--")
                            print(line)
                            print("to --")
                            file_lines[counter] = line.replace(search_text, replace_text)
                            print(file_lines[counter])
                            print()
                            match_counter += 1
                        counter += 1

                    for line in file_lines:
                        f.write(line)

                if match_counter:
                    print("Found and replaced", match_counter, "exact matches.")
                else:
                    print("\nNo matches found.")

            except FileNotFoundError:
                print(filepath, "not found.")

    elif flag == EXACTMATCHES:
        if file_lines:
            print("\nReplacing all exact occurances of \"" + search_text + "\" with \"" + replace_text + "\"")
            print("In:",  filepath)
            match_counter = 0

            try:
                with open(filepath, mode='w') as f:
                    counter = 0
                    for line in file_lines:
                        if search_text in line:
                            match_position = line.find(search_text)

                            back_check = match_position - 1
                            front_check = match_position + len(search_text)
                            # print("leading character:", line[back_check] )
                            # print("following character:", line[front_check])

                            if(line[back_check] == " " and line[front_check] == " ") or \
                                (back_check < 0 or None and line[front_check] == " "):
                                print("Found match at position:", match_position)
                                print("In line:", counter)
                                print("changing line:", counter, "--")
                                print(line)
                                print("to --")
                                file_lines[counter] = line.replace(search_text, replace_text)
                                print(file_lines[counter])
                                print()
                                match_counter += 1
                        counter += 1

                    for line in file_lines:
                        f.write(line)

                if match_counter:
                    print("Found and replaced", match_counter, "exact matches.")
                else:
                    print("\nNo exact matches found.")

            except FileNotFoundError:
                print(filepath, "not found.")


def refactor_project(folderpath, search_text, replace_text, flag=None):
    """This function will replace all occurances of a certain string with another"""
    for directory, subdirectories, files in os.walk(folderpath):
        for file in files:
            print("\nChanging", file)
            refactor_file(project_dir + file, search_text, replace_text, flag)

