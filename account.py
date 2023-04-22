# Author: Isai Rangel
# Date: 04-21-2023

class Account:
    """

    A class that creates a bank account and interacts with it
    """
    def __init__(self,name: str) -> None:
        """

        Function to set up account object for bank account
        :param name: Name of account holder
        :returns: Nothing
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """

        Method that deposits into an account
        :param amount: Value to be deposited
        :return: True if deposit was successful, False if unsuccessful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Method that withdraws from an account
        :param amount: Value to be withdrawn
        :return: True if withdraw was successful, False if unsuccessful
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Method to get the current balance on account
        :return:  Account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get person's name on account
        :return: Person's name on account
        """
        return self.__account_name
