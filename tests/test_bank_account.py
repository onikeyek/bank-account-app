import unittest
from datetime import datetime 
from app.bank_account import BankAccount 

class TestBankAccount(unittest.TestCase):
  def setUp(self):
    self.account = BankAccount("TestUser", "EUR")

  def test_deposit(self):
    self.account.deposit(100)
    self.assertEqual(self.account.balance, 100.0)
  
  def test_withdraw(self):
    self.account.deposit(100)
    self.account.withdraw(40)
    self.assertEqual(self.account.balance, 60.0)
  
  def test_overdraft(self):
    self.account.withdraw(50)
    self.assertEqual(self.account.balance, 0.0)

  def test_currency_conversion(self):
    self.account.deposit(100)
    self.account.convert_currency("USD", 0.87)
    self.assertEqual(self.account.currency, "USD")
    self.assertAlmostEqual(self.account.balance, 110.0)

if __name__ == "__main__":
  unittest.main()