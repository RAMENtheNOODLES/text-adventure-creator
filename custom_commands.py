from colorama import init, Fore, Back, Style, Cursor
import os
import re
import time

init(autoreset=True)

curdir = os.getcwd()

class Custom_Commands:
    
    def __init__(self):
        pass
    
    def new_command(self, fileloc=None, name=None, usage=None, body=None):
        if fileloc == None:
            file = open(input("Specify the location of a custom command file:\n>"))
        
        command = {
            "name": name if name != None else 
            "usage": usage if usage != None else input("Write a usage for your command:\n>"),
            "body": body if body != None else open(input("Specify the location of a custom command file:\n>"))
        }
        
        return command
    

if __name__ == "__main__":
    cc = Custom_Commands()
    cc.new_command(f"{curdir}/tac_commands/example.taccommand")
