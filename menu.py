import utility    

def menu(args):
    if args.upper().startswith("GOOGLE:"):
        userDesire = userDesire.split(":")
        userDesire = userDesire[1]
        userDesire = userDesire.replace(" ","%20")
        utility.google(args)
