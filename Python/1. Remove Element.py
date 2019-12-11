# Do not allocate extra space for another array, you must do this in place with constant memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given input array nums = [3,2,2,3], val = 3

# Your function should return length = 2, with the first two elements of nums being 2.

# 双指针，r到跟value不同的数，写到w处
def remv(nums, val):
  r, w = 0,0
  while r<len(nums):
    if nums[r] != val:
      nums[w]=nums[r]
      w+=1
    r+=1
  return w

# 看到一个有趣的代码，不过执行效率会比较低，可以到O(n^2)，内建函数，会删除遇到的第一个val
def removeElement(self, nums, val):
  try:
    while True:
      nums.remove(val)
  except:
    return len(nums)
