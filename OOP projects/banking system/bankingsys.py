class User:
    def __init__(self, first_name, last_name, age, sex):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.sex = sex

    def show_user_datails(self):
        print(f'Name: {self.f_name} {self.l_name}')
        print(f'Age: {self.age}')
        print(f'Sex: {self.sex}')

class Bank(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f'{self.amount} CZK was deposited to your account.')

    def withdraw(self, amount):
        self.amount = amount

        if self.amount > self.balance:
            print('You cannot withdraw more than what is your balance.')
        else:
            self.balance -= self.amount
            print(f'{self.amount} was withdrawed from your account.')

    def view_balance(self):
        print(f'Your balance is {self.balance}')


