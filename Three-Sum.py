# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# My first answer, it can finish the test, but exceed the time limit.
# I put my answer here for further improvement!

class Solution(object):
    @staticmethod
    def _twoSum2(nums, target):
        lookUp = {}
        res=set()
        for index, i in enumerate(nums):
            if target - i in lookUp:
                res.add(tuple([target - i, i]))
            lookUp[i] = index
        return list(res)

    def threeSum(self, nums):
        l=set()
        nums.sort()
        for i, a in enumerate(nums):
            twoS = self._twoSum2(nums[i+1:], 0-a)
            if twoS:
                for s in twoS:
                    l.add(tuple([a]+list(s)))
        return list(l)

# Like two pointer
# 先排序，然后一层for循环控制第一个pointer， 然后另外两个pointer从左和右向中间扫描。
# this answer isnt fast enough, runtime is about 2X of the fastest.

def threeSum(nums):
  nums.sort()
  res=[]
  for i in xrange(len(nums)-2):
    if i > 0 and nums[i]==nums[i-1]:  # 从第二个元素开始判断重复，e.g: [0, 0, 0]
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i]+nums[l]+nums[r]
      if s < 0:
        l+=1
      elif s > 0:
        r-=1
      else:
        res.append([nums[i], nums[l], nums[r]])
        l+=1
        r-=1
        while l < r and nums[l]==nums[l-1]:
          l+=1
        while l < r and nums[r]==nums[r+1]:
          r-=1
  return res
  
