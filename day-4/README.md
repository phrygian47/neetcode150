# Group Anagrams

Given an array of strings `strs`, group all _anagrams_ together into sublists. You may return the output in **any order**.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Example 1:

```python
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

## Example 2:

```python
Input: strs = ["x"]

Output: [["x"]]
```

## Example 3:

```python
Input: strs = [""]

Output: [[""]]
```

## Constraints

- `1 <= strs.length <= 1000`
- `0 <= strs[i].length <= 100`
- `strs[i]` is made up of lowercase English letters.

# Solution

I had the benefit of attempting this problem right after another previous problem, valid anagrams. As a result I immediately thought of the importance of using only lowercase English letters. To take advantage of this we can map each lowercase letter to an index in an array with a fixed length of 26. `'a'` would be index `0`, `'b'` is index `1` etc. We can utilize this to find which strings are anagrams, and this fixed array can act as a key for a hash map, with the value being a list of the strings. Since arrays in Python are unhashable, we must first convert the key array to a tuple. Doing this will group strings by the frequency of each character in the string, and we can return the values of this hash map as a list to find our solution.

## Code

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams.setdefault(tuple(key), []).append(s)
        return list(anagrams.values())
```

One mistake that I made that took some debugging to figure out is the difference between the `.get(key, default)` and `.setdefault(key, default)` dictionary methods. `.get()` returns a default but doesn’t insert it into the dictionary. So `anagrams.get(key, []).append(s)` will not work as it appends to a temporary list and the result does not persist or get stored. Instead, using `.setdefault()` will insert that default into the dictionary, allowing you to append the strings to the list value. You are also welcome to use `collections.defaultdict(list)` as an option, which makes this even more readable, but I’m avoiding it to keep dependencies minimal.

## Time & Space Complexity

This algorithm runs in O(m _ n) time where `m` is the number of strings and `n` is the length of the longest string. This avoids sorting, which would cost O(m _ n log n) time. The hashmap uses O(m) extra space for the dictionary, and the output itself takes O(m \* n) space overall.
