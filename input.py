# Write a program to take a action from user for (+, -, *, /)
# Confirm from user to continue action Yes | No
# If user confirm Yes then user perform continue action else say good bye and close 

def performAction(act, num1, num2):
    if(act == '+'):
        output = num1+num2
        print(f"Sum of num1 and num2 is : {output}")
    elif(act == '-'):
        output = num1-num2
        print(f"Substraction of num1 and num2 is : {output}")
    elif(act == '*'):
        output = num1*num2
        print(f"Multiplication of num1 and num2 is: {output}")
    elif(act == '/'):
        if(num2 == 0):
            print("Cannot divided by Zero")
        else:
            output = num1/num2
            print(f"Dividation of num1 and num2 is : {output}")
    else:
        print(f"{act} not a valid action")


while True:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    act = input("Choose action to perform (+, -, *, /) : ")
    performAction(act, num1, num2)
    
    while True:
        confirm = input("Are you sure want to continue (yes/no):").lower()
        if confirm in ['yes', 'no']:
            break 
        else:
            print("Invalid Input, Please type 'yes' or 'no'.")

    if confirm =='no':
        print("Bye Bye. Thanks for visiting here")
        break
        


