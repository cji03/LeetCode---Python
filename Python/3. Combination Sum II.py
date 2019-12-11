# Given a collection of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# using backtracking, DFS深度优先。
# 每个数只能用一次，所以每次递归index+1，寻找下一个数。

class Solution(object):
  def combinationSum2(self, nums, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res=[]
    nums.sort()
    self.dfs(nums, target, 0, [], res)
    return res
  
  def dfs(self, nums, target, index, path, res):
    if target == 0:
      res.append(path)
      return
    for i in xrange(index, len(nums)):
      if nums[i] > target:
        break
      if i>index and nums[i]==nums[i-1]:  # 关键部位：排除重复项目，在本次循环内，如果下一个数相同，则跳过，用 i>index 判断
        continue
      self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
