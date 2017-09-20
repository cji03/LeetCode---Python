# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

# 二分搜索思想，关键是如何判断target位置来操纵左右指针移动。
# 1. mid > l 说明l-min是连续的，如果t在l, mid之间，移动右指针。
# 2. mid < l 说明mid-r是连续的，如果t在mid, r之间，移动左指针。

def search(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """
  if not nums:
    return -1
  l, r = 0, len(nums)-1
  while l<=r:
    mid=(l+r)/2
    if nums[mid]==target:
      return mid
    if nums[l]<=nums[mid]:
      if nums[l] <= target < nums[mid]:
        r=mid-1
      else:
        l=mid+1
    else:
      if nums[mid] < target <=nums[r]:
        l=mid+1
      else:
        r=mid-1
  else:
    return -1
