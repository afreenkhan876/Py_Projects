# This is a program for Prime number.
# Take input from user.
n=int(input("Enter a number:"))
if n<=1:
    print("You entered wrong number")
else:
    for i in range(2,int(n**0.5)+1):
        if n%2==0:
            print("This is not a prime number.")
            break 
    else:
        print("This is a prime number.")       
            