# A simple Banking Program


def check_balance(balance):
    print(f"Your Balance is {balance}")

def deposit():
    depo = float(input("Enter the amount you want to deposit:- "))

    if depo < 0:
        print("Deposit can't be lesser 0")
        return 0
    else:
        return depo


def withdraw(balance):
    withdr = float(input("Enter the amount you want to withdraw :- "))

    if withdr > balance :
        print("Withdraw amount should be greater than balance")
    elif withdr < 0:
        print("Withdraw amount cant be less than 0")
    else:
        return withdr


def main():

    is_running = True
    balance = 0

    while is_running:
        option1 = print("1. Check Balance")
        option2 = print("2. Make a deposit")
        option3 = print("3. Make a Withdrawal")
        option4 = print("4. Exit")
        option = input('Enter an Option: ')

        if option == '1':
            check_balance(balance)
        elif option == '2':
            balance += deposit()
        elif option == '3':
            balance -= withdraw(balance)
        elif option == '4':
            print("Thank You!!!")
            is_running = False
        else:
            print("Enter a Valid Option")


if __name__ == '__main__' :
    main()


