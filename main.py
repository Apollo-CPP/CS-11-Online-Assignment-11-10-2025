while True:
    Name = input("Hello! What is your name?: ")

    if not Name or len(Name) == 0 or Name.isspace():
        print("You inputted nothing or you put only put spaces >:(")
        continue
    else:
        print(f"{Name} is cool!")
        break