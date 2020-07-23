
"""
"""
"""
 找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
 eg：
         输入：
         [2, 3, 1, 0, 2, 5, 3]
         输出：2 或 3
"""
# 下面这种执行超时了
def findRepeatNumber_longTime(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums) - 1):
            if (nums[i] == nums[j]) & (i != j):
                return nums[i]
    return None


def findRepeatNumber(nums):
    return None
nums1 = [2, 3, 1, 0, 2, 5, 3]

print(findRepeatNumber(nums1))
