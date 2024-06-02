transactions = {}

class BankAccount:
    def __init__(self,account_number, holder_name, password):
        self.account_number = account_number
        self.holder_name = holder_name
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankTransaction.add_transaction(self.account_number,['Deposited', amount])
            print('Amount deposited.')
        else:
            'Invalid input!'

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            BankTransaction.add_transaction(self.account_number,['Withdrew', amount])
            print('Amount withdrawn.')
        elif amount > self.balance:
            print('Insufficient! funds')
        else:
            print('Invalid input!')
    def show_info(self):
        return f'Account number : {self.account_number} \nHolder name : {self.holder_name} \nBalance : {self.balance}'


class BankSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, holder_name, password):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankSystem(account_number, holder_name, password)
            BankTransaction.add_account(account_number)
            print('Account created successfully')
        else:
            return 'Account already exists!.'

    def login(self, account_number, password):
        account_number = int(input('Enter your account number : '))
        password = input('Enter your password : ')
        account = self.accounts.get(account_number)
        if account and account.password == password:
            print('Login Successfull!')
        else:
            return 'Invalid! account number or password.'


class BankTransaction:

    @staticmethod
    def add_account(account_number):
        if account_number not in transactions:
            transactions[account_number] = []
        else:
            print('Account already exists')

    @staticmethod
    def add_transaction(accout_number, details):
        if accout_number in transactions:
            temp = transactions[accout_number]
            temp.append(details)
            transactions[accout_number] = temp
        else:
            print('No Transaction found!.')
            
def main():
    bank_system = BankSystem() 
    while True:
        print('-'*15,'\nWelcome to Banking System','-'*15)
        print('1.')
        print('2.')
        print('3.')
        choice = input('Enter your choice : ')
        if choice == '1':
            account_number = int(input('Enter your account number : '))
            holder_name = input('Enter your name : ')
            password = input('Enter your password : ')
            BankAccount.create_account(account_number,  holder_name, password)
