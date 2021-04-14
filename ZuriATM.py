database = {}

import random

def generate_account_number():
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7']
    row_bank_of_africa_account_number = ('1' + '3' + random.choice(num_list) + random.choice(num_list) + random.choice(num_list) + random.choice(num_list) + random.choice(num_list) + random.choice(num_list) + random.choice(num_list) + random.choice(num_list))
    row_bank_of_africa_account_number = int(row_bank_of_africa_account_number)
    return row_bank_of_africa_account_number
def login():
    print('*** Login ***')
    email_address = input('Enter Your Email \n')
    password_from_user = input('What is your password \n')
    for account_number, user_info in database.items():
        if email_address == user_info[1] and password_from_user == user_info[2]:
            print('Login Successful')
            print(f' Welcome, {user_info[0]} {user_info[5]}')
            bank_operations()
        else:
            print('Wrong log in details')
def register():
    print('*** Registration ***')
    email = input('What is your email address\n')
    first_name = input('Enter first name \n')
    last_name = input('Enter last name\n')
    middle_name = input('Enter other names\n')
    gender = int(input('Gender \n 1- Male \n 2- Female \n 3- Others (Please, specify) \n'))
    correctOption = True
    while correctOption == True:
        if gender == 1:
            print('Male selected')
            correctOption = False
        elif gender == 2:
            print('Female selected')
            correctOption = False
        elif gender == 3:
            different_gender = input('Type in gender of choice \n')
            print(f'{different_gender} Selected')
            correctOption = False
        else:
            print(' Please, select option 1, 2 or 3')
            gender = int(input('Gender \n 1- Male \n 2- Female \n 3- Others (Please, specify) \n'))

    marital_status = input('Marital Status \n a- Single b- Married c- Divorced \n')
    correct_status = True
    while correct_status == True:
        if marital_status == 'a':
            print('Single selected')
            correct_status = False
        elif marital_status == 'b':
            print('Married selected')
            correct_status = False
        elif marital_status == 'c':
            print('Divorced Selected')
            correct_status = False
        else:
            print(' Please, select option a, b or c')
            marital_status = input('Marital Status \n a- Single b- Married c- Divorced \n')
    phone_number = int(input('Enter your phone number? \n'))
    bvn = int(input('Enter your BVN \n'))
    password = input('Enter password \n')
    account_number = generate_account_number()
    # BVN is considered to be unique to each individual so we used it as our key  
    database[bvn] = [first_name, email, password, account_number, phone_number, last_name, middle_name]
    print('Your account has been created')
    print('================')
    print(f'Hello {first_name} {last_name} \n Your account number is {account_number}')
    print(f'Please, keep it safe')
    print("THANKS FOR CHOOSING US \n <==Row bank of Africa==> \n You can now log into your account")
    login()

