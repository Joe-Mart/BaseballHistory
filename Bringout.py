def bringoutdead():
    bringdate = input("What day is it?\n")
    if bringdate == "Monday" or bringdate == "Thursday":
        print("Bring out your dead!\n")
    else:
        print("Don't bring out the dead.\n")

    repeat = input("Would you like to re-check?(y/n)?\n")
    if repeat == "y" or repeat == "Y":
        bringoutdead()
    else:
        exit()


bringoutdead()