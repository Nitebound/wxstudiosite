from pathlib import Path
import os

home_dir = os.path.dirname(os.path.realpath(__file__))+"/"
news_page = Path(home_dir + "../news.html")
print(news_page)


def add_news(date, news_list):
    file_lines = []
    
    with open(news_page, mode="r") as f:
        file_lines = f.readlines()

    begin_pos = 0
    counter = 0
    for line in file_lines:
        # Find the beginning of the news section
        begin_pos = line.find("<!--Begin-->")

        if begin_pos > 0:
            # print("Begin found at line: %s pos: %s" % (counter, begin_pos))
            # Prepare and insert the date
            date_line = "\n\t\t\t<h3 id=\"page-subtitle\"> ~ %s ~ </h3>\n" % date
            date_check = file_lines[counter+2].find(date)
            date_exists = False
            print(date_check)

            if date_check != -1:
                print("Date exists, updating news")
                date_exists = True

            if not date_exists:
                print("Appending date:", date_line)
                file_lines.insert(counter+1, date_line)
                file_lines.insert(counter+2, "\t\t\t<ul>\n")
                news_begin = counter+3
            else:
                news_begin = counter+4


            # Loop through news list and insert as html
            # list element
            newline_counter = 0

            for news_line in news_list:
                news_line = "\t\t\t\t<li id=\"centered-block\">" + news_line + "</li>\n"
                file_lines.insert(news_begin, news_line)
                newline_counter += 1

            if not date_exists:
                file_lines.insert(news_begin+newline_counter, "\t\t\t</ul>\n\n")

            for write_line in file_lines:
                print(write_line)
        counter += 1

    with open(news_page, mode="w") as f:
        for line in file_lines:
            f.write(line)

    print("News updated!")
