from utility import utility

def menu(args):
    if args.upper().startswith("GOOGLE:"):
        args = args.split(":")
        args = args[1]
        args = args.replace(" ","%20")
        utility.google(args)
    if args.upper().startswith("PASSWORD:"):
        args = args.split(":")
        args = args[1]
        utility.password(args)
    if args.upper().startswith("EXIT"):
        exit()
