from colorama import init, Fore, Back, Style, Cursor
import re
import time


init(autoreset=True)


class Commands:
    def __init__(self):
        pass
    
    def find_command(self, line, lines, mode="story"):
        file = self.file
        i = line
        if i.__contains__("`"):
            return "comment"
        if i.__contains__("func"):
            return "function"
        if i == "\n":
            return "blank-line"
        if i.__contains__("\t") or i.__contains__("    "):
            return "inside of function"
        if re.match("text, (\w*): ", i):
            # print(i)
            color = self.get_colors(i.split(", ")[1].split(":")[0])
            # print(i.split(", ")[1].replace(":", ""))
            print(color + i.split(": ")[1])
            return "text-color"
        if i.__contains__("text: "):
            print(i)
            print(i.split("text: ")[1])
            return "text"
        if i.__contains__("run > "):
            func_name = i.split("run > ")[1]

            self.get_function(lines, func_name)
        if i.__contains__("prompt"):
            choices = i.split("prompt, (")[1].split(")")[0]
            destinations = i.split("> (")[1].split(")")[0].split(", ")
            after_text = i.split(": ")[1]
            # print(choices)
            # print(destinations)

            print(f"Please select from one of these choices: ({choices})")

            while True:
                choice = input(">")

                # print(len(lines))

                if choice.lower() in choices.lower().split(", "):
                    self.get_function(lines, choice.lower())
                    return

                print("That is not a valid option...")
                continue

            print(after_text)
            return "prompt"
        if i.__contains__("wait"):
            time.sleep(int(i.split("wait, ")[1].split(":")[0]))
            print(i.split(": ")[1])
            return "wait"
        if i.__contains__("goto > "):
            d_chapter = i.split("goto > ", "")[1].split(":")[0] + ".tac"
            d = i.split(": ")[1] + ".tac"
            read_story(d_chapter, d)
            return "goto-chapter"
        if i.__contains__("goto: "):
            read_story(chapter, i.split("goto: ")[1] + ".tac")
            return "goto"
        if i.__contains__("plugin > "):
            p.switch_file(i.split("plugin > ")[1] + ".plugin")
            p.run_plugin()
            return
        
    def get_function(self, lines: list, func_name: str):
        for k in range(len(lines)):
            if lines[k] == f"func {func_name.lower()} " + "{":
                pluginstr = ""
                for j in lines:
                    pluginstr += j + "\n"

                # print(lines[k])
                function = pluginstr.split("func " + func_name + " {")[1].split("}")[0]
                # print(function)

                for j in function.replace("    ", "").split("\n"):
                    # print(f"J: {j}")
                    if j != "\n":
                        self.store.append(j)
        return

    def get_colors(self, color_string):
        if color_string in self.colors:
            return self.colors[color_string]
        return self.colors["white"]
