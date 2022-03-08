from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time
import plugins

print("Welcome to text adventure!\nWIP")

init(autoreset=True)

curdir = os.getcwd()

colors = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
}

p = plugins.Plugins(colors)

chapters = []
c = open("story_chapters.txt", "r")
for i in c:
    print(i)
    chapters.append(i)


def read_story(chapter, option="story.txt"):
    f = open(f"{curdir}/{chapter}/{option}", "r")

    lines = f.read().split("\n")

    for i in lines:
        # print(i)

        if i.__contains__("`"):
            continue
        if i == "\n":
            continue
        if re.match("text, (\w*): ", i):
            color = get_colors(i.split(", ")[1].split(":")[0])
            # print(i.split(", ")[1].replace(":", ""))
            print(color + i.split(": ")[1])
            continue
        if i.__contains__("text"):
            print(i.split("text: ")[1])
        if i.__contains__("prompt"):
            choices = i.split("prompt, (")[1].split(")")[0]
            destinations = i.split("> (")[1].split(")")[0].split(", ")
            after_text = i.split(": ")[1]
            # print(choices)
            # print(destinations)

            print(f"Please select from one of these choices: ({choices})")

            while True:
                choice = input(">")

                if choice in choices.split(", "):
                    read_story(
                        chapter,
                        destinations[choices.split(", ").index(choice)] + ".txt",
                    )
                    return

                print("That is not a valid option...")
                continue

            print(after_text)
        if i.__contains__("wait"):
            time.sleep(int(i.split("wait, ")[1].split(":")[0]))
            print(i.split(": ")[1])
        if i.__contains__("goto > "):
            d_chapter = i.split("goto > ", "")[1].split(":")[0] + ".txt"
            d = i.split(": ")[1] + ".txt"
            read_story(d_chapter, d)
            return
        if i.__contains__("goto: "):
            read_story(chapter, i.split("goto: ")[1] + ".txt")
            return
        if i.__contains__("plugin > "):
            p.switch_file(i.split("plugin > ")[1] + ".plugin")
            p.run_plugin()


def get_colors(color_string):
    if color_string in colors:
        return colors[color_string]
    return colors["white"]


read_story("beginning")
