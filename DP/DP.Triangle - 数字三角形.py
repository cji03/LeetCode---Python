# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# 问题描述
# 给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。
# 
#    [2],
#   [3,4],
#  [6,5,7],
# [4,1,8,3]
# 从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

# 走到i，j就只有两种情况，一种是从i-1,j-1过来，一种是从i-1,j过来。
# 找到状态转移方程：dp[i][j] = Math.min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j];

triangle=\
[  [2],
  [3,4],
 [6,5,7],
[4,1,8,3]]

def miniTotal(triangle):
  dp=[[0]*len(triangle) for i in xrange(len(triangle))]
  dp[0][0] = triangle[0][0]
  for i in xrange(1, len(triangle)):
    for j in xrange(len(triangle[i])):
      l=max(j-1, 0)
      r=min(j, len(triangle[i-1])-1)
      dp[i][j]=min(dp[i-1][l], dp[i-1][r])+triangle[i][j]
  return min(dp[len(triangle)-1])

# board上其他变种答案
# Modify the original triangle, top-down
def minimumTotal2(self, triangle):
    if not triangle:
        return 
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    return min(triangle[-1])
    
# Modify the original triangle, bottom-up
def minimumTotal3(self, triangle):
    if not triangle:
        return 
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

# bottom-up, O(n) space
def minimumTotal(self, triangle):
    if not triangle:
        return 
    res = triangle[-1]
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    return res[0]
