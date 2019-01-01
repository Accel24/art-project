import os




class utility:
    def google(args):
        os.system("start https://www.google.com/search?q="+args)
    def password(args):

        passwordExist = None


        args = args.lower()
        f = open("password.txt","r")
        line = f.readline()
        while line:
            line = line.split(":")

            if args in line[0]:

                print(line[1])
                passwordExist = True
                print("\n\n\n Press enter to continue")
                input()

                break
            else:

                passwordExist = False


            line = f.readline()
        if passwordExist == True:

            f.close()
            line = None
            read = None
        else:


            print("Password not found\n")
            print("Would you like to add it?\n")
            if input().upper() == "YES":

                print("Working on it")
                print("What password would you like to assign to account:"+ args+"\n")

                password = input()
                f.close()
                f = open("password.txt","a")
                f.write(args + ":" + password+"\n")
                print("Done\n")
                print("Press enter to continue")
                input()



            else:

                print("Understood.Cleaning...")
