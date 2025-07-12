
#用于创建一条双链表
class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
def createDoublyLinkedList(arr: List[int]) -> Optional[DoublyListNode]:
    if not arr:
        return None
    
    head = DoublyListNode(arr[0])
    cur = head
    
    # for 循环迭代创建双链表 (注意：不是递归，而是通过 循环（for 循环） 来构建链表)
    for val in arr[1:]:
        new_node = DoublyListNode(val) # 将下一个节点赋予实例属性
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next
    
    return head
'''-
! 每次for循环都会创建新的节点(1-6,16-20),不会执行 8-15行
[1,2,3]
第一次循环:
(\,1,\)
val = 1
head = cur = 1
// new_node = DoublyListNode(val)
(\,2,\)
val = 1

(\,1,->(\,2,\)
(\,1,<=>,2,\)
cur = (1,2,\)

#数组
把待删除的元素，先交换到数组尾部，然后再删除，数组尾部删除元素的时间复杂度是 O(1)。
删除数组头部元素，在 Python 中如果使用 pop(0) 方法，时间复杂度为 O(n)，因为删除头部元素后，后续元素都需要向前移动一位。

#二叉树的深度
1.计算二叉树的最大深度（高度）：是从根节点到最下方叶子节点经过的节点个数，这里算上根节点，是因为它是整个树结构的起始点，代表了树的第一层，是树深度的一部分。
2.计算某个节点的子树深度:比如计算根节点1的左子树深度,此时是以该节点的子节点作为子树的根节点来计算的。
'''

#####################################################################################

#二叉树(递归遍历 DFS)  先序遍历  中序遍历  后序遍历 
'''先序遍历：根节点 -> 左子树 -> 右子树
   中序遍历：左子树 -> 根节点 -> 右子树
   后序遍历：左子树 -> 右子树 -> 根节点'''
# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树的遍历框架
def traverse(root):
    if root is None:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置

'''
       1
      /  \
     2    3
     \   /  \
      4  5   6
preorderResult = [1 2 4 3 5 6]
inorderResult = [2 4 1 5 3 6]
postorderResult = [4 2 5 6 3 1]

前序位置的代码在刚刚进入一个二叉树节点的时候执行；
中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行。
后序位置的代码在将要离开一个二叉树节点的时候执行；

仔细观察，前中后序位置的代码，能力依次增强。
前序位置的代码只能从函数参数中获取父节点传递来的数据。
中序位置的代码不仅可以获取参数数据，还可以获取到左子树通过函数返回值传递回来的数据。
后序位置的代码最强，不仅可以获取参数数据，还可以同时获取到左右子树通过函数返回值传递回来的数据。
所以，某些情况下把代码移到后序位置效率最高；有些事情，只有后序位置的代码能做。
'''
######################################################################################

#二叉树(层序遍历 BFS)  按层次遍历二叉树，从上到下，从左到右。
#遍历输出所有节点
from collections import deque

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)

        # 把 cur 的左右子节点加入队列
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)
'''
      1
     /  \
    2    3
   /  \   /  \
  9    4  5   6
层序遍历结果为 [1, 2, 3, 9, 4, 5, 6]
'''
######################################################################################

# 改进版，记录当前遍历到的层数
from collections import deque

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1
    while q:
        sz = len(q)
        for i in range(sz):  #  处理头节点
            cur = q.popleft()
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            # 把 cur 的左右子节点加入队列
            if cur.left is not None:  #  处理子节点
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        depth += 1
'''
depth = 1, val = 3 
depth = 2, val = 9 
depth = 2, val = 20
depth = 3, val = 15
depth = 3, val = 7 
      3
    /   \
   9    20
      /  \
     15   7
'''
#####################################################################################

# 改进版，记录当前遍历到的层数，并记录每个节点的路径权重和（每层节点的权重和不同，+=1）
class State:
    def __init__(self, node, depth):  #多一个depth参数
        self.node = node
        self.depth = depth

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    # 根节点的路径权重和是 1
    q.append(State(root, 1))

    while q:
        cur = q.popleft()
        # 访问 cur 节点，同时知道它的路径权重和
        print(f"depth = {cur.depth}, val = {cur.node.val}")

        # 把 cur 的左右子节点加入队列
        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + 1))
'''
depth = 1, val = 3 
depth = 2, val = 9 
depth = 2, val = 20
depth = 3, val = 15
depth = 3, val = 7 
'''

# 为什么哈希表和常说的 Map 不是同一个东西
'''
1. Map 是“接口”：定义键值对的逻辑行为。

2. 哈希表是“实现”：一种高效实现 Map 的具体技术方案。

简而言之,Map 是“做什么”（功能规范），哈希表是“怎么做”（实现手段）。理解这一点有助于根据需求选择合适的数据结构（如需要快速访问选哈希表，需要有序性选树结构）。'''


