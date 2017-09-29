# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# 描述的很差劲，第一遍都没搞清楚要干什么。
# 用非空数组表示一个正整数，12 -> [1,2], 返回数字+1之后的数组 [1，3]
# 一开始的想法就是转换成数字，+1，在用列表生成回去，done！提交之后52ms发现在8%的位置，看来别人答案速度稍快点。

def plusOne(nums):
  num=0
  for i in xrange(len(nums)):
    num=num*10 + nums[i]
  return [int(i) for i in str(num+1)]

# 大多数答案都是直接操作数组的，<9直接+1，否则进一位之类的。
```Java
public int[] plusOne(int[] digits) {
        
    int n = digits.length;
    for(int i=n-1; i>=0; i--) {
        if(digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        
        digits[i] = 0;
    }
    
    int[] newNumber = new int [n+1];
    newNumber[0] = 1;
    
    return newNumber;
}
```
