
''' 2.6 实现类和方法 '''

def make_instance(cls):
    '''此函数的目的是返回一个新的对象实例，该实例是一个"调度字典"。它可以通过 get 和 set 方法来获取和设置属性值。'''
    """Return a new object instance, which is a dispatch dictionary."""
    def get_value(name):
        '''接受一个参数 name,用于获取属性值。'''
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        '''这个函数接受两个参数 name 和 value,用于将传入的 value 存储到 attributes 字典中，以 name 为键。'''
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
        '''此函数的目的是检查传入的 value 是否可调用，并在调用时将其与 instance 绑定。'''
        """Return a bound method if value is callable, or value otherwise."""
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value
        
'''
************************************************************************************
'''


def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary.返回一个新的类，这个类是一个分派字典。"""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls
def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args.返回一个类型为 cls 的新对象，用 args 初始化。"""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance

'''

make_class(attributes, base_class=None):

功能: 创建一个新的类，返回一个包含属性和方法的字典。

参数:

attributes: 一个字典，包含类的属性定义。
base_class: 可选参数，允许指定一个基类，从该类中继承属性（如果存在）。
关键方法:

get_value(name):
根据传入的名称返回相应的属性值。
如果属性在attributes字典中,它将直接返回该属性值；如果在基类中存在，则从基类中获取。
set_value(name, value):
用于设置类的属性。
接受属性名称和对应值,并将其存储在attributes字典中。
new(*args):
用于创建新实例,实际调用init_instance函数。
最后,将以上方法封装在一个字典cls中返回作为新类。

init_instance(cls, *args):

功能: 初始化类的实例。
参数:
cls: 需要初始化的类(这里是调用make_class生成的类)。
*args: 构造函数所需的参数。
关键流程:
使用make_instance(cls)创建一个新的实例。
获取类的__init__方法(如果存在），并使用提供的参数进行初始化。

'''
'''
****************************************************************************************************
'''

def make_account_class():
        """Return the Account class, which has deposit and withdraw methods."""
        interest = 0.02
        def __init__(self, account_holder):
            self['set']('holder', account_holder)  # 在 make_class 函数中，定义了 set_value 函数（对应 set 方法）：cls = {'get': get_value, 'set': set_value, 'new': new}
            self['set']('balance', 0) # attributes['balance'] = 0
        def deposit(self, amount):
            """Increase the account balance by amount and return the new balance."""
            new_balance = self['get']('balance') + amount
            self['set']('balance', new_balance)
            return self['get']('balance')
        def withdraw(self, amount):
            """Decrease the account balance by amount and return the new balance."""
            balance = self['get']('balance')
            if amount > balance:
                return 'Insufficient funds'
            self['set']('balance', balance - amount)
            return self['get']('balance')
        return make_class(locals())

Account = make_account_class()
kirk_account = Account['new']('kirk')

'''
>>> kirk_account['get']('holder')
'kirk'
>>> kirk_account['get']('interest')
0.02
>>> kirk_account['get']('deposit')(20)
20
>>> kirk_account['get']('withdraw')(5)
15
>>> kirk_account['set']('interest', 0.04)
>>> Account['get']('interest')
0.02
'''