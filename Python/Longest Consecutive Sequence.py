# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.

# 用了hashset, 取出一个数，抛掉，然后+1 —1看是否存在，如果存在计数+1并抛掉。最后返回最大的计数。（抛掉避免重复计算）
class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    ht=set(nums)
    res=1
    while ht:
      n=ht.pop()
      count=1
      l = n-1
      while l in ht:
         count+=1
         ht.remove(l)
         l-=1
      r=n+1
      while r in ht:
         count+=1
         ht.remove(r)
         r+=1
      res = max(res, count)
    return res

# board上比较6的一个答案，先去找左边界，找到后+1找右边界，完了左右一减得到，最后返回最大长度。

def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best
