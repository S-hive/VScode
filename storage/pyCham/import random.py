import random

'''选择两个黑球，一个白球号码，并选择每注投注数量，黑球每注不得超过三个，可重复投注白球只能投注一个'''

# 定义函数，返回一个包含黑球和白球的列表
def generate_numbers(): 
    b = set()
    while len(b) < 4:
        b.add(random.randint(1, 10))
    n = random.randint(1, 5)
    b = sorted(b)
    b.append(n)
    return b

# 随机投注
print('投注号码:')
mynum = generate_numbers()
print('黑球号码：', mynum[:4], '白球号码：', mynum[4])

# 选择投注
blacknum = mynum[:4] 
whitenum = {mynum[4]} # 白球不可重复

try:
    choose = input('选择两个黑球投注号码[1~10], 用空格分隔: ').split() # 输入并分隔
    a, b = map(int, choose) # 转换为整数
    a_1 = int(input(f'请输入{a}号黑球投注数量: '))
    b_1 = int(input(f'请输入{b}号黑球投注数量: '))
    white_choose = int(input('选择白球投注号码[1~5]: '))

    # 确定黑白球最终投注结果
    blacknum.extend([a] * a_1 + [b] * b_1)
    print('最终投注号码:', blacknum)
    whitenum.add(white_choose)

except ValueError:
    print('输入无效，请输入正确的数字。')
    exit()

# 开奖
print('\n开奖号码:')
lottery = generate_numbers()
print('黑球号码：', lottery[:4], '白球号码：', lottery[4])

# 匹配
blackok = sum(1 for i in blacknum if i in lottery[:4])  # 统计中奖黑球数量
print('黑色球中奖数:', blackok)

# 判断白球是否中奖
whiteok = lottery[4] in whitenum
print('白色球中奖' if whiteok else '白色球未中奖')

# 兑奖
print()
if whiteok:
    if blackok >= 5:
        print('中一等奖！')
    elif blackok == 4:
        print('中三等奖！')
    elif blackok == 3:
        print('中五等奖！')
    else:
        print('未中奖！')
else:
    if blackok >= 5:
        print('中二等奖！')
    elif blackok == 4:
        print('中四等奖！')
    elif blackok == 3:
        print('中六等奖！')
    else:
        print('未中奖！')
