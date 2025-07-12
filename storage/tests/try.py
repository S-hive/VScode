class Solution:
    # 计算数组 nums 中所有和为 target 的三元组
    def threeSumTarget(self, nums, target):
        # 数组得排个序
        nums.sort()
        n = len(nums)
        res = []
        # 穷举 threeSum 的第一个数
        for i in range(n):
            # 对 target - nums[i] 计算 twoSum
            tuples = self.twoSumTarget(nums, i + 1, target - nums[i])
            # 如果存在满足条件的二元组，再加上 nums[i] 就是结果三元组
            for tuple in tuples:
                tuple.append(nums[i])
                res.append(tuple)
            # 跳过第一个数字重复的情况，否则会出现重复结果
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
        return res

    # 从 nums[start] 开始，计算有序数组 nums 中所有和为 target 的二元组
    def twoSumTarget(self, nums, start, target):
        # 左指针改为从 start 开始，其他不变
        lo = start
        hi = len(nums) - 1
        res = []
        while lo < hi:
            ...
        return res
n = Solution()
print(n.threeSumTarget([0,0,0,0],0)) 
