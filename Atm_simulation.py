#welcome message
print("Welcome to the AMS ATM")

balance = 1000;

user_pin = '1234'

user_input = input("Please enter your pin number: ")


if (user_input != user_pin):
    atm_on = False;
    print("Incorrect pin. Please try again.")
else:
    atm_on = True;
    print("Welcome!")

while(atm_on):
    print("\nChoose an option:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if (choice == 1):
        print("Your current balance is: ", balance)

    elif (choice == 2):
        deposit = int(input("Please enter how much you would like to deposit: "))
        if (deposit < 0):
            print("Invalid deposit amount.")
        else:
            balance += deposit
            print("Deposit successful. Your new balance is: ", balance)
    
    elif (choice == 3):
        withdrawal = int(input("Please enter how much you would like to withdraw: "))
        if (withdrawal < 0 or withdrawal > balance):
            print("Invalid withdrawal amount.")
        else:
            balance -= withdrawal
            print("Withdrawal successful. Your new balance is: ", balance)
    elif (choice == 4):
        print("Thank you for using the ATM. Goodbye!")
        atm_on = False
    else:
        print("Invalid Choice")