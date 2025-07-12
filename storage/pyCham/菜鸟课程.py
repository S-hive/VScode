
import os

def clear_screen():
    # 判断操作系统并执行相应的清屏命令
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS 或 Linux
        os.system('clear')

# 调用清屏函数
clear_screen()





str = '0123456789' 
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
#其中 start 应该小于 end。
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
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

'''
list_1 = [1,2,3,4,5,6,7,8,9]
#print(list_1 [-4:])
list_1  [2]=0 #修改列表元素
print(list_1)

