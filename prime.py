print("prime number")
no=int(input("enter a number to check for prime"))

for i in range(2,no):
    if(no%i==0):
        print("enter a number is prime")
        break
    else:
        print("enter a number is not a prime")
        
