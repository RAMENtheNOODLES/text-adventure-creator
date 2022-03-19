from nis import match
from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time
import custom_commands
import execute_command
import plugins

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

print("Welcome to text adventure!\nWIP")
print(Fore.GREEN + "┌──┬──┬─┐\n└┐┌┤┌┐│┌┘\n │││├┤│└┐\n └┘└┘└┴─┘")
print("T🖈C\nv0.0.1")

p = plugins.Plugins(colors)
cc = custom_commands.Custom_Commands()
ec = execute_command.Execute_Command()

chapters = []
c = open("story_chapters.txt", "r")
for i in c:
    print(i)
    chapters.append(i)


def read_story(chapter, option="story.tac"):
    f = open(f"{curdir}/{chapter}/{option}", "r")

    lines = f.read().split("\n")

    for i in lines:

        result = ec.FAE(i)

        if result == "stop":
            return

        # Need to check for stop, plugin, run_plugin, read_story,

        if not isinstance(result, str):
            for k in result.keys():
                if k == "plugin":
                    p.switch_file(result[k])
                if k == "run_plugin":
                    p.run_plugin(result[k] if result[k] != "" else 0)
                if k == "read_story":
                    goto_chapter = chapter

                    if result[k][0] == "cur":
                        goto_chapter = chapter

                    read_story(
                        goto_chapter,
                        result[k][1],
                    )

        continue

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
                        destinations[choices.split(", ").index(choice)] + ".tac",
                    )
                    return

                print("That is not a valid option...")
                continue

            print(after_text)
        if i.__contains__("wait"):
            time.sleep(int(i.split("wait, ")[1].split(":")[0]))
            print(i.split(": ")[1])
        if i.__contains__("goto > "):
            d_chapter = i.split("goto > ", "")[1].split(":")[0] + ".tac"
            d = i.split(": ")[1] + ".tac"
            read_story(d_chapter, d)
            return
        if i.__contains__("goto: "):
            read_story(chapter, i.split("goto: ")[1] + ".tac")
            return
        if i.__contains__("plugin > "):
            p.switch_file(i.split("plugin > ")[1] + ".plugin")
            p.run_plugin()
        if re.match("stop, (\w*): (\w*)", i):
            color = get_colors(i.split(", ")[1].split(":")[0])
            print(color + i.split(": ")[1])
            return
        if re.match("stop: (\w*)", i):
            print(i.split(": ")[1])
            return
        if i.__contains__("stop"):
            return
        if i.__contains__("import"):
            cc.import_command(i.split("> ")[1])

        for k in cc.imported.keys():
            if i.__contains__(k):
                cc.execute_command(i.split(" >")[0], i.split("> ")[1])


def get_colors(color_string: str) -> str:
    if color_string in colors:
        return colors[color_string]
    return colors["white"]


read_story("beginning")
