passphrase = 'REPLACE_THIS_WITH_PASSPHRASE'

def midsem_survey(p):
    """
    You do not need to understand this code.
    >>> midsem_survey(passphrase)
    '2bf925d47c03503d3ebe5a6fc12d479b8d12f14c0494b43deba963a0'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


class VendingMachine:
    """A vending machine that vends some product for some price.
        以某种价格出售某种产品的自动售货机。
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        """Set the product and its price, as well as other instance attributes.
        设置产品及其价格，以及其他实例属性。"""
        "*** YOUR CODE HERE ***"
        self.number = 0 # 货品数量
        self.money = 0 # 支付金额
        self.need_num = price # 需求金额
        self.product = product
        self.price = price

    def restock(self, n):
        """Add n to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        向库存中添加 n,并返回关于更新后的库存水平的消息。例如,当前糖果库存:3。
        """
        "*** YOUR CODE HERE ***"
        self.number+=n
        print(f"'Current {self.product} stock: {self.number}'")
        #return self.number

    def add_funds(self, n):
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Nothing left to vend. Please restock. Here is your $4.

        Otherwise, add n to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        如果机器缺货，返回一条消息通知用户补货（并退还他们的 n 美元）。例如：“没有东西可售卖了。请补货。这是你的 4 美元。
        ”否则，将 n 加到余额中并返回一条关于更新后余额的消息。例如:“当前余额:4 美元”。
        """
        "*** YOUR CODE HERE ***"
        if self.number > 0:
            self.money += n
            print(f"'Current balance: ${self.money}'")
        else:
            print(f"'Nothing left to vend. Please restock. Here is your ${n}.'")
        #return self.money,self.number,self.need_num


    def vend(self):
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Nothing left to vend. Please restock.
              Please add $3 more funds.
        如果有足够的库存和资金,则分发产品返回消息。相应地更新库存和余额。这是你的糖果和2美元零钱。
        如果没有，请返回一条消息,建议如何纠正问题。没有什么可卖的了。请补货。请再添加3美元的资金。      
        """
        "*** YOUR CODE HERE ***"
        if self.number == 0:
            print("'Nothing left to vend. Please restock.'")
        else:
            if self.need_num == self.money :
                self.number -= 1
                print(f"'Here is your {self.product}.'")
            elif self.need_num > self.money :
                money = self.need_num - self.money
                print(f"'Please add ${money } more funds.'")
            else:
                self.money = self.money - self.need_num
                print(f"'Here is your {self.product} and ${self.money} change.'")
                self.money = 0
                self.number -= 1
        #return self.money,self.number,self.need_num


# 交互式编程中，自定义函数返回一个字符串和直接打印一个字符串有什么区别
''' 1.函数的可复用性：当自定义函数返回一个字符串时，这个函数可以在程序的多个地方被调用
    2.数据传递：返回字符串的函数可以将数据传递给其他函数或者程序的其他部分
    3.程序流程控制：返回字符串的函数可以根据不同的条件返回不同的字符串，从而影响程序的流程
    直接打印字符串:即时输出 不可复用性 程序流程相对简单 '''

# if self.number -= 1 : 报错？
'''self.number -= 1 是一个赋值操作，它会将 self.number 的值减少 1,然后将结果赋值给 self.number。
这个操作本身没有问题，但它的返回值是 None.因此在 if 语句中使用它会导致逻辑错误。'''

##########################################################################

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.
    将正数n的数字存储在链表中。
    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    >>> store_digits(20105)
    Link(2, Link(0, Link(1, Link(0, Link(5)))))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    # if n < 10 :
    #     return Link(n)
    # else:
        #return Link(n % 10, store_digits(n // 10))  Link(5, Link(4, Link(3, Link(2))))
    num = Link.empty
    while n > 0:
        i = n % 10
        n = n // 10
        num = Link(i,num)
    return num

########################################################################################

