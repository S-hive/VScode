class Transaction:
    def __init__(self, id , before = 0, after = 0):
        self.before = before
        self.after = after
        self.id = id
    
    def changed(self):
        """Return whether the transaction resulted in a changed balance."""
        """返回交易是否导致余额发生变化"""
        "*** YOUR CODE HERE ***"
        if self.after != self.before:
            return True
        else:
            return False

    def report(self):
        """Return a string describing the transaction.
        返回描述事务的字符串。
        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        if not self.changed():
            msg = 'no change'
            return str(self.id) +  ': ' + msg
        if self.after > self.before:
            "*** YOUR CODE HERE ***"
            msg = 'increased '
        else: 
            msg = 'decreased '
        return str(self.id) +  ': ' + msg+str(self.before)+'->'+str(self.after)

class BankAccount(Transaction):
    """A bank account that tracks its transaction history.
    跟踪其交易历史的银行账户。
    >>> a = BankAccount('Eric')
    >>> a.deposit(100)    # Transaction 0 for a
    100
    >>> b = BankAccount('Erica')
    >>> a.withdraw(30)    # Transaction 1 for a
    70
    >>> a.deposit(10)     # Transaction 2 for a
    80
    >>> b.deposit(50)     # Transaction 0 for b
    50
    >>> b.withdraw(10)    # Transaction 1 for b
    40
    >>> a.withdraw(100)   # Transaction 3 for a
    'Insufficient funds'
    >>> len(a.transactions)
    4
    >>> len([t for t in a.transactions if t.changed()])
    3
    >>> for t in a.transactions:
    ...     print(t.report())
    0: increased 0->100
    1: decreased 100->70
    2: increased 70->80
    3: no change
    >>> b.withdraw(100)   # Transaction 2 for b
    'Insufficient funds'
    >>> b.withdraw(30)    # Transaction 3 for b
    10
    >>> for t in b.transactions:
    ...     print(t.report())
    0: increased 0->50
    1: decreased 50->40
    2: no change
    3: decreased 40->10
    """

    # *** YOU NEED TO MAKE CHANGES IN SEVERAL PLACES IN THIS CLASS ***

    def next_id(self):
        #return self.id = len(self.transactions) 
        ''' next_id 方法在调用时没有返回任何值。这意味着 Transaction 对象的 id 始终会是 None,
        因为 self.next_id() 没有赋值给 self.id。应该修改 next_id 方法以返回当前的 id 值。'''

        self.id = len(self.transactions)
        return  self.id
    
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount, add the deposit
        to the transaction history, and return the new balance.
        按金额 增加 账户余额，添加存款到交易历史，并返回新的余额。
        """
        self.before = self.balance 
        self.balance = self.balance + amount
        self.after = self.balance 
        self.transactions.append(Transaction(self.next_id(), self.before, self.after))
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount, add the withdraw
        to the transaction history, and return the new balance.
        按金额 减少 账户余额，添加提款到交易历史，并返回新的余额。
        """
        self.before = self.balance 
        if amount > self.balance:
            self.transactions.append(Transaction(self.next_id()))
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.after = self.balance 
        self.transactions.append(Transaction(self.next_id(), self.before, self.after))
        return self.balance
    
###########################
# 注意id的变化
# self.transactions 的创建，存储
#   注意第一次存储账户时先调用了next_id方法,此时transactions为空列表，调用len返回0，恰好id从0开始，则不用更改
''' li = []
    len(li) '''
#  next_id 方法虽然没有显式返回值但似乎应该改变 id 却没按预期更改的原因分析：
''' def next_id(self):
        return self.id = len(self.transactions) '''
# 它其实是改变了 id 的值的，但是在 transaction 里面它调用的是改变 id 了之后的返回值，
# 而它的返回值是 none ，也就是说 transaction 其实得到的是一个 none 值。
'''实例属性初始化机制
在 Python 中，虽然 BankAccount 类继承自 Transaction 类，但属性并不会自动被完全继承并初始化，原因如下：
当创建一个类的实例时,Python 会调用该类的 __init__ 方法来进行实例的初始化工作。对于 BankAccount 类，当你执行类似 a = BankAccount('Eric') 这样的语句创建实例时,
Python 只会执行 BankAccount 类中定义的 __init__ 函数，而不会自动去调用父类 Transaction 的 __init__ 函数来初始化继承过来的属性（除非显式调用）。
'''
###########################

class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
        一封电子邮件具有以下实例属性：
        - “msg (str)”：表示消息的内容，是一个字符串类型。
        - “sender (Client)”：表示发送这封电子邮件的客户端。
        - “recipient_name (str)”：表示收件人的名称，收件人是另一个客户端，也是字符串类型。
    """

    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    每台服务器都有一个名为 clients 的实例属性，它是一个从客户端名称到客户端对象的字典。
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to.
            email is an instance of the Email class.
            将电子邮件附加到收件人的收件箱中。
            电子邮件是电子邮件类的一个实例。
        """
        self.clients[email.recipient_name].inbox.append(email) # 先在字典查找收件人，再将邮件附加到收件人的收件箱中。

    def register_client(self, client): # 将代指名称self与真名name绑定
        """Add a client to the clients mapping (which is a 
        dictionary from client names to client instances).
            client is an instance of the Client class.
        将一个客户端添加到 clients 映射中（这是一个从客户端名称到客户端实例的字典）。
        这里的“client”是 Client 类的一个实例。
        """
        self.clients[client.name] = client  # 真名绑定到self
        #self.clients[name] = self   ns的位置:寄件人会写收件人的真名，要转到代名
        #self.clients[self] = name
class Client:
    """A client has a server, a name (str), and an inbox (list).
    客户端有一个服务器、一个名称(str)和一个收件箱（列表）。
    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)
        #server.register_client(name)

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient.
        发送一封带有给定信息的电子邮件给收件人"""
        email = Email(message,self,recipient_name)
        self.server.send(email)

###########################################
# server.register_client(self)调用Server类的实例为什么不写Server.
'''  已经有 Server 类的实例(比如 server ) 这里的 server 是已经创建好的 Server 类的实例对象(通过 >>> s = Server() >>> a = Client(s, 'Alice')) 
而 register_client 是 Server 类中定义的实例方法'''
# 为什么可以client.name
'''server.register_client(self) 表明，是将当前正在初始化的 Client 类的这个实例（也就是 self 所指代的对象）作为参数传递给了 Server 类的 register_client 方法，
这就进一步明确了在 register_client 方法中接收到的 client 参数实际上就是从 Client 类的实例传递过来的，
所以 client 就是 Client 类的一个实例。client.name 访问的是 Client 类某个具体实例（这里用 client 指代这个实例）的 name 属性'''
###########################################

class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself 将由子类提供，但不是由Coin本身提供
    year  = 2024

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        #self.volume = self.volume + (Mint.present_year - self.year-50) 一个新的造币厂有当前的年份
        if Mint.present_year != self.year:
            self.volume = self.volume + (Mint.present_year - self.year-50)
        return self.volume

class Mint(Coin):
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.
    一个铸币厂通过在硬币上压印年份来制造硬币。
    更新方法将铸币厂的印记设置为铸币厂的当前年份(Mint.present_year)
    >>> mint = Mint()
    >>> mint.year
    2024
    >>> dime = mint.create(Dime)
    >>> dime.year
    2024
    >>> Mint.present_year = 2104  # Time passes
    >>> nickel = mint.create(Nickel) #实例 Nickel = coin
    >>> nickel.year     # The mint has not updated its stamp yet 造币厂还没有更新它的邮票
    2024
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2104 造币厂的年份更新到2104年
    >>> Mint.present_year = 2179     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year一个新的造币厂有当前的年份
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!升级所有一角硬币
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2024
    # year = present_year
    
    def __init__(self):
        self.update()
        # self.volume = 0
        # self.year = Mint.present_year
        
        #self.worth = Coin.worth(self) 在执行到这里时，会执行Coin.worth(self)返回0，则self.worth = 0，再调用会显示int类型无法被调用。
        

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        # self.volume = coin.cents
        return Coin(self.year)
        #return self  create方法返回的是self，而应该是返回新创建的硬币实例。这会导致后续dime实例和nickel实例共用一个create。
        

    def update(self):
        "*** YOUR CODE HERE ***"
        Mint.year = Mint.present_year
        self.year = Mint.year
        #return self.year
''' >>> mint.update()   # The mint's year is updated to 2104 造币厂的年份更新到2104年
    >>> Mint.present_year = 2179  '''


class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10
###############################################
#为什么 Dime 和 Nickel共用一个create方法（环境）？
'''
在 Python 的面向对象编程中,self 指的是调用方法的那个对象实例本身。
当你在类的实例方法里写 return self 时，返回的就是当前正在调用这个方法的那个具体对象。

即使 Dime 和 Nickel 是不同的类去实例化出来的不同实例，但在 create 方法执行过程中,return self 操作只和调用 create 方法的那个对象有关。
因为每次都是 mint 去调用 create 方法，所以不管传入的参数是 Dime 类型的实例还是 Nickel 类型的实例，返回的始终是 mint 本身。
'''

#例子：
# obj1和obj2是Mint()的两个实例，相互独立
obj1 = Mint()
obj2 = Mint()

obj1.create(30)
obj2.create(40)

#dime 和 nickel 分别就是调用 create 方法返回的结果，也就是通过 Mint 类实例 mint 创建出来的 Dime 类和 Nickel 类的实例。
#由于是在同一个 mint 实例所关联的 create 方法环境中进行操作，所以共享同一个create环境，相互影响
mint = Mint()
dime = mint.create(Dime)
nickel = mint.create(Nickel)


# >>> dime.year
# 2024
# >>> Mint.present_year = 2104  # Time passes
# >>> nickel = mint.create(Nickel) #实例 Nickel = coin
# >>> nickel.year     # The mint has not updated its stamp yet 造币厂还没有更新它的邮票
# 2024
'''
Mint.present_year 是 Mint 类的一个类属性，代表造币厂当前的年份，通过 Mint.present_year = 2104 这样的语句可以直接修改类属性的值。
然而，类属性的改变并不会自动同步到每个已经创建的 Mint 类实例的相关属性上，除非在实例的代码逻辑中有主动去获取或者更新以匹配类属性变化的操作。
'''

################################################

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2024
    >>> dime = mint.create(Dime)
    >>> dime.year
    2024
    >>> Mint.present_year = 2104  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2024
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2104
    >>> Mint.present_year = 2179     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2024

    def __init__(self):
        self.update()

    def create(self, coin):
        return coin(self.year)

    def update(self):
        self.year = Mint.present_year

class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        return self.cents + max(0, Mint.present_year - self.year - 50)

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10



