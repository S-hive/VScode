
#  Q1
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n
#print((lambda n: n > 2024, for n in gen_fib()))

#  Q2
def differences(t): #返回一个迭代器，包含t中相邻元素的差值
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    t = list(t) #将迭代器转换为列表,防止s 与 n 指向同一迭代器
    s = iter(t) #分别创建新的独立的迭代器
    n = iter(t)
    num =next(s)
    count = []
    num =len(list(t))-1
    try :
        for _ in range(num):
            count.append(next(s)-next(n))
    except StopIteration:
        return iter(count)
    return iter(count)
'''
1. s n 指向同一迭代器
2. next() 指针与输出的关系
3. try 语法及其缩进

Solution:
last_x = next(t)
    for x in t:
        yield x - last_x
        last_x = x
'''

# Q3
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m) # 注意输出格式化
    if n - m > 0:
        for p in partition_gen(n-m,m):
            yield str(p)+' + '+str(m)
    if m > 1:
        yield from partition_gen(n, m-1)
