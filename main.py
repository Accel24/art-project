import time
from menu import menu
import os


def main():
    print("Input your password:")
    password = input()
    if password == "dev":
        loggedIn = True
    else:
        exit()
    print("\nThanks\n")
    print("You are logged in\n")
    time.sleep(3)
    os.system('cls')
    done = False
    while not done:
        print("What would you like to do?\n")
        userWish = input()
        menu(userWish)
        os.system('cls')

        
main()
        
        
        
    
    
    
    
