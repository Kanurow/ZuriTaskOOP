# We assumed total income is #300,000 which will be distributed between categories in our budget
# Food is #150,000
# Clothing is #100,000
# Entertainment is #50,000

#Budget was made for Mr Rowland

class Budget:
    def __init__ (self, category, opening_balance ):
        self.category = category
        self.opening_balance = opening_balance


        
    def welcome(self):
        print('=== Welcome Mr Rowland ===')
        print('==Your Favourite Budget Management App==')
        print('Select category \n a- Food \n b- Clothing \n c- Entertainment')
        budget_choice = input()
        if budget_choice == 'a':
            food = Budget('Food', 150000)
            print('What do you wish to do under your food category')
            print('a- Deposit \n b- Withdrawal \n c- Tansfer \n d- Check Balance')
            action_choice = input('Enter choice here \n')
            if action_choice == 'a':
                print('==== DEPOSIT ====')
                print(food.deposit())
            elif action_choice == 'b':
                print('==== WITHDRAWAL ====')
                print(food.withdraw())
            elif action_choice == 'c':
                print('==== TRANSFER ====')
                print(food.transfer())
            elif action_choice == 'd':
                print('==== CHECK ACCOUNT BALANCE ====')
                print(food.check_balance())
            else:
                print('Your input is invalid, please retry')
        elif budget_choice == 'b':
            clothing = Budget('Clothing', 100000)
            print('What do you wish to do under your clothing category')
            print('a- Deposit \n b- Withdrawal \n c- Tansfer \n d- Check Balance')
            action_choice = input('Enter choice here \n')
            if action_choice == 'a':
                print('==== DEPOSIT ====')
                print(clothing.deposit())
            elif action_choice == 'b':
                print('==== WITHDRAWAL ====')
                print(clothing.withdraw())
            elif action_choice == 'c':
                print('==== TRANSFER ====')
                print(clothing.transfer())
            elif action_choice == 'd':
                print('==== CHECK ACCOUNT BALANCE ====')
                print(clothing.check_balance())
            else:
                print('Your input is invalid, please retry')
                
        elif budget_choice == 'c':
            entertainment = Budget('Entertainment', 50000)
            print('What do you wish to do under your entertainment category')
            print('a- Deposit \n b- Withdrawal \n c- Tansfer \n d- Check Balance')
            action_choice = input('Enter choice here \n')
            if action_choice == 'a':
                print('==== DEPOSIT ====')
                print(entertainment.deposit())
            elif action_choice == 'b':
                print('==== WITHDRAWAL ====')
                print(entertainment.withdraw())
            elif action_choice == 'c':
                print('==== TRANSFER ====')
                print(entertainment.transfer())
            elif action_choice == 'd':
                print('==== CHECK ACCOUNT BALANCE ====')
                print(entertainment.check_balance())
            else:
                print('Your input is invalid, please retry')
    def deposit(self):
        try:
            deposit_amount = int(input(f'How much do you want to deposit or increase your {self.category} budget with? \n'))
            if deposit_amount > 0:
                valid_response = False
                print(f' You deposited {deposit_amount} into your {self.category} budget')
                print(f' Your new balance is {deposit_amount + self.opening_balance}')
                another_transaction = input('Do you wish to perform another transaction? \n a- yes \n b- no \n ')
                if another_transaction == 'a':
                    Budget.welcome(welcome)
                else:
                    print('Have a nice day')
        except Exception:
            print('Error!!! \n You are to enter a positive integer')
    def withdraw(self):
        valid_response = True
        while valid_response == True:
            try:
                withdrawal_amount = int(input(f'How much do you want to withdraw from your {self.category} category? \n'))
                if withdrawal_amount > 0:
                    valid_response = False
                    print(f'You withdrew {withdrawal_amount} \n New balance is {self.opening_balance - withdrawal_amount}')
                    another_transaction = input('Do you wish to perform another transaction? \n a- yes \n b- no \n ')
                    if another_transaction == 'a':
                        Budget.welcome(welcome)
                    else:
                        print('Have a nice day')
            except Exception:
                print('Error!!! \n You are to enter a positive integer')
    def transfer(self):
        valid_response = True
        while valid_response == True:
            try:
                print('Which account do you wish to make transfers into')
                option_selected = input('a- Food \n b- Clothing \n c- Entertainment \n')
                if option_selected == 'a':
                    transfer_amt = int(input('You are transfering into food category \n Enter transfer amount \n '))
                    print(f'You tansfered {transfer_amt} into food category \n new balance is {transfer_amt + food.opening_balance}')
                    valid_response = False
                    another_transaction = input('Do you wish to perform another transaction? \n a- yes \n b- no \n ')
                    if another_transaction == 'a':
                        Budget.welcome(welcome)
                    else:
                        print('Have a nice day')
                elif option_selected == 'b':
                    transfer_amt = int(input(' You are transfering into clothing category \n Enter transfer amount \n '))
                    print(f'You tansfered {transfer_amt} into clothing category \n new balance is {transfer_amt + clothing.opening_balance}')
                    valid_response = False
                    another_transaction = input('Do you wish to perform another transaction? \n a- yes \n b- no \n ')
                    if another_transaction == 'a':
                        Budget.welcome(welcome)
                    else:
                        print('Have a nice day')
                elif option_selected == 'c':
                    transfer_amt = int(input(' You are transfering into Entertainment category \n Enter transfer amount \n '))
                    print(f'You tansfered {transfer_amt} into entertainment category \n new balance is {transfer_amt + entertainment.opening_balance}')
                    valid_response = False
                    another_transaction = input('Do you wish to perform another transaction? \n a- yes \n b- no \n ')
                    if another_transaction == 'a':
                        Budget.welcome(welcome)
                    else:
                        print('Have a nice day')
                else:
                    print('Invalid option, please retry')
            except Exception:
                print('invalid option selected') 
    def check_balance(self):
        print(f'Your opening balance for {self.category} is {self.opening_balance} ')
        another_transaction = input('Do you wish to perform another transaction? \n a- yes \n b- no \n ')
        if another_transaction == 'a':
            Budget.welcome(welcome)
        else:
            print('Have a nice day')


#Income Distribution amongst categories
welcome = Budget('Welcome', 0)
food = Budget('Food', 150000)
clothing = Budget('Clothing', 100000)
entertainment = Budget('Entertainment', 50000)


Budget.welcome(welcome)
