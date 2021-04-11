class Budget:
    """
    This is a budget class. You can instatiate various objects as categories
    and have them all interact with each other
    You instantiate the categories by adding an amount and a name

    """

    # the init function defines the default value for amount as zero and category name as others
    def __init__(self, amount=0, name='others'):
        self.name = name
        self.amount = amount
        
    # the deposit function takes an amount from the user and adds same to their current balance
    def deposit(self):
        try:

            deposit_amount = int(input("Please enter an amount to deposit for %s\n" % self.name))
            self.amount += deposit_amount
            self.check_balance()

        except ValueError:
            print('Please enter amount in figures')
            self.deposit()

    # the withdraw function withdraws a user defined sum from their available balance and updates the category amount
    def withdraw(self, withdrawal_amount=0):
        if withdrawal_amount  == 0:
            try:
                withdrawal_amount = int(input("Please enter amount to withdraw\n"))
                if self.amount - withdrawal_amount >= 0:
                    self.amount -= withdrawal_amount
                else:
                    print("Insuffienct funds. Please try again")
                    self.withdraw()
            
            except ValueError:
                print('Please enter amount in figures')
                self.withdraw()

        
        elif withdrawal_amount > 0:
            if self.amount - withdrawal_amount >= 0:
                self.amount -= withdrawal_amount
                return withdrawal_amount
            else:
                print("Insufficient funds. Please try again")
                return 0

    # the check balance fuction checks the category balance and prints same
    def check_balance(self):
        print("Your available balance for %s is %s" % (self.name, self.amount))

    # the transfer function transfers a user defined amount from another category and deposit same to the new category
    def transfer_from(self, category):
        transfer_amount = int(input("Please enter amount to transfer from %s\n" % category.name))
        try:
            if transfer_amount > 0:
                received_amount = category.withdraw(transfer_amount)
                if received_amount > 0:
                    self.amount += received_amount
                
                else:
                    self.transfer_from(category)
            
            else:
                print('Enter an amount greater than zero')
                self.transfer_from(category)
        except ValueError:
            print('Please enter amount in figures')
            self.transfer_from(category)

    # the change name category changes the name of the category to a new name defined by the user
    def change_name(self):
        name_change = input('Enter new name for this category\n')
        self.name = name_change

food = Budget(10000, 'food')
cloth = Budget(50000, 'clothing')
food.transfer_from(cloth)
food.check_balance()
cloth.check_balance()
#cloth.change_name()
#cloth.check_balance()

cloth.deposit()