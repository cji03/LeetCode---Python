Given a string, find the length of the longest substring without repeating characters.

```
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

主指针做遍历，次指针记录当前可连续`subArray`左边界；用`map`记录遇到过的字符；如果遇到出现过的字符且当前字符存在于`subArray`内，次指针前进至重复字符；每次遍历记录当前最大`subArray`长度；

```javascript
var lengthOfLongestSubstring = function(s) {
  if (s.length === 1) return 1;
  const map = new Map();
  let lp = 0;
  let maxl = 0;

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i]) && map.get(s[i]) >= lp) {
      lp = map.get(s[i]) + 1;
    }
    map.set(s[i], i)
    maxl = maxl > (i - lp) ? maxl : (i - lp + 1);
  }

  return maxl;
};
```
