command=""
while command!="y":
    command=input(">").lower()
    if command=="start":
        print("car stated")
    elif command=="stop":
        print("car stopped")
    elif command=="help":
        print("""
        start- to start the program
        stop- to stop the program
        quit- to quit
        """)
    elif command=="quit":
        print("are you sure to quit the game\nif yes enter the 'y' or enter the 'n'")
        p=input(">").lower()
        if p=="y":
            break
        else:
            continue
    else:
        print("sorry i don't undertand that")
