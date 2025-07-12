import os

def clear_screen():
    # 判断操作系统并执行相应的清屏命令
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS 或 Linux
        os.system('clear')

# 调用清屏函数
clear_screen()





str = '0123456789' # 字符串
# 字符串的切片操作
print(str[2:5])
print(str[2:5])    #输出: 234
print(str[2:5:2])    #隔一个 输出: 24
print(str[2:5:1])    #不隔 输出: 234
#print(str[2:5:0]) 错误，步长不能为 0。
print(str[2:5:-1])  

#由于步长为 -1,
#Python会尝试从索引 2 (字符 '2'）向左移动，
#但由于切片的结束条件是 5,即从这个位置不往左提取
#这导致没有任何字符能够被提取到。因此，最终输出为空。
 
print(str[5:2]) #开始位置大于结束位置，导致结果为空。
print(str[-5:-8])#正确的方式应该是 [start:end]
#！！！！！！！！！！！其中 start 《 end 正步长。！！
print(str[5:2:-1])
print(str[-1:])#没有注明，读取顺序从左到右
print("end")

---------------
x = True
y = False
z = False
result = x or y and not z  # 先计算 y and not z,然后再计算 x or 结果
print(result)  # 输出: True,因为 not z 是 True,y and True 是 False，x or False 是 True
--------------
#优先级:not > and > or
a = ''
print(bool(a))  # 输出: False



print(int(True))
print(True-6)
print(type(False))
print(True and False or not False)



if True:
    print("This will always print")
   
if not False:
    print("This will also always print")

-------------------------------------------
x = []
if x:#判断
    print("x is non-zero ")
if not x:#判断
    print("x is zero ")

if False:#永远不会执行
    print("This will never print")
if True:#永远执不论代码的执行路径如何变化
    #只要遇到这个 if True,下面的代码就会被执行
    print("This will print")

 -----------------------------------------
# 列表的切片操作
list_1 = [1, 2, 3, 'a',4, 5, 6, 7, 8, 9]

# 使用索引访问元素
print(list_1[2])  # 输出: 3
print(list_1[-1])  # 输出: 9 (最后一个元素)

# 使用切片获取子列表
print(list_1[2:5])  # 输出: [3, 4, 5]
print(list_1[:3])   # 输出: [1, 2, 3]
print(list_1[5:])   # 输出: [6, 7, 8, 9]
print(list_1[::2])  # 输出: [1, 3, 5, 7, 9] (步长为2的切片)
----------
# 字符串的切片操作
str_1 = "Hello, World!"

# 使用索引访问字符
print(str_1[7])    # 输出: W
print(str_1[-1])   # 输出: !

# 使用切片获取子字符串
print(str_1[0:5])  # 输出: Hello
print(str_1[:5])   # 输出: Hello
print(str_1[7:])   # 输出: World!
print(str_1[::2])  # 输出: Hlo ol! (步长为2的切片)

list_1 = [1,2,3,4,5,6,7,8,9]
#print(list_1 [-4:])
list_1  [2]=0 #修改列表元素
print(list_1)

修改列表元素
>>> a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为 [] 
>>> a
[9, 2, 6]

#元组的切片操作
tuple_1 =('a',1,'b',2,3,4,5,6)
#print(tuple_1[-5:-1:-1]) tuple[start:stop:step]
# !!!!!!!!!!!!!!!!!!!!!!!负步长 start > stop。!!
#start 是开始索引，stop 是结束索引，step 是步长OOO
print(tuple_1[-1:-5:-1])
print(tuple_1*2)#重复元组
#连接
#print (tuple_1 +list_1) 错误 
# 只能将元组（不是“列表”）连接到元组  
"""
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
在没有逗号的情况下,Python会将括号解释为数学运
算中的括号，而不是元组的表示

print(type(float))#<class 'type'> 查询类型

这样的话，not_a_tuple 将是整数类型而不是元组类型。

string、list 和 tuple 都属于 sequence（序列）。

注意：

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用 + 操作符进行拼接。


tuple=(1,2,3)
#tuple[0]=3 #元组不能修改元素
tup=(1,)
tuple_1=tuple+tup
print(tuple_1)



#注意：创建一个空集合必须用 set() 而不是 { }，
# 因为 { } 是用来创建一个空字典。
sites={1,2,3,4,5,6,"good"}
"""用户通过 input() 函数输入的值会被作为字符串类型进
行处理，而 sites 中的元素都是整数
(1, 2, 3, 4, 5, 6),只有一个元素是字符串 ("good")。
因此，用户输入的任何数字字符串都不会与 sites 
中的整数匹配,导致永远输出“no”"""
num=eval(input("give me a num"))
"""在 input() 函数内部使用 print() 函数作为提示信息
是不必要的，应该直接使用 input("give me a num")"""
if num in sites :
    print("yes")
else: print("no")

a = str
sites = {2,a}
print(sites)
num = eval(input("give me a num"))
if num in sites:
    print("yes")
else:
    print("no")

#集合运算
q = {'a','b','c','d'}
w = {'c','d','e','f'}
print(q-w)   #{'a', 'b'} 差集
print(w|q)   #{'a', 'f', 'b', 'e', 'd', 'c'}  并集
print(q&w)   #{'c', 'd'} 交集
print(q^w)   #{'a', 'b', 'e', 'f'} 同时不存在的元素
'''

a = str
sites = {2,a} #2,a可行
print(sites)
num = eval(input("give me a num : "))
if num in sites:
    print("yes")
else:
    print("no")


'''

sites = {2,'a'} #2,'a'可行，a不可行
print(sites)
num = eval(input("give me a num : "))
if num in sites:
    print("yes")
else:
    print("no")




sites = {'s','d','a',1}
sites.add(2)#输入a,s,d,都可行；1不可行
print(sites)
num = str(input("give me a num : "))
if num in sites:
    print("yes")
else:
    print("no")




my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["1"])  #错误，不可调换 
#键(key) : 值(value)
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有


'''
'''
#字典的创建
dixt = {'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
#字典通常用大括号 {} 来表示，
# Python 还提供了 dict() 这一构造函数，
# 可以通过传入可迭代的键值对集合（
# 如元组的列表）来创建字典。


#dict ={a=1,b=2,c=3}
dict_1={"name": "Runoob", "age": 7, "city": "Beijing"}#创建字典
f=input("What's f?")
#print(dict_1.get(f, "Key not found"))  # 如果键不存在，返回 "Key not found"

print(dict_1[f])

#不同类型元素是不是只能存储在字典dict,列表list,元组tuple中？集合set呢？
# #列表和元组都可以存储不同类型的元素，包括整型、字符型、字符串等。
#答：不同类型元素可以存储在字典，元组中，但不能存储在列表中。
#字典是一种映射类型，它的元素是键值对。
#列表和元组是有序集合，其元素是按索引访问的。
#因此，列表和元组是可以存储不同类型元素的容器，
#而字典则是一种更加通用的容器，可以存储各种类型的数据。
#进行修改操作时需要创建一个新的 bytes 
#不可修改元素：集合set,元组tuple,字符串string
old_bytes = b'hello world'
new_bytes = b'Hi,' + old_bytes[:]
print(new_bytes)

#bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")


#ord
ord(char)
print(ord('A'))  # 输出 65
print(ord('a'))  # 输出 97
print(ord('中'))  # 输出 20013

