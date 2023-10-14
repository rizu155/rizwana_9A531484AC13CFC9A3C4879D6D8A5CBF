class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      #self.__account_balance = self.__account_balance+amount
      print("Deposited Rs {}. New balance:Rs {}".format(
          amount, self.__account_balance))
    else:
      print(" Invalid Deposit Amount")

  def withdrawal(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw Rs {}. New balance:Rs {}".format(amount,
                                                       self.__account_balance))
    else:
      print(" Invalid Withdrawal Amount")

  def display_balance(self):
    print("Account Balance for  {} (Account #{}):Rs{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


account = BankAccount("123456789","rizu", 500.0)

account.display_balance()
account.deposit(500.0)
account.withdrawal(200.0)
account.display_balance()