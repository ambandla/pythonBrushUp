
# class Account():
#     def __init__(self, name, balance, password):
#         self.name = name
#         self.balance = balance
#         self.password = password

#     def deposit(self, amountToDeposit, password):
#         if amountToDeposit < 0:
#             print('You cannot deposit a negative amount!')
#             return None
#         if password != self.password:
#             print('Incorrect password')
#             return None
#         self.balance = self.balance + amountToDeposit
#         return self.balance
#     def withdraw(self, amountToWithdraw, password):
#         if amountToWithdraw < 0:
#             print('You cannot withdraw a negative amount')
#             return None
#         if password != self.password:
#             print('Incorrect password for this account')
#             return None
#         if amountToWithdraw > self.balance:
#             print('You cannot withdraw more than you have in your account')
#             return None
#         self.balance = self.balance - amountToWithdraw
#         return self.balance
#     def getBalance(self, password):
#         if password != self.password:
#             print('Incorrect password')
#             return None
#         return self.balance
#     def show(self):
#         print('       Name', self.name)
#         print('       Balance:', self.balance)
#         print()

class testClass ():
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def increment(self,p1):
        self.p1 = self.p1 + p1
        return self.p1


testObject = testClass(1, 2, 3)
print (testObject.p1)
testObject.increment(5)
print(testObject.p1)

testObject2 = testClass(10,20,30)
print(testObject2.p1)
testObject2.increment(5)
print(testObject2.p1)

class switch():
    def __init__(self):
        self.state = 'off'
        self.brightness = 0
    
    def turnOn(self):
        self.state = 'on'
        return self.state
    
    def raiseBrightness(self, brightness):
        if brightness + self.brightness > 100:
            print('Brightness cannot exceed 100')
            return None
        self.brightness = self.brightness + brightness
        return self.brightness
    
    def lowerBrightness(self, brightness):
        if self.brightness - brightness < 0:
            print ('Brightness cannot be less than 0')
            return None
        self.brightness = self.brightness - brightness
        return self.brightness
    
    def show(self):
        print('State:', self.state)
        print('Brightness:', self.brightness)
        print()

switchObject = switch()
print(switchObject.state)
switchObject.turnOn()
switchObject.raiseBrightness(10)
print(switchObject.state)
print(switchObject.brightness)