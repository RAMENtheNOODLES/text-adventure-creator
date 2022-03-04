from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time

init(autoreset=True)

curdir = os.getcwd()

class Plugins:
    def __init__(self, mColors, file):
        self.colors = mColors
        self.store = []
        self.file = str(file)

    def run_plugin(self, linenum=0):
        f = open(f"{curdir}/plugins/{self.file}", "r")

        lines = f.read().split("\n")

        for i in lines:
            if len(self.store) > 0:
                print(*self.store)
                for k in self.store:
                    self.execute(k, lines)
                self.store = []
                continue
            self.execute(i, lines)

            
    def execute(self, line, lines):
        file = self.file
        i = line
        if i.__contains__("`"):
            return 'comment'
        if i.__contains__("func"):
            return 'function'
        if i.__contains__("\t\t"):
            return 'inside of function'
        if re.match("text, (\w*): ", i):
            print(i)
            color = self.get_colors(i.split(", ")[1].split(":")[0])
            # print(i.split(", ")[1].replace(":", ""))
            print(color + i.split(": ")[1])
            return 'text-color'
        if i.__contains__("text: "):
            print(i)
            print(i.split("text: ")[1])
            return 'text'
        if i.__contains__("prompt"):
            choices = i.split("prompt, (")[1].split(")")[0]
            destinations = i.split("> (")[1].split(")")[0].split(", ")
            after_text = i.split(": ")[1]
            # print(choices)
            # print(destinations)

            print(f"Please select from one of these choices: ({choices})")

            while True:
                choice = input(">")
                
                print(len(lines))

                if choice.lower() in choices.lower().split(", "):
                    for k in range(len(lines)):
                        if lines[k] == f"func {choice.lower()} " + "{":
                            pluginstr = ""
                            for j in lines:
                                pluginstr += j + "\n"
                            
                            print(lines[k])
                            function = pluginstr.split("func " + choice + " {")[1].split("}")[0]
                            print(function)
                            
                            for j in function.replace("    ", "").split("\n"):
                                print(f"J: {j}")
                                if j != "\n":
                                    self.store.append(j)
                    return

                print("That is not a valid option...")
                continue

            print(after_text)
            return 'prompt'
        if i.__contains__("wait"):
            time.sleep(int(i.split("wait, ")[1].split(":")[0]))
            print(i.split(": ")[1])
            return 'wait'
        if i.__contains__("goto > "):
            d_chapter = i.split("goto > ", "")[1].split(":")[0] + ".txt"
            d = i.split(": ")[1] + ".txt"
            read_story(d_chapter, d)
            return 'goto-chapter'
        if i.__contains__("goto: "):
            read_story(chapter, i.split("goto: ")[1] + ".txt")
            return 'goto'
        
    def get_colors(self, color_string):
        if color_string in colors:
            return self.colors[color_string]
        return self.colors["white"]
        
        
p = Plugins({
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
}, "example.plugin")
p.run_plugin()
