# 寻找一个数（基本的二分搜索） 向中间收缩，搜索一个数，如果存在，返回其索引，否则返回 -1。
def left_bound(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums)
    
    # 注意
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid

    return left
# 寻找左侧边界的二分搜索 
#完整代码如下： 左开右闭
def left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # 搜索区间为 [left, right]
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif nums[mid] == target:
            # 收缩右侧边界
            right = mid - 1
    
    # 判断 target 是否存在于 nums 中
    # 如果越界，target 肯定不存在，返回 -1
    if left < 0 or left >= len(nums):
        return -1
    
    # 判断一下 nums[left] 是不是 target
    return left if nums[left] == target else -1
 # 为什么 while 循环的条件是 <= 而不是 <？
''' 因为初始化 right 的赋值是 nums.length - 1,即最后一个元素的索引，而不是 nums.length。  '''
# target 不存在时返回什么？
''' 搜索左侧边界的二分搜索返回的索引是大于 target 的最小索引。  '''
# 为什么是 left = mid + 1 和 right = mid？
''' 因为我们的「搜索区间」是 [left, right) 左闭右开，所以当 nums[mid] 被检测之后，下一步应该去 mid 的左侧或者右侧区间搜索，即 [left, mid) 或 [mid + 1, right)。 '''
# 为什么该算法能够搜索左侧边界？
''' 关键在于对于 nums[mid] == target 这种情况的处理：
    if (nums[mid] == target)
        right = mid; '''
# 为什么返回 left 而不是 right？
''' 都是一样的，因为 while 终止的条件是 left == right '''

#####################################################################################

 # 寻找右侧边界的二分搜索
def right_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 注意
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 注意
    return left - 1

# 为什么 while 中是 < 而不是 <=？
'''因为 right = nums.length 而不是 nums.length - 1。因此每次循环的「搜索区间」是 [left, right) 左闭右开。'''
# 为什么这个算法能够找到右侧边界？
'''if (nums[mid] == target) {
    left = mid + 1;
}'''
 # 为什么返回 left - 1？
'''while 循环的终止条件是 left == right,所以 left 和 right 是一样的，你非要体现右侧的特点，返回 right - 1 好了。

至于为什么要减一，这是搜索右侧边界的一个特殊点，关键在锁定右边界时的这个条件判断：

// 增大 left,锁定右侧边界
if (nums[mid] == target) {
    left = mid + 1;
    // 这样想: mid = left - 1
} '''
#  nums[mid] > target时为什么不是 right = mid-1，mid不是已经被检查过了吗？
'''  因为搜索区间是左闭右开的 [left, right), while left < right 会使left到达right前一位
同理:elif nums[mid] < target: left = mid + 1 是由于left为闭区间
'''
# 如果 target 不存在时返回什么？
''' 如果 target 不存在，搜索右侧边界的二分搜索返回的索引是小于 target 的最大索引。'''
'''
#如果你想在 target 不存在时返回 -1
while left < right:
    # ...
# 判断 target 是否存在于 nums 中
# left - 1 索引越界的话 target 肯定不存在
if left - 1 < 0 or left - 1 >= len(nums):
    return -1
# 判断一下 nums[left - 1] 是不是 target
return left - 1 if nums[left - 1] == target else -1

# 左闭右闭
def right_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 这里改成收缩左侧边界即可
            left = mid + 1
    # 最后改成返回 left - 1
    if left - 1 < 0 or left - 1 >= len(nums):
        return -1
    return left - 1 if nums[left - 1] == target else -1
'''