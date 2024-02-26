command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("The car is started....")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("The car is stopped")
    elif command == "help":
        print("""Start - car will be run
Stop - Car will be stop
Quit - Game Over""")
    elif command == "quit":
        print("Game Over")
        break
    else:
        print("I don't understand")