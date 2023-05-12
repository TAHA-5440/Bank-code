

def login():
    username = input("USERNAME :  ")
    password = input("Enter Your Pin :  ")

    with open("C:\\Users\\tahaa\\OneDrive\\Desktop\\BANK DATA\\accounts.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            if parts[0] == username and parts[1] == password:
                # Open the corresponding text file for the user
                filename = username + ".txt"
                filepath = "C:\\Users\\tahaa\\OneDrive\\Desktop\\BANK DATA\\" + filename
                return filepath
        print("INVALID PASSWORD OR USERNAME")
        return None


def cash_deposit(filepath):
    user_cash = int(input("Enter the amount of cash : "))
    with open(filepath, "r") as f:
        old_cash = int(f.read())
    total = user_cash + old_cash
    if user_cash > 0:
        with open(filepath, "w") as f:
            f.write(str(total))
        print("TOTAL BALANCE AVAILABLE :", total)
    else:
        print("illegal amount")


def cash_withdraw(filepath):
    user_cash = int(input("Enter the amount of cash : "))
    with open(filepath, "r") as f:
        old_cash = int(f.read())
    user_cash = abs(user_cash)
    if old_cash > user_cash:
        total = old_cash - user_cash
        with open(filepath, "w") as f:
            f.write(str(total))
        print("TOTAL BALANCE REMAINING :", total)
    else:
        print("insufficient balance")


def check_balance(filepath):
    with open(filepath, "r") as f:
        old_cash = int(f.read())
    print("YOUR CURRENT BALANCE = ", old_cash)


def signup():
    newusername = input("USERNAME : ")
    newpassword = input("CREATE A PASSWORD : ")
    with open("C:\\Users\\tahaa\\OneDrive\\Desktop\\BANK DATA\\accounts.txt", "a") as f:
        f.write(f"{newusername},{newpassword}\n")  # Write the username and password separated by a comma
    filename = newusername + ".txt"
    with open("C:\\Users\\tahaa\\OneDrive\\Desktop\\BANK DATA\\" + filename, "w") as file:
        file.write("0")
    print("YOUR ACCOUNT HAS BEEN CREATED")


def main():
    print("Welcome to HBL ")
    login_type = input("Do You Want To LOG IN OR SIGN UP : ").upper().replace(" ", "")
    if login_type == "LOGIN":
        filepath = login()
        if filepath is not None:
            cash_type = input("CHOOSE FROM THE FOLLOWING  \n 1.CASH DEPOSIT\n 2.CASH WITHDRAW\n 3.CHECK BALANCE  \n ")
            cash_type = cash_type.upper().replace(" ", "")
            if cash_type == "1":
                cash_deposit(filepath)
            elif cash_type == "2":
                cash_withdraw(filepath)
            elif cash_type == "3":
                check_balance(filepath)
    elif login_type == "SIGNUP":
        signup()
    else:
        print("INVALID INPUT")


if __name__ == "__main__":
    main()
