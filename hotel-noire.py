def gameTitle():
    # Start by asking for the user's name:
    print("HOTEL NOIRE: A Murder/Mystery Text Game")
    print("By: Christopher Fergo Jr.")
    print("(c) 2022\n")
    name = input("Enter your name?: ")
    print(f"Hello, {name}! Welcome to HOTEL NOIRE.")
    input("Press 'ENTER' to begin adventure.")
    first()

def first():
    print("Our story begins on a cold and wet December night. You've been driving for hours when finally you arrive at your destination THE HOLLOWS INN.")
    print("You grab your luggage from the trunk and enter the lobby.")
    print("You look around. No one is there to greet you.")
    print("You notice a BELL on the counter.")
    ringChoice = input("What do you do?: ").upper()

    if ringChoice == "RING" or ringChoice == "RING BELL":
        print("An overweight, greasy looking man approaches you from behind the desk.")
        print("\"My name is Mr. Dunning. Welcome to the Hollows Inn. Will you be STAYING with us tonight?\"")
        second()
    elif ringChoice == "EXIT" or ringChoice == "LEAVE":
        print("You decide this hotel looks like a dump and leave.")
        print("Pretty anti-climatic.")
        input("Press 'ENTER' to restart game.")
        gameTitle()
    else:
        print("You must reply RING or LEAVE.")
        input("Press 'Enter' to continue.")
        first()

def second():
    stayChoice = input("STAY at Hollows Inn?: ").upper()

    if stayChoice == "YES" or stayChoice == "STAY":
        print("Mr. Dunning answers excitedly \"Excellent! It will be $100 a night. You'll be staying in ROOM 6. Let me get your KEY.\"")
        print("Mr Dunning hands you the KEY.")
        third()
    elif stayChoice == "NO" or stayChoice == "LEAVE":
        print("Mr. Dunning frowns.")
        print("\"Well then don't waste my time!\"")
        print("You leave the hotel. Pretty anti-climatic.")
        print("THE END!")
        input("Press 'ENTER' to restart game.")
        gameTitle()
    else:
        print("You must reply Yes or no.")
        input("Press 'Enter' to continue.")
        second()

def third():
    print("You proceed around the lobby.")
    print("In front of you is the STAIRS. To your left is an old ELEVATOR.")
    elevationChoice = input("Which do you take?: ").upper()

    if elevationChoice == "STAIRS":
        print("You proceed up the stairs to your room.")
        fourth()
    elif elevationChoice == "ELEVATOR":
        print("The ELEVATOR reads \"Out of Order\"")
        print("Maybe you should try the STAIRS.")
        input("Press 'Enter' to continue.")
        third()
    else:
        print("You must choose between ELEVATOR or STAIRS")
        input("Press 'Enter' to continue.")
        third()

def fourth():
    print("At the top of the stairs is a sign")
    print("<-- ROOMS 1-5 | ROOMS 6-10 -->")
    hallwayChoice = input("Which way do you go?: ").upper()

    if hallwayChoice == "LEFT":
        print("You decide to go left.")
        print("Rooms 1-5")