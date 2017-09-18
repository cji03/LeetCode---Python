# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# 一开始写了 for+while 双循环去了，结果超时。还是用双指针操作。
class Solution(object):
  def maxArea(self, L):
    """
    :type L: List[int]
    :rtype: int
    """
    c, l, r = 0, 0, len(L)-1
    while l<r:
      if L[l]<L[r]:
        cn=L[l]*(r-l)
        l+=1   # 进一步优化的话，在这一步while判断L[l+1]<=L[l], l+=1, 将高度小于当前的快速过滤掉。
      else:
        cn=L[r]*(r-l)
        r-=1
      c=cn if cn>c else c  
    return c