# 二叉搜索树的keys 方法 : 
''' keys 方法返回所有键，且结果有序。可以利用 BST 的中序遍历结果有序的特性。'''
# 为什么不用前序遍历，这个结果不有序吗？
'''
    5
   / \
  3   7
 / \ / \
2  4 6  8
前序遍历：访问顺序是根节点 -> 左子树 -> 右子树。
前序遍历的顺序是 5 -> 3 -> 2 -> 4 -> 7 -> 6 -> 8,显然这个顺序不是按照键值从小到大排列的。

中序遍历：访问顺序是左子树 -> 根节点 -> 右子树
中序遍历结果是 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
'''
#######################################################################################
# 图结构
'''
在图的遍历中,visited数组和onPath数组(或on_path数组)的作用和区别如下：

1. 核心区别
onPath数组:
记录当前递归路径上经过的节点，用于避免路径成环。它允许节点在其他路径中被重复访问，但确保同一条路径中节点不重复。
例如,当寻找从A到D的所有路径时,若路径A→B→D和A→C→B→D均存在,B会在不同路径中被多次访问,但同一条路径中不会重复。

visited数组:
记录全局已访问过的节点，用于避免重复遍历整个图。一旦节点被标记为已访问，后续所有路径都不会再经过它。
例如,在常规DFS遍历中,每个节点只处理一次，无论有多少路径可达。

2. 应用场景
onPath数组:
用于寻找所有可能路径（如从起点到终点的所有路径）。它允许节点在不同路径中重复出现，但禁止同一路径中的循环。
visited数组:
用于遍历或搜索整个图（如判断连通性、拓扑排序等）。它确保每个节点只被处理一次。

3. 生命周期
onPath数组:
状态在递归过程中动态变化。每次递归进入节点时标记，退出时撤销（回溯），生命周期与递归栈一致。

visited数组:
状态一旦标记便不再改变（除非显式重置），生命周期覆盖整个遍历过程。


总结
特性	    onPath数组	           visited数组
目的	    防止当前路径成环	    防止重复遍历整个图
作用范围	当前递归路径	        全局
生命周期	动态回溯（标记后撤销）   永久标记（除非显式重置）
典型应用	寻找所有路径	        图的常规遍历(DFS/BFS)
重复访问	不同路径中允许	        完全禁止
'''

# 由于这里使用的 onPath 数组会在后序位置撤销标记，所以这个函数可能重复遍历图中的节点和边，解释一下
'''重复遍历的根本原因
假设图结构如下A 是起点,D 是终点）：
A → B → D  
A → C → D  
B → C
      A
     /  \
    C —— B
     \  /
       D

关键问题：
节点 B 和 C 会被不同路径多次访问。
边 A→B、A→C、B→C 等会被重复遍历。
边A → B, a → c, B → C ↓ ↓

示例代码的重复遍历过程遍历过程：

1. 首次递归路径:A → B → D
    onPath 标记 A、B、D。
    找到路径 [A, B, D]。
    回溯时依次撤销 D、B、A 的标记。
2.第二次递归路径:A → B → C → D
    从 B 继续遍历到 C(假设存在边 B→C)
    onPath 标记 A、B、C、D。
    找到路径 [A, B, C, D]。
    回溯时依次撤销标记。
3.第三次递归路径:A → C → D
    onPath 标记 A、C、D。
    找到路径 [A, C, D]。
    回溯时撤销标记。
4.第四次递归路径:A → C → B → D
    从 C 继续遍历到 B(假设存在边 C→B)
    onPath 标记 A、C、B、D。
    找到路径 [A, C, B, D]。
    回溯时撤销标记。

最终结果:
节点 B 和 C 被多次访问。
边 A→B、B→C、C→D 等被重复遍历。
'''
# 广度优先搜索（BFS）遍历图
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    q = deque(start)
    stop = 0

    while q:
        sz = len(q)
        for i in sz :
            cur = q[i]
            print(stop,cur)
            q.popleft()
            f = graph[cur]
            visited[cur] = True
            for n in f:
                if visited[n] == False:
                    q.append(n)
        stop += 1
    return -1


# 滑动窗口问题
# 如果题目中包含了至少等限定小号条件，则缩小窗口的条件是：
'''
 # 判断左侧窗口是否要收缩
            while right - left >= len(t):
                # 当窗口符合条件时，把起始索引加入 res
                if valid == len(need):
                    res.append(left)
'''
# 当可迭代对象为空时，使用 default 参数避免报错
empty_list = []
default_max = max(empty_list, default=0)
