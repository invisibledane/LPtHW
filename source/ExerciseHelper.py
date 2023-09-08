def PEBKAC():
    print("Welp, looks like you don't want to play. Buh-bye.")
    exit

def GetUserInputAndCheckAgainstAcceptableValues(userPrompt, acceptableInputs, maxAttemptsAllowed, exitIf):
    
    attempts = maxAttemptsAllowed
    output = None

    while(attempts > 0):
        print(userPrompt)
        output = input("> ")

        for inputs in acceptableInputs:
            if output.lower() == inputs.lower():
                attempts = 0
                break
            elif attempts > 0 & (output == None | output == ""):
                print(f"Invalid input. Please try again. You have {attempts} remaining.")
                attempts -= 1
            else:
                output = None
                PEBKAC()

    return output

def GetUserInputsAndCheckAgainstNone(userPrompt):
    output = None

    while(attempts > 0):
        print(userPrompt)
        output = input("> ")

        if attempts > 0 & (output == None | output == ""):
            print(f"Invalid input. Please try again. You have {attempts} remaining.")
            attempts -= 1
        elif attempts == 0:
            PEBKAC()
        else:
            attempts = 0

    return output