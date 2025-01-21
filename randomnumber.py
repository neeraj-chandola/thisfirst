import random
number= random.randint(1,10)
count = 0
while count<5:
    useri=int(input("Enter your guess"))
    if useri== number:
        count+=1
        print(F"you guess it correct in {count} guess")
        print(count)
        break
    elif useri < number:
        print("guess a greater number")
        count+=1
        print(count)
    elif count<5:
        print(f"the guess are end the number is {number}")
    else :
        count+=1
        print(count)
        print("guess a smaller number")
