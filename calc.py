def get_numbers():
    x=int(input("enter first number;"))
    y=int(input("enter second number;"))
    return x,y    # retrun a tuple (x,y)
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def main():
    # Call get_numbers() and unpack its result into x and y
    x,y=get_numbers()
    # Pass those into add() and capture the result
    print("for add choice 1:")
    print("for sub choice 2:")
    print("for mul choice 3:")
    print("for div choice 4:")
    ch=int(input("enter your choice which you want to operate:"))
    if ch==1:
        result=add(x,y)
        print(f"the sum of {x} and {y} is {result}")
    elif ch==2:
        result=sub(x,y)
        print(f"the sub of {x} and {y} is {result}")
    elif ch==3:
        result=mul(x,y)
        print(f"the mul of {x} and {y} is {result}")
    elif ch==4:
        result=div(x,y)
        print(f"the div of {x} and {y} is {result}")
    else:
        print("you entered wrong choice")
if __name__=="__main__":
    main()
