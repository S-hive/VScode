

# x = input('')
# ls = bin(int(x))
# ls = ls[2:]
# print(x +'='+ls+'(B)')

# print(ls,'(B)')
# print(ls+'(B)')区别:
'''
print(ls, '(B)')
在 Python 中,print函数可以接受多个参数,当传入多个参数时,print函数会自动在每个参数之间添加一个空格作为分隔符，并将所有参数输出到控制台。这里假设ls是一个已经定义的变量，print(ls, '(B)')会将ls的值和字符串'(B)'作为两个独立的对象输出，它们之间会有一个空格分隔。
print(ls+'(B)')
这里涉及字符串拼接操作。如果ls是一个字符串类型的变量,+运算符用于将ls和'(B)'两个字符串连接成一个新的字符串。然后print函数会输出这个拼接后的新字符串，在这个新字符串中，ls和'(B)'是紧密相连的，没有额外的空格。'''

# ls = input('').split(" ")
# n = []
# for i in ls :
#     i = int(i)
#     if i not in n :#and i in x (i 换了类型，所以不在x中)
#         n.append(i)
# #n.reverse()  [5, 3, 2, 4]
# print(n) #[3, 2, 4, 5]

# x = int((input('')))
# n = (input(''))
# ls = list(n.split(' '))
# ls.remove(max(ls))
# ls.remove(min(ls))
# ls.sort(reverse=True)
# total = 0
# for i in ls:
#     print(i, end=' ')
#     total += float(i)
# print()
# print("{:.2f}".format(total/(x-2)))

# x = int(input(''))
# ls = list(range(1,x+1))
# if len(ls) > 2:
#     while len(ls) > 2:
#         for i in ls:
#             if i % 3 ==0:
#                 ls.remove(i)
#         ls = list(range(1,len(ls)+1))
# print(max(ls))

'''
在循环中修改列表：使用 ls.remove(i) 在遍历 ls 时会改变列表的长度，
从而导致某些元素被跳过。比如，当 remove 删除一个元素后，
列表中的下一个元素会移动到相应的位置，这可能会导致本次循环中的某些元素无法被判断到。
'''
# x = int(input(''))
# ls = list(range(1,x+1))
# num = range(1,4)
# move = []
# while len(move) !=x-1:
#     for i in ls:
#         for n in num:
#             if n==3:
#                 move.append(i)
# for i in move:
#     ls.remove(i)     
# print(max(ls))


x = int(input(''))
ls = list(range(1,x+1))
num = 0
count= 0
while len(ls) > 1:
    num+=1
    if num ==3:
        ls.pop(count)
        num = 0
    else:
        count+=1      
        #count += 1 不变因为元素会代替被删除的元素，所以count不会变
    if count == len(ls):  # 如果达到列表末尾，则循环到头
        count = 0
    # else: 
    #     count+=1  
    '''循环从上至下,如果放在这里的话,便利第一个if句之后会遍厉else从句，
    因为else从句的条件变成,与上面两个if相关.num改变成o的时候,else会执行'''

    # if count>len(ls)-1:#-1
    #     count=0
print(int(ls[0]))
#如果这个元素是一个可以被转换为整数的类型（比如数字字符串或本身就是整数），那么使用int(ls[0])就可以将其转换为整数并打印出来。
# print(int(ls))错误 列表不是一个可以被直接转换为整数的类型



x = int(input(''))
ls = list(range(1,x+1))
count = range(1,4)
num = []
while len(ls)>1:   
    # for n in ls:
    #     for i in count:
    for n,i in zip(ls,count):
'''
如果两个列表的长度不一致,zip() 只会遍历到最短列表的长度。
若希望遍历到最长的列表，可以使用 itertools.zip_longest() 函数，这样不匹配的部分会用 None 填充。
'''
    if i == 3:
        num.append(n)
    if n==ls[-1]:
        for i in num :
            ls.remove(i)
print(int(ls[0]))                   
               
                

            
        








