class bank:
    def __init__(self, name, balance):
        """
        makes a bank acount with a name and a starting balance
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        this deposits a numerical amount above 0
        """
        if type(amount) != int:
            return False
        elif amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        this withdraws a numerical amount above 0 and below the total account balance
        """
        if type(amount) != int:
            return False
        elif 0 < amount <= self.balance and type(amount) == int:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        """
        this returns the balance
        """
        return self.balance

    def get_name(self):
        """
        this returns the account name
        """
        return self.name
