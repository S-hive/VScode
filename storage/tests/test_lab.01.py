class Account:
    """一个余额非零的账户。"""
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """存入账户 amount，并返回变化后的余额"""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """从账号中取出 amount，并返回变化后的余额"""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
class CheckingAccount(Account):
    """从账号取钱会扣出手续费的账号"""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)
    

def dictionary():
    """返回一个字典的函数实现"""
    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]#遍历records列表，查找键值对
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]#查找键值对是否不存在，不存在则添加
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch
d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)
print(d('getitem', 3))
print(d('getitem', 4))