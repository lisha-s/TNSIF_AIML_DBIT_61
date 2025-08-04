#Build a simple ATM simulation. User must: Enter correct PIN (e.g., 1234) Can perform withdraw, deposit, or check balance
#Only 3 attempts allowed for PIN 

pin = "1234"
balance = 1000
tries = 0
while tries < 3:
    user_pin = input("Enter PIN: ")
    if user_pin == pin:
        print("Welcome!")
        break
    else:
        tries += 1
        print("Wrong PIN")

if tries == 3:
    print("Account locked.")
else:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose (1-4): ")

        if choice == "1":
            print("Balance: ₹", balance)

        elif choice == "2":
            amount = float(input("Amount to deposit: ₹"))
            balance += amount
            print("Money deposited.")

        elif choice == "3":
            amount = float(input("Amount to withdraw: ₹"))
            if amount <= balance:
                balance -= amount
                print("Money withdrawn.")
            else:
                print("Not enough balance.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")