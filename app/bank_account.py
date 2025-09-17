import json
import os
import hashlib

from datetime import datetime

class BankAccount:
  def __init__(self, name, currency, pin_hash):
    self.name = name
    self.currency = currency #Account currency, Euro or USD
    self._balance = 0.0
    self.transactions = []  #To store each transaction as a dictionary
    self.pin_hash = pin_hash #Hashed version of pin

  def  __str__(self):
    return(f"Account Holder: {self.name}\n"
           f"Currency: {self.currency}\n"
           f"Balance: {self._balance:.2f}")
  
  @property
  def balance(self):
    return self._balance
  
  def deposit(self, amount):
    if amount <= 0:
      print("Dear Customer, Deposit must be greater than 0.")
      return
    
    self._balance += amount
    self.transactions.append({
      "type": "deposit",
      "amount": amount,
      "currency": self.currency,
      "timestamp": datetime.now().isoformat()
    })
    print(f"Deposited {amount:.2f} {self.currency}. New Balance: {self._balance:.2f}")
  
  def withdraw(self, amount):
    if amount <= 0:
      print("Dear customer, Withdrawal must be greater than 0.")
      return
    if amount > self.balance:
      print("Insufficient Balance!")
      return
    
    self._balance -= amount
    self.transactions.append({
      "type": "withdrawal", 
      "amount": amount,
      "currency": self.currency,
      "timestamp": datetime.now().isoformat()
    })
    print(f"Withdrew {amount:.2f} {self.currency}. New Balance: {self._balance:.2f}")
  
  def show_transaction_history(self):
    print(f"\n Transaction history for {self.name}:")
    if not self.transactions:
      print("No transaction yet.")
      return
    for tx in self.transactions:
      print(f"- {tx['timestamp']} | {tx['type']} | {tx['amount']} {tx['currency']}")
  #Save account data to a JSON file.
  def save_file(self):
    data = {
      "name" : self.name, 
      "currency": self.currency,
      "balance": self._balance,
      "transaction": self.transactions,
      "pin_hash": self.pin_hash
    }
     #Saving in folder accounts
    os.makedirs("accounts", exist_ok=True)
   
    filename = f"{self.name.lower()}_accounts.json"
    with open(filename, "w") as f:
      json.dump(data, f, indent=4)
    print(f"Account saved to {filename}")

  @staticmethod
  def load_from_file(name, entered_pin):
    filename = os.path.join("accounts", f"{name.lower()}_accounts.json")

    if not os.path.exists(filename):
      print(f"No saved account found for {name}.")
      return None
    
    with open(filename, "r") as f:
      data = json.load(f)

      entered_hash = hashlib.sha256(entered_pin.encode()).hexdigest()
      if entered_hash != data.get("pin_hash"):
        print("Incorrect PIN. Access Denied.")
        return None

    
      account = BankAccount(data["name"], data["currency"])
      account._balance = data["balance"]
      account.transactions = data["transaction"]
      return account
  
  #Currency conversion 
  """Args:
     target_currency (str): Currency to convert to rate (float): 
     Exchange rate to use
  """
  def convert_currency(self, target_currency, rate):
    if self.currency == target_currency:
      print("Account is already in ", target_currency)
      return
    
  #convert balance
    converted_amount = self._balance * rate
    old_currency = self.currency
  
  #Update account
    self._balance = round(converted_amount, 2)
    self.currency = target_currency

  #Log transaction
    self.transactions.append({
      "type" : "currency_conversion", 
      "from_currency" : old_currency,
      "to_currency": target_currency,
      "rate": rate,
      "new_balance": self._balance,
      "timestamp": datetime.now().isoformat()})
    
    print(f"Converted Account {old_currency} to {target_currency} at rate {rate}.")
    print(f"New Balance: {self._balance:.2f} {self.currency}")

#Bank statement generator
  def generate_bank_statement(self):
      print("\n BANK STATEMENT") #print a formatted bank statement for transactions.
      print("=" * 30)
      print(f"Accout Holder: {self.name}")
      print(f"Account Currency: {self.currency}")
      print(f"Current Balance: {self._balance:.2f} {self.currency}")
      print("-" * 30)
      print("Transaction:")
      if not self.transactions:
        print("No Transaction yet.")
        return
      for  tx in self.transactions:
        timestamp = tx.get("timestamp", "N/A")
        tx_type = tx.get("type", "unknown")
      
      if tx_type in ["deposit", "withdrawal"]:
        print(f"{timestamp} | {tx_type.capitalize():<10} | {tx['amount']} {tx['currency']}")
      elif tx_type == "currency_conversion":
        print(f"{timestamp} | Converted from  {tx['from_currency']} to {tx['to_currency']} @ rate {tx['rate']}, New Balance: {tx['new_balance']}")
      
      print("=" *30)

