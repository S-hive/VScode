
'''
def pi_sum(n): 
    total = 0
    for n in range(1,n+1,4): #限制了范围
        total  = 8/(n*(n+2)) + total
    return total
print(pi_sum(100))#错误结果3.121594652591009

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total
print(pi_sum(100))#3.1365926848388144


#第一个代码把n视作分母的范围
#第二个代码把n视作带入表达式的参数


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total         #term(k) 的意思是将当前的 k 作为参数传递给 term 函数

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube)

result = sum_cubes(3)
print(result)

#迭代函数求黄金比例
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
def golden_update(guess):
    return 1/guess + 1
def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)
def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance
print(improve(golden_update, square_close_to_successor))


#牛顿法
def square_root_newton(a,b):
    def f(x):
        return x**a-b
    def df(x):
        return a*x**(a-1)
    #设置一个初值
    x0 = 1
    def starter(x0):
        return f(x0)/df(x0)
    if f(x0) != 0:
        times = 5
        x1 = x0 - starter(x0)
        while times != 0:
            x1 = x1 - f(x1)/df(x1)
            times-=1
    else:print(x0)
    return x1
print(square_root_newton(4,8))

#牛顿法（优化版）

def square_root_newton(a,b):#a,b为方程的系数和常数项
    def f(x):
        return x**a-b
    def df(x):
    def ratio(x):
        return a*x**(a-1)
        return f(x)/df(x)
    #设置一个初值
    x0 = 1
    if f(x0) != 0:
        times = 5
        x1 = x0 - ratio(x0)
        while times != 0:
            x1 = x1 - ratio(x1)
            times-=1
    else:print(x0)
    return x1
print(square_root_newton(3,8))



#柯里化
def curried_pow(x):
    def g(z):
        def h(y):
            return pow(x,y,z)
        return h
    return g
curried_pow(2)(4)(2) #0  计算出 pow(2, 2, 4)，即计算 2 的 2 次方再对 4 取模，结果为 0。
#curried_pow(2)(4)(2) 等价于 pow(2, 2, 4)

def map_to_range(a,s,d):
#a,s表示系数范围，表示底数
    total = 0
    for i in range(a,s+1):
        total = d**i + total
        print(d**i)
    return total
print(map_to_range(0,10,2)) 

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
print(map_to_range(0, 10, 2))


#柯里化
def curry2(f):
    """返回给定的双参数函数的柯里化版本"""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

print(curry2(pow)(2)(5))#32
pow_curried = curry2(pow)
print(pow_curried(2)(5)) #32
#curry2 函数接受一个双参数函数 f 并返回一个单参数函数 g。
#当 g 应用于参数 x 时，它返回一个单参数函数 h。
#当 h 应用于参数 y 时，它调用 f(x, y)。
#因此，f(x, y) 等价于 curry2(f)(x)(y) 

#“给定的双参数函数”是指 curry2 函数的参数 f  这个参数 f 可以是任何接受两个参数的函数，比如 Python 内置的 pow 函数。pow 函数的作用是计算一个数的幂，其基本用法是 pow(x, y)，意味着计算 x 的 y 次方。
#在柯里化的过程中，curry2 函数接受这个双参数函数，并将其转换为可以接受单个参数的函数。

#反柯里化
def uncurry2(g):
    """返回给定的柯里化函数的双参数版本"""
    def f(x, y):
        return g(x)(y)
    return f

print(uncurry2(pow_curried)(2, 5))#32
#uncurry2 函数反转了柯里化变换
# #因此 uncurry2(curry2(f)) 等价于 f(x,y)

#定的柯里化函数是 pow_curried。pow_curried 是之前用柯里化（currying）技术处理过的 pow 函数。
#双参数”是指 uncurry2 函数返回的函数 f

'''

#lambda 
def compose1(f, g):

    return lambda x: f(g(x))
f = compose1(lambda x: x * x,
                lambda y: y + 1)
print(f(12))