

'''
c = 2
a = c**3
print(a)#8
b=5
b*=a  #b=b*a,前后两个b是不同的值
print(b)#40
b /=a
print(b) #5.0
#b的值从5变为40，最后又变为5.0
b /=c 
print(b) #2.5
b = 5
b //= c
print(b) #2
b %= a #2/8=0····2   取余
print(b) #2


b = eval(input('give me a num :'))
print(b+6)

# := 赋值运算符，可以将表达式的值赋给变量，并返回赋值结果。
# len() 函数用于计算字符串的长度。
len("give me a num :")
print(b+5) #20
#段代码的主要功能是计算字符串 "give me a num :" 的长度，
# 长度为15，并在此基础上加上 5，最后将结果输出。



q = {'a','b','c','d'}
w = {'c','d','e','f'}
print(q-w)   #{'a', 'b'} 差集
print(w|q)   #{'a', 'f', 'b', 'e', 'd', 'c'}  并集
print(q&w)   #{'c', 'd'} 交集
print(q^w)   #{'a', 'b', 'e', 'f'} 同时不存在的元素

# ：= 还像运算符，但它可以用于变量赋值。
# 传统写法
n = 10
if n > 5:
    print(n)

# 使用海象运算符
if (n := 10) > 5:
    print(n)

'''


 









