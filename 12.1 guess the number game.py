import random


print("Hey, i am thinking of a number between 1 and 100. "
      "can you guess the number?")

####### set difficulty #########

difficulty = input("choose the difficulty level 'easy' or 'hard' :  ")

chances = 0

if difficulty == 'hard':
    chances = 5
    print(f"you have {chances} chances to guess the correct number")
else:
    chances = 10
    print(f"you have {chances} chances to guess the correct number")

########## computer guessing random number ###############
cmm_list = []
for _ in range(10):
    x = int(random.randint(0, 100))
    cmm_list.append(x)

random.shuffle(cmm_list)

cmp_num = random.choice(cmm_list)


#############################################################################
#  A FUNCTION TO COMPARE THE USR NUMBER AND COMPUTER NUMBER 

def compare(usr, cmp):

    for near_value in range(1, 6):
        if usr > cmp and usr - near_value == cmp:
            print(" very close")
        elif usr < cmp and usr + near_value == cmp:
            print(" very close")

    # if usr > cmp and usr - 1 == cmp:
    #     print(" very close")
    #
    # elif usr > cmp and usr - 2 == cmp:
    #     print(" very close")
    #
    # elif usr > cmp and usr - 3 == cmp:
    #     print(" very close")
    #
    # elif usr > cmp and usr - 4 == cmp:
    #     print(" very close")
    #
    # elif usr > cmp and usr - 5 == cmp:
    #     print(" very close")
    #
    # elif usr < cmp and usr + 1 == cmp:
    #     print("very close")
    #
    # elif usr < cmp and usr + 2 == cmp:
    #     print("very close")
    #
    # elif usr < cmp and usr + 3 == cmp:
    #     print("very close")
    #
    # elif usr < cmp and usr + 4 == cmp:
    #     print("very close")
    #
    # elif usr < cmp and usr + 5 == cmp:
    #     print("very close")

    if usr > cmp:
        print("too high")

    elif usr < cmp:
        print("too low")

    elif usr > 100:
        print("u must guess between 1 and 100.")

############################### END OF COMPARE FUNCTION #############################################################


###### LOOPING THE GAME TO ASK AGAIN AND AGAIN UNTIL CHANCES = 0 ###########

loop_condition = True

while loop_condition:
    usr_in = int(input("make a guess:"))
    compare(usr_in, cmp_num)

    if chances == 0:
        loop_condition = False
        print("u are out of your luck!")

    elif usr_in != cmp_num:
        chances -= 1
        print(f"you have {chances} chances remaining")
        if usr_in != cmp_num and chances == 0:
            print(f"well correct answer was {cmp_num} ")
            loop_condition = False

    elif usr_in == cmp_num:
            loop_condition = False
            print("Damn!! u just beat the computer.")
