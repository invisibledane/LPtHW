from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else: dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat baert is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("""On the plus side, the bear moves. On the minus side, 
                 it moved forward to fuck you the fuck up.""")
        elif choice == "taunt bear" and not bear_moved:
            print("""On the plus side, bear has moved from the door.
                  On the minus side, you've irrevocably hurt its feeling.
                  You'll never be friends.""")
            print("You can go through the door now.")
        elif choice == "taunt bear" and bear_moved:
            dead("""Recalling a childhood of bullying and ridicule, 
                 the bear becomes enraged. It quickly proceeds to fuck you the fuck up.""")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("You confuse the bear and it proceeds to fuck you the fuck up for the lack of another option.")
            print("I mean, what did you expect? It's a bear.")

def cthulu_room():
    print("""Here you see the great evil, Cthulu.
          He, it, whatever ... stares at you and you go insane.
          Do you flee for your life or eat your head?""")
    
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty. And lethal.")
    else:
        cthulu_room()

def dead(why):
    print(why, "You're dead.")
    exit(0)

def start():
    print("""You are in a dark room.
          There is a door to your right and left.
          Which one do you take?""")
    
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()