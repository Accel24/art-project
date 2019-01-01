import time


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
    
    
    
    
