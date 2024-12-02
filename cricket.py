import random

Score = 0
print("You choose Bowling.\nLet's start the Match ...")
while True:
    
    user = int(input())
    while(user>6 or user<1):
        print("Enter between 1 to 6:",end=" ")
        user = int(input())
    comp = random.randint(1,6)
    
    # print(comp)

    if (comp == user):
        if (comp == 1):
            print("Computer scored 1 Runs...","Total Score = ",Score)
        if (comp == 2):
            print("Computer scored 2 Runs...","Total Score = ",Score)
        if (comp == 3):
            print("Computer scored 3 Runs...","Total Score = ",Score)
        if (comp == 4):
            print("Computer scored 4 Runs...","Total Score = ",Score)
        if (comp == 5):
            print("Computer scored 5 Runs...","Total Score = ",Score)
        if (comp == 6):
            print("Computer scored 6 Runs...","Total Score = ",Score)
        print("--- OUT ---\n")
        print("Want to play again ?")
        print("1.Yes \n2.No\n")
        num = int(input())
        if (num == 1):
            Score = 0
            continue
        if (num == 2):
            print("\nThanks for Playing...\nCome Again !!\n")
            break

    else:
        Score+=comp
        if (comp == 1):
            print("Computer scored 1 Runs...","Total Score = ",Score)
        if (comp == 2):
            print("Computer scored 2 Runs...","Total Score = ",Score)
        if (comp == 3):
            print("Computer scored 3 Runs...","Total Score = ",Score)
        if (comp == 4):
            print("Computer scored 4 Runs...","Total Score = ",Score)
        if (comp == 5):
            print("Computer scored 5 Runs...","Total Score = ",Score)
        if (comp == 6):
            print("Computer scored 6 Runs...","Total Score = ",Score)
