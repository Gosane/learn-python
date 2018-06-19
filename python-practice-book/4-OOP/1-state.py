# Past code juste enough for a single account
# balance = 0

# def deposit(amount):
#     global balance
#     balance += amount
#     return balance

# def withdraw(amount):
#     global balance
#     balance -= amount
#     return balance

# print (deposit(2000))

def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
deposit(a, 50000)
print (withdraw(a,99))
b = make_account()
deposit(b, 500)
print (deposit(b,99))

##### Classes and Objects #####

class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

d = BankAccount()
c = BankAccount()

d.deposit(1000)
c.deposit(2300)

print(d.withdraw(500))
print(c.deposit(500))

#### Inheritance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print ('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)
            return self.balance
e = MinimumBalanceAccount(BankAccount)
e.minimum_balance = 50

print (e.deposit(50000))
print (e.withdraw(5))
print (e.withdraw(5555))

### Problem 1

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

aa = A()
bb = B()

print(aa.f())
print(bb.f())
print(aa.g())
print(bb.g())
