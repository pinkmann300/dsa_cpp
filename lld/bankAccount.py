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
        


"""
Design Library Book Class
Problem: Create a Book class for a library management system.

Requirements:

Fields: title, author, isbn, isAvailable
Constructor that initializes all fields (book starts as available)
borrowBook(): marks book as unavailable if currently available, returns success/failure
returnBook(): marks book as available
displayInfo(): prints book details including availability status

"""

class Book: 
    def __init__(self, title, author, isbn): 
        self.__title = title 
        self.__author = author 
        self.__isbn = isbn 
        self.__isAvailable = True 

    def borrowBook(self): 
        if self.__isAvailable: 
            self.__isAvailable = False 
            return True 
        else: 
            return False
        
    def returnBook(self): 
        self.__isAvailable = True  

    
    def displayInfor(self): 
        print("Title : ", self.__title) 
        print("Author: ", self.__author) 
        print("ISBN: ", self.__isbn) 
        print("Availability: ", self.__isAvailable)