# Below is account details in our database which can be used in making transfers
def bank_operations():
    row_bank_users_acnt_num = [139800, 139801, 139802, 139803]
    row_bank_users_acnt_name = ['Rowland Kanu', 'Samuel Kanu', 'Kenneth Kanu', 'Ugbo Chima']

    gt_bank_users_acnt_num = [337688, 338787]
    gt_bank_users_acnt_name = ['James Obi', 'John Obi']

    uba_bank_users_acnt_num = [774565, 775345]
    uba_bank_users_acnt_name = ['David Obi', 'Gabriel James']

    print('How can we help you?')
    print('1- Withdrawal \n 2- Cash Deposit \n 3- Transfer \n 4- Contact Customer Care')
    action_selected = int(input('Select one option \n'))
    if (action_selected) == 1:
        print('====Withdrawal====')
        withdrawal_choice = input(
            'INSTANT WITHDRAWAL OPTION \n a- 1000 \n b- 5000 \n c- 10000 \n d- 20000 \n e- Enter Amount of Choice \n')
        if withdrawal_choice == 'a':
            print('Amount withdrawn \n #1,000')
            print('Take Cash')
            another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if another_transaction == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'b':
            print('Amount withdrawn \n #5,000')
            print('Take Cash')
            another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if another_transaction == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'c':
            print('Amount withdrawn \n #10,000')
            print('Take Cash')
            another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if another_transaction == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'd':
            print('Amount withdrawn \n #20,000')
            print('Take Cash')
            another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if another_transaction == 'a':
                bank_operations()
            else:
                exit
        elif withdrawal_choice == 'e':
            print('Withdraw in units of #500 only \n Example: 2000, 4500 etc')
            newAmount = int(input('**Enter Amount** \n'))
            availableBalance = newAmount % 500
            if availableBalance == 0:
                print('Successful \n Please Take Your Cash')
                print(f'Total Withdrwal is # {newAmount}')
                another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                if another_transaction == 'a':
                    bank_operations()
                else:
                    exit
            else:
                print('Wrong, input. \n Please retry')
        else:
            print('Wrong input')
    elif (action_selected == 2):
        print('====Cash Deposit====')
        deposit_acnt = int(input('Enter Account Number \n'))
        if deposit_acnt in Row_bank_users_acnt_num:
            correct_user = Row_bank_users_acnt_num.index(deposit_acnt)
            deposit_validation = input(
                f'You are depositing into {Row_bank_users_acnt_name[correct_user]} account. \n a- continue \n b- wrong account \n')
            if answer == 'a':
                amount_in = int(input('Enter amount \n'))
                print(f' SUCCESSFUL \n You have credited {Row_bank_users_acnt_name[correct_user]} with #{amount_in}')
                another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                if another_transaction == 'a':
                    bank_operations()
                else:
                    exit
            elif answer == 'b':
                print('Please enter correct account')
            else:
                print('Invalid input')
        else:
            print('Invalid account number, please retry')
    elif (action_selected == 3):
        print('====Transfer====')
        bank_of_choice = input('a- Transfer to own bank \n b- Transfer to other banks \n')
        if bank_of_choice == 'a':
            row_acnt_num = int(input('Enter the Row Bank of Africa account number \n'))
            if row_acnt_num in row_bank_users_acnt_num:
                valid_user = row_bank_users_acnt_num.index(row_acnt_num)
                transfer_validation = input(
                    f'You are transfering into {row_bank_users_acnt_name[valid_user]} account. \n a- continue \n b- wrong account \n')
                if transfer_validation == 'a':
                    amount_trans = int(input('Enter amount \n'))
                    print(
                        f' SUCCESSFUL \n You have transfered #{amount_trans} to {row_bank_users_acnt_name[valid_user]}')
                    another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                    if another_transaction == 'a':
                        bank_operations()
                    else:
                        exit
                elif transfer_validation == 'b':
                    print('Re-enter account number')
                else:
                    print('Invalid input')

            else:
                print('Invalid account number')
        elif bank_of_choice == 'b':
            other_bank_options = input('a- UBA \n b- Gt Bank \n')
            if other_bank_options == 'a':
                uba_acnt_no = int(input('Enter UBA account number \n'))
                if uba_acnt_no in uba_bank_users_acnt_num:
                    valid_uba = uba_bank_users_acnt_num.index(uba_acnt_no)
                    uba_validation = input(
                        f'You are transfering into {uba_bank_users_acnt_name[valid_uba]} account. \n a- continue \n b- wrong account \n')
                    if uba_validation == 'a':
                        uba_trans_amount = int(input('Enter amount \n'))
                        print(
                            f' SUCCESSFUL \n You have transfered #{uba_trans_amount} to {uba_bank_users_acnt_name[valid_uba]}')
                        another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                        if another_transaction == 'a':
                            bank_operations()
                        else:
                            exit


                    elif uba_validation == 'b':
                        print('Please reconfirm account number')
                    else:
                        print('Invalid input')

                else:
                    print('Enter a valid account number')

            elif other_bank_options == 'b':
                gt_bank_acnt_no = int(input('Enter Gt bank account number \n'))
                if gt_bank_acnt_no in gt_bank_users_acnt_num:
                    valid_gt = gt_bank_users_acnt_num.index(gt_bank_acnt_no)
                    gt_validation = input(
                        f'You are transfering into {gt_bank_users_acnt_name[valid_gt]} account. \n a- continue \n b- wrong account \n')
                    if gt_validation == 'a':
                        gt_trans_amount = int(input('Enter amount \n'))
                        print(
                            f' SUCCESSFUL \n You have transfered #{gt_trans_amount} to {gt_bank_users_acnt_name[valid_gt]}')
                        another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
                        if another_transaction == 'a':
                            bank_operations()
                        else:
                            exit
                    elif gt_validation == 'b':
                        print('Please reconfirm account number')

                else:
                    print('Enter a valid account number')
        else:
            print('Invalid option')

    elif (action_selected == 4):
        print('====Contact Customer Care====')
        contact_care = input(
            'a- Frequently asked questions \n b- Send a type in your complaint \n c- Speak to a customer care representative \n')
        if contact_care == 'a':
            options = input(
                'i. How to create an account \n ii. forgot password \n iii. unsuccessful transaction but got debited \n')
            if options == 'i' or 'ii' or 'iii':
                print('Please Visit: www.bankhelpwebpage.com')
            else:
                print('Invalid option')

        elif contact_care == 'b':
            complaint_msg = input('Type in your complaint \n')
            print('WE have received your complaint')
            another_transaction = input('Do you want to perform another transaction \n a- yes \n b- no \n')
            if another_transaction == 'a':
                bank_operations()
            else:
                exit
        elif contact_care == 'c':
            print('You are now being connected to a customer care representative')
            print('Connecting...')
        else:
            print('Wrong option selected')


    else:
        print('Wrong Option \n Please Retry')


def initialize():
    valid_option = False
    print('Welcome to Row bank of Africa')
    while valid_option == False:
        try:
            # while valid_option == False:
            have_account = int(input('Do you have account with us: \n 1- Yes. 2- No \n'))
            if have_account == 1:
                valid_option = True
                print('You can now log in')
                # These are accounts already existing in the banks data base with there log in details
                # And my banks account details always starts with 13, thats why the random code always starts with 13
                row_users_acnt_num = [139800, 139801, 139802, 139803]
                row_users_pass = [123, 456, 789, 987]
                ac_number = int(input('Enter Account Number \n'))

                if ac_number in row_users_acnt_num:
                    ac_password = int(input('Enter Password \n'))
                    if row_users_acnt_num.index(ac_number) == row_users_pass.index(ac_password):
                        bank_operations()
                    else:
                        print('Password incorrect')

                else:
                    print('Invalid Account Number')


            elif have_account == 2:
                valid_option = True
                print('Please fill in your details')
                register()
                #login()
            else:
                print('Invalid input')
        except Exception as e:
            print('Please, enter an integer', e)


initialize()
