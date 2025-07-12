
#需要多长时间
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare: #如果乌龟的距离小于兔子的距离，则结果为负值，此时条件不成立；如果乌龟追上了兔子，则两者的距离为0，条件成立。
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

#判断n是否是素数
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 2
    while i<n**0.5+1:
        if n%i==0:
            print('False')
            break
        else:
            print('True')
            break
        i = i+1
    if n == 1:
        print('False')

#编写一个函数，该函数以正整数形式返回唯一位数。
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    
    my_set = set()
    while n >= 1:
        i = n % 10
        n = n // 10
        my_set.add(i)
    return len(my_set)
    

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n>=1 :
        x = n %10
        n = n//10
        if x ==k:
            return True
        else :
            continue
    return False

#d(b),abc,b


