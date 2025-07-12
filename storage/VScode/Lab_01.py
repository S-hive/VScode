


my_set = set()

for i in range (1,80):
    if  80 % i ==0:
        print(i)
        my_set.add(i)
print(max(my_set))

n=27
while n != 1:
    if n % 2 != 0:
        n = n*3+1
    
    else:
        n = n/2
    print(n,end=',')

for n in range (1,10001):
   
    if n % 2 != 0:
        n = n*3+1
    
    else:
        n = n/2

if n != 1:
    print('The hail conjecture is right in this range.')
else:
    print(n) 
       

def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return 


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        num=n
        for i in range(n-k+1,n):
           # i=i*num ( i=2 i=2*4=8 i=3 i=3*4=12
            num=num*i
        return num
print(falling(4,3))


def divisible_by_k(n, k):
    times = 0
    num = k
    if k > n:
        return 0
    if k <= n:
        for k in range (k,n+1,num):
            print(k)
            times+=1
        return times
print(divisible_by_k(6,7))

def sum_digits(y):
    """Sum all the digits of y."""
    i = 0
    while y>=1 :
        x = y%10
        y = y//10
        i+=x
    return i
print(sum_digits(12345)) # Output: 15


class lab_01:
    def double_eights(n):
        while n != 0:
            x = n%10
            n = n//10
            if x ==8 :
                r = n %10
                if r ==8 :
                    return True
                else:
                    return False
            #return False (if x！=8,都是False，结束程序)
        #return False (n=0,结束程序)
    print(double_eights(808))

