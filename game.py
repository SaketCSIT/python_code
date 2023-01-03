import random
num=random.randint(1,100)
attempt=5


while attempt:
    user_num=int(input("Enter Number 1 to 100\n"))
    print(f'Attempts Left {attempt}')
    attempt-=1
    if user_num==num:
        print("You Won")
        break
    elif user_num<num:
        print("to small")
    else:
        print("to large")
