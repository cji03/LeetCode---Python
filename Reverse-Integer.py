# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

# transfer to string and use slice[::-1]
# 32-bit  -1<<31 < n < (1<<31)-1

def reverse(self, n):
  if n>0:
    return int(str(n)[::-1]) if int(str(n)[::-1]) < (1<<31)-1 else 0
  else:
    return -int(str(-n)[::-1]) if -int(str(-n)[::-1]) > -1<<31 else 0
