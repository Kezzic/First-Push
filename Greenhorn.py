import sys

####################################################################

def PartNarrative():
    print("the following is a narrative of logic")
    v = 1
    print("I set the value of variable v to:",v)
    v = v + 1
    print("The value has been increased by one:",v)
    v = 51
    print("Variables can be set to any value")
    print("v is now worth",v)
    print("v x 5 =",v * 5)
    y = v * 5
    print("y is now the value of the previous equation. y is now",y)
    print("v, ",v," is not y,",y)
    
    question = input("""
Would you like to restart the program?
Please type [Y]es or [N]o:
""")
    if question == 'YES' or question == 'yes' or question == 'y' or question == 'Y' or question == 'Yes':
        PartIntro()
    elif question == 'NO' or question == 'No' or question == 'no' or question == 'n' or question== 'N':
        print()
        print("Bye bitch.")
    else:
        print()
        print("u w0t m8? type facking yes or no.")
        PartIntro()


####################################################################

def PartInput():
    
    try:
        v = int(input("Please input value for v: "))
        y = int(input("Please input value for y: "))
    except ValueError:
        print()
        print("u w0t m8? type a facking number...")
        print()
        PartInput()
        
#FOLLOW-ON LOGIC
    else:
        if v > y:
            print()
            print("the variable v,",v," is greater than the variable y,",y)
        elif v < y:
            print()
            print("the variable v,",v," is less than the variable y,",y)
        else:
            print()
            print("the variable v,",v," is equal to the variable y,",y)

        question = input("""
Would you like to restart the program?
Please type [Y]es or [N]o:
""")
        if question == 'YES' or question == 'yes' or question == 'y' or question == 'Y' or question == 'Yes':
            PartIntro()
        elif question == 'NO' or question == 'No' or question == 'no' or question == 'n' or question== 'N':
            print()
            print("Bye bitch.")
        else:
            print()
            print("u w0t m8? type facking yes or no.")
            PartIntro()

####################################################################

def PartIntro():
    question = input("""
Would you like to hear example programming logic?
Please type [Y]es or [N]o:
""")
    if question == 'YES' or question == 'yes' or question == 'y' or question == 'Y' or question == 'Yes':
        print()
        PartNarrative()
    elif question == 'NO' or question == 'No' or question == 'no' or question == 'n' or question== 'N':

        question = input("""
Do you want to compare numbers?
Please type [Y]es or [N]o:
""")
        if question == 'YES' or question == 'yes' or question == 'y' or question == 'Y' or question == 'Yes':
            PartInput()
        elif question == 'NO' or question == 'No' or question == 'no' or question == 'n' or question== 'N':
            question = input("""
Would you like to restart the program?
Please type [Y]es or [N]o:
""")
            if question == 'YES' or question == 'yes' or question == 'y' or question == 'Y' or question == 'Yes':
                PartIntro()
            elif question == 'NO' or question == 'No' or question == 'no' or question == 'n' or question== 'N':
                print()
                print("Bye bitch.")
            else:
                print()
                print("u w0t m8? type facking yes or no.")
                PartIntro()
        else:
            print()
            print("u w0t m8? type facking yes or no.")
            PartIntro()
    else:
        print()
        print("u w0t m8? type facking yes or no.")
        PartIntro()

####################################################################

#Variables have been defined
#INITIATE SEQUENCE

PartIntro()


