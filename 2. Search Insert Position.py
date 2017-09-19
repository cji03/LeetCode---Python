# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

# 我是用了内建函数index()来做了搜索。

def searchInsert(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """
  try:
    return nums.index(target)
  except:
    nums.append(target)
    nums.sort()
    return nums.index(target)

# 看到一个非常简洁的代码，思路很清奇。生成小于目标数的列表再取长度。不过复杂度上稍高一些。

def searchInsert(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """       
  return len([x for x in nums if x<target])

# 下面就是二分搜索做了。思路很清晰。

def searchInsert(nums, key):
  if key > nums[len(nums) - 1]:
    return len(nums)
  if key < nums[0]:
    return 0
  l, r = 0, len(nums) - 1
  while l <= r:
    m = (l + r)/2
    if nums[m] > key:
      r = m - 1
      if r >= 0:
        if nums[r] < key:
          return r + 1
      else:
        return 0
    elif nums[m] < key:
      l = m + 1
      if l < len(nums):
        if nums[l] > key:
          return l
      else:
        return len(nums)
    else:
      return m

# 优化简洁版本二分搜索。
def searchInsert(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = left + (right - left) / 2
    if nums[mid] >= target:
      right = mid - 1
    else:
      left = mid + 1
  return left
