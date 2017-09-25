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
