# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 用了 Next lexicographical permutation algorithm 这么个算法。
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# 完全是自己的写法，速度只有30%，确实慢了一些。

# 在思考怎么写反转的时候，想到了reverse(),切片[::-1], 不是很确定这种操作会不会产生extra memory所有就写了while交换。
# 看别人的代码看到这么个操作，n[j+1:] = n[j+1:][::-1] 切片反转在赋值。

def nextPermutation(self, n):
  """
  :type nums: List[int]
  :rtype: void Do not return anything, modify nums in-place instead.
  """
  if len(n)<=1:
      return
  i, j=len(n)-2, len(n)-1
  while i>0:
      if n[i]>=n[i+1]:
          i-=1
      else:
          break
  while j>i:
      if n[j]>n[i]:
          n[i], n[j] = n[j], n[i]
          break
      else:
          j-=1
  i = i+1 if j>0 else i  # 在i的取值上思考克好一会儿，如何确定[3,2,1]这种递减的参数如何处理，最后是用j做判断。
  j=len(n)-1
  while i<j:
      n[i],n[j]=n[j], n[i]
      i+=1
      j-=1
