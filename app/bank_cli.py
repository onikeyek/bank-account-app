from bank_account import BankAccount
import hashlib
def main():
  print("Welcome to JKLEO BANK")
  pin = input("Set a 4-digit PIN: ")
  pin_hash = hashlib.sha256(pin.encode()).hexdigest()
  name = input("Enter account holder name: ").strip()
  account = BankAccount.load_from_file(name, pin_hash)
  if account: 
    #Verify PIN
    if not account.verify_pin(pin):
      print("Incorrect PIN. Access Denied.")
      return
    else:
      print(f"Welcome back, {account.name}!")
  else:
    print("Account does not exist.Please contact customer service.")
    return
    

  while True:
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3.View Account Balance")
    print("4. Generate Bank statement")
    print("5. Exist")
   
    choice = input("Enter choice (1-5):")

    if choice == "1":
      amount = float(input("Enter deposit amount: "))
      account.deposit(amount)

    elif choice == "2":
      amount = float(input("Enter Withdrawal amount: "))
      amount.withdraw(amount)

    elif choice == "3":
     account.show_transaction_history()

    elif choice == "4":
      account.generate_bank_statement()

    elif choice == "5":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Try again.")

if __name__ == "__main__":
  main()