"""
Design Bank Account Class
Problem: Create a BankAccount class that manages a simple bank account with deposit, withdrawal, and balance checking functionality.

Requirements:

Fields: accountNumber, ownerName, balance
Constructor that initializes the account with owner name and account number (balance starts at 0)
deposit(amount): adds money to balance (only positive amounts)
withdraw(amount): removes money if sufficient balance exists, returns success/failure
getBalance(): returns current balanc
"""

class BankAccount: 
    def __init__(self, ownerName, accountNumber): 
        self.__ownerName = ownerName 
        self.__accountNumber = accountNumber 
        self.__balance = 0 
    
    def getBalance(self): 
        return self.__balance
    
    def deposit(self, amount): 
        if amount > 0: 
            self.__balance += amount 
        else: 
            print("Deposit amount must be positive")

    def withdraw(self, amount): 
        if self.__balance >= amount: 
            self.__balance -= amount
            return True
        else: 
            print("Insufficient Funds") 
            return False 
        
