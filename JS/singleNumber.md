Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```
Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
```

#### 思路：我们可以利用二进制异或的性质来完成，将所有数字异或即得到唯一出现的数字。

1. 异或的性质 两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是 如果同一位的数字相同则为 0，不同则为 1
2. 异或的规律   
  a. 任何数和本身异或则为0   
  b. 任何数和 0 异或是本身


```javascript
var singleNumber = function(nums) {
  let res = 0;
  for(let i = 0; i < nums.length; i++) {
    res = res ^ nums[i];
  }

  return res;
};

var singleNumber = function(nums) {
  return nums.reduce((acc, curr) => acc ^ curr, 0)
};
```
