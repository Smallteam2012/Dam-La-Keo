from random import randint

def logic():
    score_p = 0
    score_c = 0
    print("Nhap Dam, La, Keo:")
    player = input()
    computer = randint(0, 2)


    if computer == 0:
        computer = "Dam"
    if computer == 1:
        computer = "La"
    if computer == 2 :
        computer == "keo"

    print("---")
    print("Player choose:", player)
    print("Computer choose:", computer)
    print("---")

    if player == computer:
        print("Draw\n")
    else :
        if player == "Keo":
            if computer == "Dam":
                score_c+=1
                print("COMPUTER WIN!\n")
            else:
                score_p += 1
                print("PLAYER WIN!\n")
        elif player == "Dam":
            if computer == "La":
                score_c+=1
                print("COMPUTER WIN!\n")
            else:
                score_p += 1
                print("PLAYER WIN!\n")
        elif player == "La":
            if computer == "Dam":
                score_c+=1
                print("COMPUTER WIN!\n")
            else:
                score_p += 1
                print("PLAYER WIN!\n")

        else:
            print("Nhap sai! =)")
    print("---")
    print("Your score is", score_p)
    print("Computer score is", score_c)
    if score_p > score_c:
        print("You win!+)")
    else:
        print("You lose!-(")
    print("---")

print("Nhap so lan choi")
d = int(input())

i = 1
while i <= d:
    logic()
    i+=1;