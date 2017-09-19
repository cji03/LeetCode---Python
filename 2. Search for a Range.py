# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# 题目中提了时间复杂度是O(log n)，暗示我们用二分搜索做，刚开始我没注意，结果用了内置函数index()，然后答案也过了。
def searchRange(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  try:
    i = nums.index(target)
    j=i
    while j<len(nums) and nums[j]==target:
      j+=1
    return [i, j-1]
  except:
    return [-1, -1]

# 二分搜索的话：一位老哥用了tricky的方法，+-0.5来避免重复的问题。
class Solution:
# @param A, a list of integers
# @param target, an integer to be searched
# @return a list of length 2, [index1, index2]
def searchRange(self, arr, target):
  start = self.binary_search(arr, target-0.5)
  if arr[start] != target:
    return [-1, -1]
  arr.append(0)
  end = self.binary_search(arr, target+0.5)-1
  return [start, end]

def binary_search(self, arr, target):
  start, end = 0, len(arr)-1
  while start < end:
    mid = (start+end)//2
    if target < arr[mid]:
      end = mid
    else:
      start = mid+1
  return start
