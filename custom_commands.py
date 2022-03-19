from ctypes import Array
from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time

init(autoreset=True)

curdir = os.getcwd()


class Custom_Commands:
    def __init__(self):
        self.imported = {}

    def import_command(self, command_name: str):
        loc = curdir + "/tac_commands/" + command_name + ".taccommand"
        print(loc)
        f = open(loc, "r")
        params = []
        command = ""

        lines = f.read().split("\n")

        for i in lines:
            if i.__contains__("`"):
                continue
            if i.__contains__("name"):
                continue
            if i.__contains__("desc"):
                continue
            if i.__contains__("params"):
                params = i.split("> ")[1].split(", ")
            if i.__contains__("disp"):
                command = i.split("> ")[1]

        self.imported.update(
            {command_name: {"dir": loc, "params": params, "command": command}}
        )

    def execute_command(self, command_name: str, cinput: Array) -> str:
        if command_name not in self.imported.keys():
            return (
                f"stop, red: Error: Command {command_name} "
                + f"either doesn't exist or isn't imported..."
            )

        params = self.imported[command_name]["params"]
        raw_command: str = self.imported[command_name]["command"]
        print(f"Params: {params}\nRaw Command: {raw_command}")
        comp_command = ""

        if len(cinput) < len(params):
            return (
                f"stop, red: Error: Command {command_name} "
                + f"expected {len(params)} params but got {len(cinput)} param(s) instead..."
            )

        for i in range(len(params)):
            if i == 0:
                comp_command = raw_command.replace(f"${params[i]}", cinput[i])
            else:
                comp_command = comp_command.replace(f"${params[i]}", cinput[i])

        return comp_command

    """""
    def new_command(self, fileloc=None, name=None, usage=None, body=None):
        if fileloc == None:
            file = open(input("Specify the location of a custom command file:\n>"))
        
        command = {
            "name": name if name != None else 
            "usage": usage if usage != None else input("Write a usage for your command:\n>"),
            "body": body if body != None else open(input("Specify the location of a custom command file:\n>"))
        }
        
        return command
    """ ""


if __name__ == "__main__":
    cc = Custom_Commands()
    cc.import_command("example")
    print(cc.execute_command("example", ["red", "another test"]))
