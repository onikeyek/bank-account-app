from bank_account import BankAccount

#Create a new account
#account = BankAccount("Ope", "Euro")

#Deposit
##account.deposit(150)

#withdrawal
#account.withdraw(40)

#check balance
#print(f"Current Balance: {account.get_balance()} {account.currency}")

#transaction history
#account.show_transaction_history()

"""#load existing account
account = BankAccount.load_from_file("ope")
if not account:
  account = BankAccount("ope", "Euro")
  print("New account created")

#Test
account.deposit(200)
account.withdraw(60)

#print history
account.show_transaction_history()
print(f"Final Balance: {account.get_balance()} {account.currency}")

#data to file
account.save_file()
"""
"""#creating new account
account12 = BankAccount("Sade", "USD")



#Print balance
print(f"New Account Balance: {account12.get_balance()} {account12.currency}")

#load existing account
account12 = BankAccount.load_from_file("Sade")
if not account12:
  account12 = BankAccount("Sade", "USD")

#deposit money
account12.deposit(1300)

#withdrawal
account12.withdraw(700)

#Another deposit made
account12.deposit(200)

#Check balance
print(f"Account Balance: {account12.get_balance()} {account12.currency}")

#Print account history 
account12.show_transaction_history()
print(f"Account Balance: {account12.get_balance()} {account12.currency}")

#Data to save
account12.save_file()

#Convert USD to Euro 1 USD is 0.87 Euro
account12.convert_currency("Euro", 0.87)

#generate bank statement
account12.generate_bank_statement()"""

#new account 
account13 = BankAccount("Farouk", "Euro")


#deposit money 
account13.deposit(20)

print(f"Account Balance: {account13.balance}  {account13.currency}")

#withdraw money 
account13.withdraw(5)

#deposited 
account13.deposit(100)


account13.show_transaction_history()
print(f"Final Balance: {account13.balance} {account13.currency}")
#data to file
account13.save_file()


#Currency conversion
#Convert USD to Euro 1 USD is 0.87 Euro
account13.convert_currency("USD", 1.15)

#generate account13 bankstatement 
account13.generate_bank_statement()


