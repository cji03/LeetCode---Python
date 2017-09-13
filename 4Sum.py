# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# 基本思想和3Sum一样，拿一个数，开始3Sum。
# 方法中加入了过滤，所以执行非常快。
# 1. A太大，退出：（如果4*A > target）
# 2. A太小，跳过：（A+3*MAx < target）
# 3. 确定A后求BCD的3SUM问题
# 4. B太大，退出：（如果3*B > target）
# 5. B太小，跳过：（B+2*MAx < target

def fourSum(n, target):
  n.sort()
  res=[]
  for i in xrange(len(n)-3):
    if 4*n[i]>target:   # 判断A过大
      break
    if n[i]+3*n[len(n)-1] < target:  # 判断A过小
      continue
    if i>0 and n[i]==n[i-1]:
      continue
    target_i = target - n[i]
    for j in xrange(i+1, len(n)-2):
      if 3*n[j]>target_i:  # 判断B过大
        break
      if n[j]+2*n[len(n)-1] < target_i:  #判断B过小
        continue
      if j>i+1 and n[j]==n[j-1]:   # 这里j要从i+1开始判断，一开始还是写的1，结果就出问题了。
        continue
      l, r = j+1, len(n)-1
      while l<r:
        s = n[j]+n[l]+n[r]
        if s<target_i:
          l+=1
        elif s>target_i:
          r-=1
        else:
          res.append([n[i],n[j],n[l],n[r]])
          l+=1
          r-=1
          while l<r and n[l]==n[l-1]:
            l+=1
          while l<r and n[r]==n[r+1]:
            r-=1
  return res
