
class Link:
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
    
# s = Link(1)
# s.rest = s  
# s.rest.first.rest is s
#为什么报错
'''
1 当执行 s = Link(1) 时 创建了一个 Link 对象 first 属性被设置为 1 rest 属性被设置为 Link.empty
2 当执行 s.rest = s 时 问题开始出现 因为 s.rest 原本是 Link.empty 现在被设置为 s 一个 Link 对象 这在逻辑上可能会导致问题 但本身不会报错
3 当执行 s.rest.first.rest = s 时 就会报错 因为 s.rest 现在是 s s.rest.first 就是 s.first 而 s.first 是 1 一个 int 对象 int 对象没有 rest 属性 所以 Python 会抛出 AttributeError
'''

# Q1
def strange_loop():
    """Return a Link s for which s.rest.first.rest is s. 返回s.rest.first.rest为s的链接。

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    "*** YOUR CODE HERE ***"
    s = Link(1,Link(Link(1)))
    s.rest.first.rest = s
    return s


# Q2
def sum_rec(s, k):
    """Return the sum of the first k elements in s.  返回s中前k个元素的总和。(递归实现)

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    # Use a recursive call to sum_rec; don't call sum_iter使用递归调用来调用函数 sum_rec；不要调用函数 sum_iter。
    "*** YOUR CODE HERE ***"
    if k == 0 or s == Link.empty:
        return 0
    else:
        return s.first + sum_rec(s.rest, k - 1)

def sum_iter(s, k):
    """Return the sum of the first k elements in s.  返回s中前k个元素的总和。(循环实现)

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    # Don't call sum_rec or sum_iter 不要调用 “sum_rec” 或 “sum_iter”。
    "*** YOUR CODE HERE ***"
    count = 0
    for _ in range(k):
        if k == 0 or s == Link.empty:
            count += 0
        else:
            count += s.first
            #s.first = s.rest
            s = s.rest
    return count

#s.first = s.rest  导致 TypeError: unsupported operand type(s) for + : 'int' and 'Link'
''' 未正确更新链表指针： 在循环中,s.first = s.rest 是错误的。这行代码并没有更新 s 对象本身，而是错误地将 s.first 的值更改为 s.rest。
正确的做法应该是更新 s 为 s.rest,即使用 s = s.rest  '''


# Q3
def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    if s==Link.empty or t==Link.empty:
        return 0
    if s.first == t.first:
        return 1+overlap(s.rest, t.rest)
    elif s.first > t.first:
        return overlap(s, t.rest)
    elif s.first < t.first:
        return overlap(s.rest, t)    
    

# Q4
def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.将无限链表s的前k位打印为小数。

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')

s = Link(0, Link(8, Link(3)))
s.rest.rest.rest = s.rest.rest
display(s)

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    cache = {}
    tail = result
    while n not in cache:  # 检查当前的变量 n 是否存在于字典 cache 的键中
        q, r = 10 * n // d, 10 * n % d
        tail.rest = Link(q)
        tail = tail.rest
        cache[n] = tail
        n = r
    tail.rest = cache[n]
    return result

#tail = tail.rest 不会导致链表跟踪失败吗？
'''不会,result一直指向链表首相,tail.rest指向列表当前末端并增添新值,也就是result一直'跟踪'链表。'''
# q,r,n 的变化：
'''从除数方法得到'''

#other ways

# num = str((n/d)).replace('0.','')
# for i in num:

# n = 5
# d = 6
# num = str((n/d)).replace('0.','')
# num
#>>>'8333333333333334'