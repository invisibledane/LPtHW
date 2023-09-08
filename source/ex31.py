def GetUserInput(userPrompt, attempts, acceptableResponses):
    
    userInput = None
    output = None

    while attempts > 0:
        print(f"\n{userPrompt}")
        userInput = input("> ").lower()

        for value in acceptableResponses:
            if userInput == value.lower():
                attempts = 0
                output = userInput
                break
        
        if output == None:
            print(f"Invalid input. Please try again. You have {attempts} remaining.")
            attempts -= 1
        else:
            attempts = 0
    
    return output
    
def PEBKAC():
    print("Welp, looks like you don't want to play. Buh-bye.")
    exit

def main():
    question = """You enter a dark room with two doors.
        Do you go through door #1 or door #2?"""
    
    
    result = GetUserInput(question, 3, ["1", "one", "2", "two"])

    if result != None:
        if result == "1" or result == "one":
            question = "There's a giant bear here eating a cheese cake.\nWhat do you do? \n1. Take the cake.\n2. Scream at the bear."

            result = GetUserInput(question, 3, ["1", "one", "2", "two"])

            if result != None:
                if result == "1" or result == "one":
                    print("The beats eats your face off. Obviously.")
                elif result == "2" or result == "two":
                    print("The bear eats your legs off. Obviously.")
                else:
                    PEBKAC()
        elif result == "2" or result == "two":
            question = """You stare into the endless abyss at Cthulu's retina."
            1. Blueberries.
            2. Yellow jacket clothespins."
            3. Understanding revolvers yelling melodies."""

            result = GetUserInput(question, 3, ["1", "one", "2", "two", "3", "three"])
            if result == "1" or result == "one" or result == "2" or result == "two":
                print("Your body survives powered by a mind of jello.")
                print("Good job ... I guess.")
            elif result == "three" or result == "3":
                print("The insanity rots your eyes into a pool of muck.")
                print("Good ... job?")
            else:
                PEBKAC()
    else:
        PEBKAC()

    print("\nWow. What a day, huh? Press any key to go to bed.")
    input()

main()
