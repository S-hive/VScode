

#Q4
def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0 and n !=1 :
        return even(n)
    elif n % 2 != 0 and n !=1:
        return odd(n)
    if n == 1:
        return 1

def even(n):
    n = n//2
    return 1+hailstone(n)

def odd(n):
    n = n*3+1
    return 1+hailstone(n)



def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        "*** YOUR CODE HERE ***"
        if who > k :
            who = 1
        elif  who <= 0:
            who = k
        if i == n:
            return who
        if has_seven(i):
            direction = -direction
            return f(i+1, who+direction, direction)
        else:
            direction = direction
            return f(i+1, who+direction, direction)
    return f(1, 1, 1)#从这开始游戏

def has_seven(n):  #通过7则显示True
    if n == 0:
        return False
    elif n % 10 == 7 or n % 7==0 :
        return True
    else:
        return has_seven(n // 10)