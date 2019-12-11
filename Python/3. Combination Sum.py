# Given a set of candidate numbers (C) (without duplicates) and a target number (T)
# find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]

# useing backtracking DFS深度优先。

class Solution(object):
  def combinationSum(self, nums, target):
    res=[]
    nums.sort()
    self.dfs(nums, target, 0, [], res)
    return res
  
  def dfs(self, nums, target, index, path, res):
    if target == 0:
      res.append(path)
      return
    for i in xrange(index, len(nums)):  # 从index开始，跳过之前的值避免重复结果。
      if nums[i] > target:  # 应为是sort过的，所以当前值大于target的话直接跳过当前循环。
        break
      self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

# 一个比较快的答案
class Solution(object):
def combinationSum(self, candidates, target):
    result = []
    candidates = sorted(candidates)
    
    def dfs(remain, stack):
        if remain == 0:
            result.append(stack)
            return 
        for item in candidates:
            if item > remain: break  # 来避免重复答案
            if stack and item < stack[-1]: continue
            else:
                dfs(remain - item, stack + [item])
    dfs(target, [])
    return result
