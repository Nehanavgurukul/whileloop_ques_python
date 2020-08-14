number=5
i=0
while(i<number):
    user_guess=int(input("enter number"))
    if(user_guess==number):
        print("hamara number guess ho gya hai")
        break
    i=i+1
else:
    print("user ne guess nhi kiya")