#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

# O(n^2)
def twoSum(nums, target):
  for index1, i in enumerate(nums):
    if i > target:
      continue
    for index2, j in enumerate(nums[index1+1:]):
      if i+j == target:
        return index1, index1+index2+1

# O(n)
# 将检索过的值存入map中，下面的搜索中可以直接检索map返回对应的值。

def twoSum2(nums, target):
  lookUp = {}
  for index, i in enumerate(nums):
    if target - i in lookUp:
      return lookUp[target - i], index
    lookUp[i] = index

print twoSum([0,4,3,0], 0)
