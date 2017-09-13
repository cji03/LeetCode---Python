# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# 跟3sum类似，需要遍历全部的说。
# 一开始在确定tmp初始值这个地方把自己绕了好久，一开始写在for里面，怎么测都有问题，后来发现应该拿出来放在外面，而且就把前三个值作为初始值就好了。

def threeSumClosest(self, n, target):
  n.sort()
  tmp=n[0]+n[1]+n[2]
  for i in xrange(len(n)-2):
    l, r = i+1, len(n)-1
    while l < r:
      s = n[i]+n[l]+n[r]
      if abs(target-s)-abs(target-tmp)<0:
        tmp = s
      if s < target:
        l+=1
      elif s > target:
        r-=1
      else:
        return s
  rern tmp
