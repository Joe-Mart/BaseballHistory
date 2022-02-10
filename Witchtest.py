def witchtest():
    witch = input("Enter the weight of the suspect witch.\n")
    if float(witch) >= 125 and float(witch) <= 135:
        print("She weighs the same as a duck.  So she's a witch!\n")
    else:
        print("She's not a witch, even if she turned you into a Newt and you got over it\n")

    repeat = input("Would you like to retest?(y/n)\n")
    if repeat == "y" or repeat == "Y":
        witchtest()
    else:
        exit()

witchtest()


