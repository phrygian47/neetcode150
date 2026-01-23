# Valid Anagram

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An **anagram** is a string that contains the exact same characters as another string, but the order of the strings can be different.

## Example 1

```python
Input: s = "racecar", t = "carrace"

Output: true
```

## Example 2

```python
Input: s = "jar", t = "jam"

Output: false
```

## Constraints:

- `s` and `t` consist of lowercase English letters.

# Solution 1

At first glance I thought this would be solved by sorting. And that is totally valid, if you sort both strings, if they are anagrams they will be equal. So you can use any sort function or algorithm you'd like, and compare the sorted strings. If they are equal to each other, return `true` otherwise, return `false`. Bonus points for a one line answer.

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

## Time & Space Complexity

Since this solution uses the sort function, the time complexity is held back by the sorting algorithm leading to a complexity of O(_n_ log _n_ + _m_ log _m_) with n being the length of string `s`, and m being the length of string `t`. The space complexity will depend on the sorting algorithm of choice.

# Solution 2

Looking at the recommended Time complexity for this problem I noticed it is O(n + m). This can’t be achieved using sorting alone so I had to think of what else I can use. Since we are looking for frequency of characters a hashmap or python dictionary works great in this case. If we create 2 hashmaps that count the frequency of each character in each string `s` or `t`, we can then compare those hashmaps and return `true` if they are equal, or `false` if not. To achieve this in O(n + m) time we loop through each string `s` and `t` separately, then each iteration insert the character as a key with a value of 1 if it is not in our hashmap, or increment the value of the hashmap key if it is. Finally we can compare each map and return the correct answer.

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for c in s:
            hash1[c] = hash1.get(c, 0) + 1
        for c in t:
            hash2[c] = hash2.get(c, 0) + 1
        return hash1 == hash2
```

## Time & Space Complexity

The time complexity for this algorithm is O(n + m), which we can simplify down to just O(n), where n is the length of both strings. While we do take extra memory for this, we can consider it O(1) extra memory as there are at most 26 characters that each string can be made from.

# Solution 3

This final solution I discovered from Neetcode. This was not a solution I found myself but it is very interesting and worth looking at. Since the problem guarantees only lowercase English letters, we can use a fixed array length of 26 like this: `count = [0] * 26`. Then we can map each character to an index in the array starting with `'a'` at index `0`. Then we can loop through both strings `s` and `t`, incrementing the count at the corresponding index for each character for string `s`, and then decrementing for string `t`. If the two strings are valid anagrams, then our array `count` should all be `0` as every increment is canceled out by the decrement. If there is a value not equal to `0` then we know that this is not a valid anagram and can return `false`. Otherwise return `true`. This solution also includes a check to save time making sure both strings are of equal length, as they cannot be anagrams if they are different lengths.

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
```

## Time & Space Complexity

This solution has the same time and space complexity of solution 2. It runs in O(n + m) time, and takes O(1) space as our array is a fixed length of 26.
