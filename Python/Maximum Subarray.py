# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# 从第二个数开始，判断当前数与前一个数的大小，n[i]比较大保留当前，否则替换n[i]+n[i-1]。
# 可以计算出所有能连续相加得到的最大数。最后在列表里找最大的即可max()。

class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    for i in xrange(1, len(nums)):
      nums[i] = max(nums[i], nums[i]+nums[i-1])
    return max(nums)
