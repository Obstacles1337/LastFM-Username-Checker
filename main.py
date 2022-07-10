##Commented out the taken, but if you want to view the taken. You can.


import requests
from colorama import Fore, init

init()

class LastFM():
    def __init__(self):

        self.targets = open("targets.txt").read().splitlines()
        self.valid = open("valid.txt", "a+")
    
    def check(self):
        for targets in self.targets:
            checkusername = requests.get(f"https://www.last.fm/user/{targets}")

            if checkusername.status_code == 404:
                print(f"[{Fore.GREEN}+{Fore.WHITE}] {targets} is not taken!")
                self.valid.write(f"{targets}\n")
            #elif ("That username is taken." in checkusername.text):
              #  print(f"[{Fore.RED}+{Fore.WHITE}] {targets} is taken!")

if __name__ == "__main__":
    LastFMChecker = LastFM()
    LastFMChecker.check()
    
    #Discord: Obstacles#5096