'''
def store_digits(n):
    if n < 10 :
        return [n]
    else:
        return [n % 10, store_digits(n // 10)]
print(store_digits(2345))
>>>[5, [4, [3, [2, []]]]]
'''
'''
def store_digits(n):
    result = []
    while n > 0:
        result = [n % 10, result]
        n //= 10          #第一次是空,其他是上次的结果
    return result
print(store_digits(2345))
>>>[2, [3, [4, [5, []]]]]
'''
# 两者区别在于store_digits(n // 10)返回的是其他元素，result除了第一次为空，其他都是上次的全部结果。


def deep_map_mut(func, s):
    """Mutates a deep link s by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.
    通过将深度嵌套结构 “s” 中的每个项替换为对该项调用 “func” 的结果来修改 “s”。
    函数不会创建新的链接对象(因此不会使用链接的构造函数）。并且这个函数不返回修改后的对象。

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    # if isinstance(s, Link): #错误代码
    #     if isinstance(s.first, Link):
    #         deep_map_mut(func, s.first)
    #     elif  not isinstance(s.first, Link):
    #         s.first = func(s.first)
    #         deep_map_mut(func, s.rest)
    #     elif s == Link.empty:
    #         return None
    # else:
    #     return None

    if isinstance(s, Link): #正确代码
        if s == Link.empty:
            return None
        elif isinstance(s.first, Link):
            deep_map_mut(func, s.first)
        elif  isinstance(s.first, int): # not isinstance(s.first, Link) 也行
            s.first = func(s.first)
        deep_map_mut(func, s.rest)
    else:
        return None
    
#print(isinstance(Link(5, Link(6), Link)))   True

# link1 = Link(3, Link(Link(4), Link(5, Link(6))))
# print(link1)
# deep_map_mut(lambda x: x * x, link1)
# print(link1)

###################################################################################################

'''递归终止条件不正确:elif s == Link.empty 这个条件应该放在函数的开头，而不是在处理完 s.first 和 s.rest 之后。
因为如果 s 是空的，后续的递归调用是不必要的，并且会导致错误，因为 s.first 和 s.rest 对于空链表是没有定义的。'''

'''在处理完 s.first 后，使用了 return deep_map_mut(func, s.rest)，这意味着如果 s.first 不是 Link,函数会立即返回，而不会继续处理 s.rest。
正确的做法是在处理完 s.first 后，继续递归处理 s.rest,而不是在 elif 分支中使用 return。'''

#     Traceback (most recent call last):
#       ...
#     AttributeError: 'tuple' object has no attribute 'first'
'''我们需要在递归调用之前检查 s 是否是一个 Link 实例。如果不是 Link 实例，则不需要进一步处理 s.first 和 s.rest。'''

# Error: expected  (错误代码)
#     <9 <16> 25 36>
# but got
#     <9 <16> 5 6>
'''执行到Link(Link(4), Link(5, Link(6)))时,s.first 已经是 Link 实例，因此会进入 isinstance(s.first, Link) 分支，
结束后续运行后，后续操作离开递归范围，执行
    else:
        return None
于是结果为5 6>
'''

#？代码预执行时（即到达link1 = Link(3, Link(Link(4), Link(5, Link(6))))时，为什么评估顺序是 4 -> 6 -> 5 -> 3 而不是 3456？
#？ 想法 ： 由一个参数开始，到两个，到多个，顺序执行？？？

'''
s.first 是 3,不是 Link 实例。
s.first 是 Link(4),是一个 Link 实例。
s.first 是 4,不是 Link 实例。
s.first 是 5,不是 Link 实例。
s.first 是 6,不是 Link 实例。
'''


def two_list(vals, counts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.
    根据传入的这两个列表返回一个链表。假设 “vals” 和 “counts” 大小相同,“vals” 中的元素表示值,
    “counts” 中对应的元素表示在最终链表中所需的这个值的数量。假定 “counts” 中的所有元素都大于 0,
    并且两个列表都至少有一个元素。
    >>> a = [1, 3]
    >>> b = [1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"
    count = Link.empty
    vals.reverse()
    counts.reverse()
    for i ,n in zip(vals,counts):    
        for _ in range(n):
            count = Link(i,count)
    return count

# Error: expected
#     Link(1, Link(3))
# but got
#     Link(3, Link(1))
'''注意指针和firse的位置。解决方法:列表倒序'''


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

