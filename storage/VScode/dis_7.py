# Q1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def draw(hand, positions):
    """Remove and return the items at positions from hand.

    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
   # return list(sorted( [hand.pop(i) for i in list(sorted(positions,reverse=True))],reverse=True) )
    return list(reversed( [hand.pop(i) for i in list(sorted(positions,reverse = True))]))
                #列表反转                             #列表倒序

#为什么positions要倒序排序            
"""
先逆序排序，避免移除元素后影响后续索引
这是因为列表的索引是从头到尾连续的。当你从列表末尾开始移除元素时，不会影响到前面元素的索引。
具体来说，移除元素的操作会改变列表的长度，如果从前面开始移除，每次移除后，后续元素的索引都会减 1,这会导致后续的移除操作出错。
而从末尾开始移除则不会影响前面元素的索引。
"""
# 反转 ： [...].reverse() 和 reversed([...])
"""
reverse() 函数的使用不正确:reverse() 不是 Python 内置的函数，而是列表对象的一个方法。因此，应该使用 [...].reverse() 而不是 reverse([...])。
但根据代码的意图，可能是想直接返回一个反转的列表，这时应该使用 reversed([...]) 或者 [...][::-1]
"""

# Q2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1

class Button:
    """A button on a keyboard.

    >>> f = lambda c: print(c, end='')  # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """
    caps_lock = CapsLock()

    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        """Call output on letter (maybe uppercased), then return the button that was pressed."""
        self.pressed += 1  #每次当我按下按钮的时候， press 都会增加一。
        "*** YOUR CODE HERE ***"
        if self.caps_lock.pressed % 2 == 0: #偶数小写，奇数大写
            now_letter = self.letter.lower()
        else:
            now_letter = self.letter.upper()
        self.output(now_letter)
        return self  #self.output(current_letter)

#为什么返回self，而不是self.output(current_letter)
'''返回 self ，就相当于每次调用 press 方法后返回的还是这个按钮(Button 实例）自身，
这样就能紧接着再次调用 press 方法，符合像上述连续多次调用 press 方法来模拟连续按键操作的使用场景要求。'''

class Keyboard(Button):
    """A keyboard.

    >>> Button.caps_lock.pressed = 0  # Reset the caps_lock key
    >>> bored = Keyboard()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o']
    >>> bored.keys['l'].pressed
    2

    >>> Button.caps_lock.press()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o', 'H', 'E', 'L', 'L', 'O']
    >>> bored.keys['l'].pressed
    4
    """
    def __init__(self):
    
        self.typed = []
        self.keys = {n:Button(n,self.add_to_typed)for n in LOWERCASE_LETTERS}  # Try a dictionary comprehension!试试字典理解
                                # 字典推导式，创建键值对，键是小写字母，值是Button实例，输出函数是add_to_typed 

    def type(self, word):
        """Press the button for each letter in word.
        按单词中每个字母的按钮。"""
        assert all([w in LOWERCASE_LETTERS for w in word]), 'word must be all lowercase单词必须全部小写'
        "*** YOUR CODE HERE ***"
        for i in word:
            self.keys[i].press()
    
    def add_to_typed(self,letter): #要另外定义一个函数，把letter加到typed列表中
        return self.typed.append(letter)
        
# Q3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Eye:
    """An eye.

    >>> Eye().draw()
    '0'
    >>> print(Eye(False).draw(), Eye(True).draw())
    0 -
    """
    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return '-'
        else:
            return '0'

class Bear:
    """A bear.

    >>> Bear().print()
    ? 0o0?
    """
    def __init__(self):
        self.nose_and_mouth = 'o'

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print('? ' + left.draw() + self.nose_and_mouth + right.draw() + '?')

# class SleepyBear(Bear):
#     """A bear with closed eyes.

#     >>> SleepyBear().print()
#     ? -o-?
#     """
#     "*** YOUR CODE HERE ***"
#     def next_eye(self): # Eye 是一个类，它并不是 SleepyBear 实例的属性（你用 self.Eye 这种写法是尝试当作属性去访问了）
#         #return self.Eye(False)
#         return Eye(False)
    

# class WinkingBear(Bear):
#     """A bear whose left eye is different from its right eye.

#     >>> WinkingBear().print()
#     ? -o0?
#     """
#     def __init__(self):
#         "*** YOUR CODE HERE ***"
#         #self.left_self_next_eye() = True 看起来像是在调用一个方法（因为有括号），而赋值操作的左边应该是一个合法的变量（比如普通的属性名称、通过点号访问的对象属性等），不能是方法调用的形式
#         self.left = True 
#         self.right= False

#     def next_eye(self):
#         "*** YOUR CODE HERE ***"
#         print('? ' + Eye(self.left) + self.nose_and_mouth + Eye(self.right) + '?')
        


class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ? -o-?
    """
    "*** YOUR CODE HERE ***"
    def next_eye(self):
        return Eye(True)

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ? -o0?
    """
    def __init__(self):
        "*** YOUR CODE HERE ***"
        self.count = 1
        self.nose_and_mouth = 'o'  #重新初始化,否则会显示是不存在的属性

    def next_eye(self):
        "*** YOUR CODE HERE ***"
        if self.count :
            self.count-=1
            return Eye(True)
        else:
            self.count+=1
            return Eye(False)

# 为什么 WinkingBear 类中 nose_and_mouth 变量重新初始化？
'''
实例属性查找:
-未定义__init__方法的情况
当子类没有定义__init__方法时,在创建子类实例时会自动调用父类的__init__方法。所以实例属性会按照父类__init__方法中的定义进行初始化,后续查找实例属性时，就像预期的那样可以找到这些在父类中初始化的属性。
-定义了__init__方法的情况
当子类定义了自己的__init__方法时,它会覆盖父类的__init__方法。在这种情况下,Python 在创建子类实例时,只会执行子类的__init__方法。
如果子类的__init__方法没有对某个实例属性进行初始化,并且在实例中找不到这个属性,那么在访问这个属性时就会报错,不会自动去父类中查找。但是,如果在子类的__init__方法中使用了super().__init__()语句,就会先执行父类的__init__方法,这样就可以初始化从父类继承的实例属性，然后在实例中就能正确地查找这些属性了。'''