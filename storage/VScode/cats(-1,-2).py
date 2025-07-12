"""Typing test implementation"""

from utils import (
    lower,
    split,
    remove_punctuation,
    lines_from_file,
    count,
    deep_convert_to_tuple,
)
from ucb import main, interact, trace
from datetime import datetime
import random


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):  # 返回符合select条件的第k个词，如果没有则返回空字符串
    """Return the Kth paragraph from PARAGRAPHS for which the SELECT returns True.
    If there are fewer than K such paragraphs, return an empty string.

    Arguments:
        paragraphs: a list of strings representing paragraphs
        select: a function that returns True for paragraphs that meet its criteria
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    ls = []
    for i in paragraphs:
        if select(i) :
            ls.append(i)
    if k >= len(ls):
        return ''
    else:
        return ls[k]


def about(subject):  #返回bool，判断输入单词是否在subject中
    """Return a function that takes in a paragraph and returns whether
    that paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), "subjects should be lowercase."

    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2
    import string #导入库
    def test(num):
        ls = []
        num = num.lower() #转换为小写字母
        num = remove_punctuation(num)
        #num.remove(n) 语句实际上尝试从字符串中移除字符，这是不可能的，因为字符串是不可变对象。
        # for n in num:
        #     #if n in string.punctuation:  #去除标点符号
        #     if n not in string.ascii_letters or None:
        #         ls_1.remove(n)  #字符串没有remove方法
        ls = num.split()
        for i in ls:
            if i in subject:
                return True 
        return False
    return test

#ls_1 = lambda x:ls.append(x.split()) ls_1被lambda绑定成一个函数，λ隐式返回None，修改了ls



