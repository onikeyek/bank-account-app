from bank_account import BankAccount
#Create Account
account11 = BankAccount("paul", "Euro", 2345)
account12 = BankAccount("Farouk", "Euro", 2021)
account13 = BankAccount("ope", "Euro", 5412)
account14 = BankAccount("joanl", "USD", 9851)



#Deposit  & withdraw 
#ACCOUNT 11 TRANSACTION
account11.deposit(1000)
account11.withdraw(200)
account11.save_file()
#transaction history 
account11.show_transaction_history()
#print balance
print(f"Account Balance: {account11._balance} {account11.currency}")
#Convert Currency  Euro to USD is 1.15
account11.convert_currency("USD", 1.15)
#Generate bank statement 
account11.generate_bank_statement()



#ACCOUNT 13 TRANSACTION
account13.deposit(200)
#save 
account13.save_file()
#print balance 
print(f"Account Balance: {account13._balance} {account13.currency}")
#More deposit
account13.deposit(100)
#generate bank statement 
account13.generate_bank_statement()




#ACCOUNT 12 TRANSACTION
account12.deposit(20)
print(f"Account Balance: {account12.balance}  {account12.currency}")
#withdraw money 
account12.withdraw(5)
#deposited 
account13.deposit(100)
account13.show_transaction_history()
print(f"Final Balance: {account12.balance} {account12.currency}")
#data to file
account12.save_file()
#Currency conversion
#Convert USD to Euro 1 USD is 0.87 Euro
account12.convert_currency("USD", 1.15)
#generate account13 bankstatement 
account12.generate_bank_statement()


#ACCOUNT 14 TRANSACTION
#deposit money 
account14.deposit(20000)
print(f"Account Balance: {account14.balance}  {account14.currency}")
#withdraw money 
account14.withdraw(5000)
#deposited 
account14.deposit(10000)
account14.show_transaction_history()
print(f"Final Balance: {account14.balance} {account14.currency}")
#data to file
account14.save_file()


