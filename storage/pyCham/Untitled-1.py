'''
num = int(input('请输入一个数字：'))
x = int(input("请输入你猜的数字?"))
times  = 1
while x != num :
    if x > num:
        print('谜底数字比你猜的要小')
        x = int(input('请输入你猜的数字?'))
        times += 1
    elif x < num:
        print('谜底数字比你猜的要大')
        x = int(input('请输入你猜的数字?'))
        times += 1
print(times)


x=a=int
while x < 10:
    while x != a:
        s = x*a
        print(f'{x}*{a}={s}',end=' ')
        a+=1
    if x==a:
        s=x*a
        print(f'{x}*{a}={s}',end="\n")
        x+=1

for x in range(1, 10):  
    for a in range(1, x + 1):  
        s = x * a
        print('{}*{}={}'.format(x,a,s),end=' ')
    print() 



for n in range(3,101):
    for x in range(1,n):
        while n % x !=0:
            print(x,n)   

'''
'''
times = 0
import math

for n in range (3,101): 
    result =int(math.sqrt(n)) + 1
    for x in range (1,result):
        if n % x == 0:
            break
    else:
        times +=1
        print(times,n)


import math

times = 0

times = 0
import math

for n in range (3,101): 
    result =int(math.sqrt(n))+1
    for x in range (1,result):
        if n % x == 0:
            break
    else:
        times +=1
        print(times,n)


for n in range(3, 101):
        result = int(math.sqrt(n)) + 1  # 计算到sqrt(n)，包括该值
  
        for x in range(2, result):  # 从2开始检查因数
            if n % x == 0:
                  # 找到因数，标记为合数
                break
        else:
            times += 1
            print(f'质数: {n}, 当前质数个数: {times}')

        
           

import math

for n in range (3,101): 
    result = int(math.sqrt(n))+1
    for x in range (2,result):
        if n % x == 0:
            break
    else:
         print(n)

times = 0
import math

for n in range (3,101): 
    result = int(math.sqrt(n))+1
    for x in range (2,result):
        if n % x == 0:
            break
    else:
        times +=1
        print('{}.{}'.format(times,n))



hei = eval(input(" "))
wei = eval(input(" "))
BMI = wei /(hei ** 2)
if BMI < 18.5:
    print("偏廋")
elif 18.5 <= BMI <24 :
    print("正常")
elif  24 <= BMI < 28:
    print("偏胖")
else: 
    print("肥胖")    

 

for x in range(1, 10):  
    for a in range(1, x + 1):  
        s = x * a
        print('{}*{}={}'.format(x,a,s),end=' ')
    print() 


for x in range(1, 10):  
    for a in range(1, x + 1):  
        if  x != a:
            s = x*a
            print(f'{x}*{a}={s}',end=' ')
            a+=1
            
        if x==a:
            s=x*a
            print(f'{x}*{a}={s}',end="\n")
      
'''
for x in range(1, 10):
    print(x)
    x+=1
    print(x)




hei = eval(input(" "))
wei = eval(input(" "))
BMI = wei /(hei ** 2)
if BMI < 18.5:
    print("偏廋")
elif 18.5 <= BMI <24 :
    print("正常")
elif  24 <= BMI < 28:
    print("偏胖")
else: 
    print("肥胖")        