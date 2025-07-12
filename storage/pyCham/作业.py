print("李雅琳240200430")
'''
#投注
from random import randint
mynum = []
x = 0
while x < 4:
    i = randint(1,10)
    if i not in mynum:
        mynum.append(i)
        x += 1
mynum.sort()
x = randint(1,5)
mynum.append(x)
print(mynum)
#开奖号码
lottery = []
x = 0
while x < 4:
    i = randint(1,10)
    if i not in lottery:
        lottery.append(i)
        x = x+1
x = randint(1,5)
lottery.append(x)
print(lottery)
#匹配
blackok = 0
whiteok = False
black=mynum[:4]
for i in range (len(mynum)-1):
    if i in lottery:
        blackok+=1
if mynum[4] == lottery[4]:
    whiteok=True
print(blackok,whiteok)


'''


#from 李雅琳

#选择两个黑球，一个白球号码，并选择每注投注数量，黑球每注不得超过三个，可重复投注白球只能投注一个
#定义函数，返回一个列表
def num(): 
    b = set()    
    from random import randint
    while len(b) < 4:
        i = randint(1,10)
        b.add(i)
    b = sorted(b) # 转换为列表并排序
    n = randint(1,5)
    b.append(n)
    return b

#随机投注
print('投注号码:')
mynum = num()
print('黑球号码：',mynum[:4],'白球号码：',mynum[4])

#选择投注
blacknum = mynum[:4] 
whitenum = {mynum[4]} #白球不可重复
print()
choose = input('选择黑球投注号码[1~10], 用空格分隔: ')#以逗号分隔受到用户中英符号限制，故使用空格分隔
choose = choose.split(' ') #以空格为分隔符
# a = choose[0] 输入部分会被i遍历，因为输入的类型是字符串，不与i的整数类型相同，所以没有配对的对象
# b = choose[1]
a, b = map(int, choose)
a_1  = int(input(f'请输入{a}号黑球投注数量: '))
b_1  = int(input(f'请输入{b}号黑球投注数量: '))
white_choose = int(input('选择白球投注号码[1~5]: '))

#确定黑白球最终投注结果
blacknum.extend([a]*a_1+[b]*b_1) #append()会返回 None，保持扁平结构
print('最终黑球投注号码:',blacknum)
whitenum.add(white_choose)
print('最终白球投注号码:',whitenum)

#开奖
print()
print('开奖号码:')
lottery = num()
print('黑球号码：',lottery[:4],'白球号码：',lottery[4])

#匹配
lotteryok=lottery[:4]
times= 0
for i in blacknum:
    if i in lotteryok:
        times+=1
print('黑色球中奖数:',times)

whiteok = False
if lottery[4] in  whitenum :
    whiteok=True
    print('白色球中奖')
else:
    print('白色球未中奖')

#兑奖
if whiteok:
    if times >= 5:
        print('中一等奖！')
    elif times == 4:
        print('中三等奖！')
    elif times == 3:
        print('中五等奖！')
    else:
        print('未中奖！')
else:
    if times >= 5:
        print('中二等奖！')
    elif times == 4:
        print('中四等奖！')
    elif times == 3:
        print('中六等奖！')
    else:
        print('未中奖！')



        

import random

# 定义函数，返回一个列表
def generate_numbers():
    b = set()  # 使用集合避免重复
    while len(b) < 4:
        b.add(random.randint(1, 10))
    n = random.randint(1, 5)
    b = sorted(b)  # 转换为列表并排序
    b.append(n)
    return b

# 投注
try:
    print('投注号码:')
    mynum = generate_numbers()
    print(mynum)
    
    # 开奖
    print('开奖号码:')
    lottery = generate_numbers()
    print(lottery)
    
    # 匹配
    blackok = sum(1 for i in mynum[:4] if i in lottery[:4])  # 使用生成器表达式
    print('黑色球中奖数:', blackok)
    
    if mynum[4] == lottery[4]:
        print('白色球中奖')
    else:
        print('白色球未中奖')

except Exception as e:
    print('发生错误:', e)