def accuracy(typed, source):  #返回严格正确率
    """Return the accuracy (percentage of words typed correctly) of TYPED
    compared to the corresponding words in SOURCE.

    Arguments:
        typed: a string that may contain typos
        source: a model string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    from itertools import zip_longest
    if typed_words == source_words:
        return 100.0
    elif (len(typed_words) == 0 and len(source_words) != 0) or (len(typed_words) != 0 and len(source_words) == 0):
        return 0.0
    else:   
        all = 0
        max_one = len(typed_words)
        for a,s in zip_longest(typed_words,source_words):
            if a == s :
                all+=1
        if all == 0 :
            return 0.0
        else:
            num = all/max_one*100

            #to = 1
            # num_1 = num
            # while num_1 != int(num_1):  #保留到计算结果的后一位数(两种方法都行)
            #     num_1 = num_1*10
            #     to += 1
            # n = round(num,to)
            # return n

            n = float(num)    
            return n
        
#print( accuracy("a b \tc" , "a b c") ) #制表符会被自动忽略
'''
zip函数会将多个可迭代对象(如列表）中对应的元素打包成一个个元组，直到最短的可迭代对象耗尽为止
从itertools模块导入的zip_longest函数,它会按照索引位置匹配元素,当较短的列表元素耗尽后,会用指定的填充值(默认为None）填充较短列表的位置，继续遍历，直到最长的可迭代对象中的元素全部处理完
round() 函数用于四舍五入，但请注意，它返回的是数字而不是字符串。如果你想保留四位小数且需要输出为浮点数，可以这样做

'''



def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, "Elapsed time must be positive"
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    sixty_num = float(elapsed)/60 #20=20.0
    all_num = len(typed)
    ratio_num = all_num/5
    return float(ratio_num/sixty_num)



################
# Phase 4 (EC) #
################


def memo(f):
    """A general memoization decorator."""
    cache = {}

    def memoized(*args):
        immutable_args = deep_convert_to_tuple(args)  # convert *args into a tuple representation
        if immutable_args not in cache:
            result = f(*immutable_args)
            cache[immutable_args] = result
            return result
        return cache[immutable_args]

    return memoized


def memo_diff(diff_function):
    """A memoization function."""
    cache = {}

    def memoized(typed, source, limit):
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        # END PROBLEM EC

    return memoized


###########
# Phase 2 #
###########


def autocorrect(typed_word, word_list, diff_function, limit): #返回最接近typed_word的word_list中的词，如果没有则返回typed_word
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD based on DIFF_FUNCTION. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, return TYPED_WORD instead.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    #min_one = int(diff_function(typed_word,word_list[-1], limit))
   #min_list = word_list[-1]   全局变量会被下面应用，for语句被架空
   # for i in range(0,len(word_list),-1): 不会进行遍历，会直接返回最后一个元素 range（开始，结束，步长）
    
    # for i in range(len(word_list),1,-1):
    #     if int(diff_function(typed_word,word_list[i-1], limit))<= min_one:
    #         min_one_1 = int(diff_function(typed_word,word_list[i-1], limit))
    #         min_list_1 = i
    #     else:
    #         min_list_1 = len(word_list)-1
    #         min_one_1 = int(min_one)

    dis = {}
    if typed_word in word_list:
        return typed_word
    if len(word_list) == 1:
        min_1 = num = int(diff_function(typed_word,word_list[0], limit))
        dis[num] = 0
    elif len(word_list) > 1:
        for i in range(0,len(word_list)):
            num = int(diff_function(typed_word,word_list[i], limit))
            dis[i] = num  #注意字典的值不能相同，否则会覆盖
        min_list = min(dis.values()) #“list.index” 在 Python 中是列表（list）的一个方法。它用于返回列表中某个特定元素第一次出现的索引位置。例如       
        list_end = []
        for key,value in dis.items():
            if value == min_list:
                list_end.append(key)#返回列表中最小的元素，如果有相同元素，则返回第一个。
            else:
                continue
            min_1 = min(list_end)
            if int(diff_function(typed_word,word_list[min_1], limit))> int(limit):
                return typed_word
            else:
                return  word_list[min_1]

    if int(min_1 )> int(limit):
        return typed_word
    else:
        return  word_list[dis[num]]



def furry_fixes(typed, source, limit):#返回typed与source的差异数
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    #assert False, 'Remove this line'
    # END PROBLEM 6
    def furry_diff(typed, source, limit,same=0):   
        limit = int(limit)
        typed = list(typed)
        source = list(source)
        #same = 0  每一次递归都会初始化，所以这里初始化为0，导致错误,可以通过自定义函数默认参数来解决
        if same > limit:
            return same
        elif len(typed) ==0 or  len(source)==0:
            num = abs(len(typed) - len(source))
            return num + same
        elif typed[0] != source[0]:
            same += 1
        typed.remove(typed[0])
        source.remove(source[0])
        return furry_diff(typed, source, limit,same)
    return furry_diff(typed, source, limit,same=0)
# big_limit = 10
# print(furry_fixes("car", "cad", big_limit))


def minimum_mewtations(typed, source, limit):
    """A diff function for autocorrect that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if typed == source:
        return 0
    if limit <  0:
        return 1
    if len(typed) == 0 or len(source) == 0:
        return abs(len(typed) - len(source))
    if len(typed) == 1 and len(source) == 1:
        if typed == source:
            return 0
        else:
            return 1
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
    if typed[0] == source[0]:
        return minimum_mewtations(typed[1:], source[1:], limit) 
    else:
        add = minimum_mewtations(typed[:], source[1:], limit-1)+1
        remove = minimum_mewtations(typed[1:], source[:], limit-1)+1
        substitute = minimum_mewtations(typed[1:], source[1:], limit-1)+1
        return min(add, remove, substitute)
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END


#     if typed == source:
#         return 0
#     if limit <  0:
#         return 1
#     if len(typed) == 0 or len(source) == 0:
#         return abs(len(typed) - len(source))
#     if len(typed) == 1 and len(source) == 1:
#         if typed == source:
#             return 0
#         else:
#             return 1
#     if str(typed) in str(source):
#         return len(source) - len(typed)
#     else:
#         typed = list(typed)
#         source = list(source)
#         if typed[0]!= source[0]:

#             if  typed[1] == source[0]:#删除
#                 return minimum_mewtations(typed[1:], source[:], limit-1)+1
#             elif typed[1] == source[1]:#替换
#                 return minimum_mewtations(typed[1:], source[1:], limit-1)+1
#             elif typed[0] == source[1]:#插入
#                 return minimum_mewtations(typed[:], source[1:], limit-1)+1
#         else:
#             return minimum_mewtations(typed[1:], source[1:], limit) 
        
