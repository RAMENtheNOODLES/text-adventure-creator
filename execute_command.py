from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time
import custom_commands

init(autoreset=True)

curdir = os.getcwd()

cc = custom_commands.Custom_Commands()


class Execute_Command:
    def __init__(self):
        self.colors = {
            "black": Fore.BLACK,
            "red": Fore.RED,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE,
        }

    def FAE(self, line) -> dict:
        if line.__contains__("`"):
            return "comment"
        if line == "\n":
            return "blank line"
        if re.match("text, (\w*): ", line):
            color = self.get_colors(line.split(", ")[1].split(":")[0])
            # print(i.split(", ")[1].replace(":", ""))
            print(color + line.split(": ")[1])
            return "text color"
        if line.__contains__("text"):
            print(line.split("text: ")[1])
            return "text"
        if line.__contains__("prompt"):
            choices = line.split("prompt, (")[1].split(")")[0]
            destinations = line.split("> (")[1].split(")")[0].split(", ")
            after_text = line.split(": ")[1]
            # print(choices)
            # print(destinations)

            print(f"Please select from one of these choices: ({choices})")

            while True:
                choice = input(">")

                if choice in choices.split(", "):
                    return {
                        "read_story": [
                            "cur",
                            destinations[choices.split(", ").index(choice)] + ".tac",
                        ]
                    }

                print("That is not a valid option...")
                continue
        if line.__contains__("wait"):
            time.sleep(int(line.split("wait, ")[1].split(":")[0]))
            print(line.split(": ")[1])
            return "wait"
        if line.__contains__("goto > "):
            d_chapter = line.split("goto > ", "")[1].split(":")[0] + ".tac"
            d = line.split(": ")[1] + ".tac"
            return {"read_story": [d_chapter, d]}
        if line.__contains__("goto: "):
            return {"read_story": ["cur", line.split("goto: ")[1] + ".tac"]}
        if line.__contains__("plugin > "):
            return {"plugin": line.split("plugin > ")[1] + ".plugin", "run_plugin": ""}
        if re.match("stop, (\w*): (\w*)", line):
            color = self.get_colors(line.split(", ")[1].split(":")[0])
            print(color + line.split(": ")[1])
            return "stop"
        if re.match("stop: (\w*)", line):
            print(line.split(": ")[1])
            return "stop"
        if line.__contains__("stop"):
            return "stop"
        if line.__contains__("import"):
            cc.import_command(line.split("> ")[1])

        for k in cc.imported.keys():
            if line.__contains__(k):
                cc.execute_command(line.split(" >")[0], line.split("> ")[1])
        return "not found"

    def get_colors(self, color_string: str) -> str:
        if color_string in self.colors:
            return self.colors[color_string]
        return self.colors["white"]
