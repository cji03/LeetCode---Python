Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  const sortArray = nums.sort((a, b) => a - b);
  const result = [];

  for(let i=0; i<nums.length-2; i++) {
    if (sortArray[i] > 0) break
    if (sortArray[i] === sortArray[i-1]) continue
    let l = i + 1;
    let r = nums.length - 1;

    while(l<r) {
      const sum = sortArray[i]+sortArray[l]+sortArray[r];
      if(sum < 0) {
        l++
        while(sortArray[l] === sortArray[l-1]) l++
        continue
      }
      if(sum > 0) {
        r--
        while(sortArray[r] === sortArray[r+1]) r--
        continue
      }
      if(sum === 0) {
        result.push([sortArray[i], sortArray[l], sortArray[r]]);
        l++;
        r--;
        while(l<r && sortArray[l] === sortArray[l-1]) l++
        while(l<r && sortArray[r] === sortArray[r+1]) r--
      }
    }
  }

  return result;
};
```
