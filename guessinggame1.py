number=5
i=0
while(i<10):
    user_guess=int(input("number enter kro "))
    if(user_guess==number):
        print("waah! guess kr liya")
        break
    elif(user_guess>number):
        print("number bada hai,fir try kro")
    else:
        print("number chhota hai,fir try kro")
    i=i+1
