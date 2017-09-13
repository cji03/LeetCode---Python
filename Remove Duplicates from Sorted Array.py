# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the new length.

# 非常诡异的要求，不允许创建新的array，也不用删掉。
# 还是用了两个指针，一个读取（r）另一个记录写入位置（w），指针r从头向后读取，遇到不一样的数写入w位置，并且w+1，直到最后。

def removeDuplicates(n):
  if not n:
    return 0
  r, w = 1, 1
  while r < len(n):
    if n[r] != n[r-1]:
      n[w] = n[r]
      w+=1
    r+=1
  return w
