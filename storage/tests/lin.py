
'''
def cake():
   print('beets')
   def pie():
       print('sweets')
       return 'cake'
   return pie
chocolate = cake()
虽然没有显式地调用 pie() 函数，因此它不会打印 'sweets'，但仍然会有一些输出。
这是因为执行 cake() 函数时,print('beets') 这行代码会被执行，所以会输出 'beets
print(chocolate())
print()
print(chocolate())
print()
more_chocolate, more_cake = chocolate(), cake
print(more_chocolate)
def snake(x, y):
    if cake == more_cake:#比较函数地址
        return chocolate
    else:
        return x + y
print(snake(10, 20))
print(cake)
print(more_cake)
# print(snake(10, 20)())=print(chocolate())
print(snake(10, 20)())
print(22)
cake = 'cake'
print(snake(10, 20))


def total(*zrgs):
  ls = input(zrgs).spit()
  ls = list(ls)
  for i in range(1,n+1):
    for z in range(1,m+1):
      times = 0
      for a in range(1,n+1):
        for s in range(1,m+1):
          n_1 = (i-1)*m+z
          n_2 = (a-1)*m+s
          if int(ls[n_1])==int(ls[n_2]):
            if abs(i-z)==abs(a-s)>0:
              times+=1
          return times
print(total(3 2 1 2 2 3 3 2))


l = input()
k = int(input())
n = list(l)
i = 1
while i<=k:
    x = n.pop(0)
    n.append(x)
    i = i+1
for m in n:
    print(m,end="")

# 在代码的 for m in n: 循环中，变量 m 实际上是 n 中的每一个元素，
# 该元素是一个字符。尽管在 print(int(n[int(m)])) 中对 m 使用了 int(m)，
# 但是 m 在这之前并没有被转换成数字。

'''
def snake(x, y):
    x=8
    y=[9]
a=0
s=[1]
snake(a,s)
print(a,s)