# big_limit = 10
# print(minimum_mewtations("tesng", "testing", big_limit) )
'''不用判断用哪个add remove substitute,直接调用即可'''

# Ignore the line below
minimum_mewtations = count(minimum_mewtations)


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, "Remove this line to use your final_diff function."


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8
    num = 0
    for i in source:
        if i in typed:
            num+=1
        else:
            break
    upload ({'id': user_id, 'progress': num/len(source)})
    return num/len(source)


def time_per_word(words, timestamps_per_player):
    """Return a dictionary {'words': words, 'times': times} where times
    is a list of lists that stores the durations it took each player to type
    each word in words.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time the
                          player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> result = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> result['words']
    ['collar', 'plush', 'blush', 'repute']
    >>> result['times']
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    tpp = timestamps_per_player  # A shorter name (for convenience)
    # BEGIN PROBLEM 9
    times = []  # You may remove this line
    # END PROBLEM 9
    num = len(tpp[0])
    all = len(tpp)
    #list_1 = list_2 = [] list_1 = list_2  两个列表的值会混乱，不能直接赋值，需要重新定义
    list_1 = []
    for n in range(all):
        for i in range(1,num):
            list_1.append(tpp[n][i]-tpp[n][i-1])
        times.extend([list_1])
        list_1 = []
    return {'words': words, 'times': times}

def fastest_words(words_and_times):
    """Return a list of lists indicating which words each player typed fastests.

    Arguments:
        words_and_times: a dictionary {'words': words, 'times': times} where
        words is a list of the words typed and times is a list of lists of times
        spent by each player typing each word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    check_words_and_times(words_and_times)  # verify that the input is properly formed
    words, times = words_and_times['words'], words_and_times['times']
    player_indices = range(len(times))  # contains an *index* for each player
    word_indices = range(len(words))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 10
    n = max(times[0])
    all = {}
    for j in player_indices:
        if min(times[j]) < n:
            min_people_1 = j
    for i in word_indices: #单词索引,返回数字
        for n in player_indices:  #玩家索引,返回数字
            min_people = 0
            num = 0
            if times[n][i] < times[0][i] or times[n][i] > times[0][i]: #找出玩家最小时间数
                num+=1
                if times[n][i] < times[0][i]:
                    min_people = n
                all[words[i]] = min_people             
        if num>1:
            min_people=min_people_1
            all[words[i]] = min_people  
        #all[words[i]] = n #构建字典，键为单词，值为玩家索引  # n总是为一（遍历）
        
    total = []
    for m in player_indices:  #遍历字典，返回玩家索引对应的单词
        list = []
        for k ,v in all.items(): 
            if v == m:
                list.append(k)
        total.extend([list])
    return total
        
    
'''
dis={'a': [1,2,3,4,5,5]}
dis['a'][2]  #3
'''



            


def check_words_and_times(words_and_times):
    """Check that words_and_times is a {'words': words, 'times': times} dictionary
    in which each element of times is a list of numbers the same length as words.
    """
    assert 'words' in words_and_times and 'times' in words_and_times and len(words_and_times) == 2
    words, times = words_and_times['words'], words_and_times['times']
    assert all([type(w) == str for w in words]), "words should be a list of strings"
    assert all([type(t) == list for t in times]), "times should be a list of lists"
    assert all([isinstance(i, (int, float)) for t in times for i in t]), "times lists should contain numbers"
    assert all([len(t) == len(words) for t in times]), "There should be one word per time."


def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
    num_players = len(times)
    num_words = len(times[0])
    assert word_index < len(times[0]), f"word_index {word_index} outside of 0 to {num_words-1}"
    assert player_num < len(times), f"player_num {player_num} outside of 0 to {num_players-1}"
    return times[player_num][word_index]


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file("data/sample_paragraphs.txt")
    random.shuffle(paragraphs)
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print("No more paragraphs about", topics, "are available.")
            return
        print("Type the following paragraph and then press enter/return.")
        print("If you only type part of it, you will be scored only on that part.\n")
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print("Goodbye.")
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print("Words per minute:", wpm(typed, elapsed))
        print("Accuracy:        ", accuracy(typed, source))

        print("\nPress enter/return for the next paragraph or type q to quit.")
        if input().strip() == "q":
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)