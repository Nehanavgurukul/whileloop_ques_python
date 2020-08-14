num=int(input("enter value"))
i=2
while(i<num):
    if(num%i==0):
        print("it is not prime")
        break
    i=i+1
else:
    print("it is prime")