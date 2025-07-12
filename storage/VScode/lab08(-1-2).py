def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of its own
    label and all labels in the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    >>> otherTree = Tree(2, [Tree(1, [Tree(3), Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> cumulative_mul(otherTree)
    >>> otherTree
    Tree(5040, [Tree(60, [Tree(3), Tree(4), Tree(5)]), Tree(42, [Tree(7)])])
    """
    "*** YOUR CODE HERE ***"
    for i in t.branches:
        #while not i.is_leaf():
        cumulative_mul(i)
        if i.is_leaf():
            global num  #(1 test cases passed! No cases failed.)
            num = i.label
        num *= t.label
        t.label = num
########################################################################################
# num       
'''变量作用域问题:在cumulative_mul函数中,num变量在if语句块内定义,其作用域应该仅限于该if块内,
但是后续在if块外又使用了num进行乘法运算,会导致在if语句没有执行进入时(也就是当前遍历的分支不是叶子节点时)出现num未定义的错误。'''

    # for b in t.branches: (答案)
    #     cumulative_mul(b)  (会得到一个最底层的结果)
    #     t.label *= b.label

#他遍历到Tree(5)的时候没有t.branches不会报错吗
'''Tree(5) 是一个叶子节点，意味着它没有任何子分支。因此，执行到 for b in t.branches: 时,t.branches 是一个空列表（[]）。
由于没有分支,for b in t.branches: 循环不会被执行，因此不会对 Tree(5) 进行任何进一步的递归调用。这时，程序会跳过这个循环，并继续执行下一行代码。'''

'''  Tree(1)
    /      \
Tree(3)   Tree(7)
    |
Tree(5)
'''

# while not i.is_leaf():
'''即使下层子树递归到叶子节点处理完返回了,回来继续判断while循环条件时,这个i节点依然保持原来的状态(非叶子节点就还是非叶子节点，不会因为刚刚递归处理了下层就自动变成叶子节点了）
只要它一开始是非叶子节点,就会一直反复执行cumulative_mul(i)，不断进入递归而无法真正结束，最终导致无限递归。'''


def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest labels.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while len(t.branches) > n:
        # largest = max([t.branches], key = lambda t: t.label )
        largest = max(t.branches, key = lambda t: t.label )
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b, n)

# largest = max([t.branches], key = lambda t: t.label )
#这一行代码错误地将 t.branches 放入了一个列表中，导致 max 函数的参数实际上是一个包含单个元素（列表）的列表，而不是对列表中各个分支进行比较 
# 为什么？max([-7, 2, -1], key=abs)不是也可以比较吗？
'''t.branches返回一个列表  self.branches = list(branches) '''



def delete(t, x):
    """Remove all nodes labeled x below the root within Tree t. When a non-leaf
    node is deleted, the deleted node's children become children of its parent.

    The root node will never be removed.
    从树 t 中移除根节点以下所有标记为 x 的节点。当一个非叶节点被删除时，被删除节点的子节点将成为其父节点的子节点。根节点永远不会被移除。

    >>> t = Tree(3, [Tree(2, [Tree(2), Tree(2)]), Tree(2), Tree(2, [Tree(2, [Tree(2), Tree(2)])])])
    >>> delete(t, 2)
    >>> t
    Tree(3)
    >>> t = Tree(1, [Tree(2, [Tree(4, [Tree(2)]), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(4)])
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(2, [Tree(6),  Tree(2), Tree(7), Tree(8)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(6), Tree(7), Tree(8), Tree(4)])
    """
    new_branches = []
    for b in t.branches:
        delete(b, x)
        if b.label == x:
            #delete(b, x)
            new_branches.extend(b.branches)
        else:
            new_branches.append(b)
    t.branches = new_branches

#################################################################################3
# t = Tree(1, [Tree(2, [Tree(4, [Tree(2,[Tree(2)])]), Tree(5)])])
# delete(t, 2)
# print(t)

'''extend 是一个列表方法，用于将一个可迭代对象中的所有元素添加到现有列表的末尾。
与 append 方法不同,append 只会将可迭代对象作为一个单独的元素添加到列表中，而 extend 会将可迭代对象中的每个元素逐个添加。'''

# new_branches.extend(b.branches) 为什么b.branches里不会有x？
'''t.branches = new_branches  子节点被修改 '''


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    all = []
    for i in t.branches:
        max_path_sum(i)
        if i.is_leaf():
            global num
            num = i.label
        num += t.label
        all.append(num)
    mun = max(all)
    return mun
    
    if t.is_leaf():
      return t.label
    else:
      return t.label + max([max_path_sum(b) for b in t.branches])

class Tree:
    """A tree has a label and a list of branches.
        一棵树有一个标签和一个分支列表。
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

