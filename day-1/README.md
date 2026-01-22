# Contains Duplicate

Given and integer array `nums`, return `true` if any value appears **more than once** in the array, otherwise return `false`

### Example 1:

```python
Input: nums = [1, 2, 3, 3]

Output: true
```

### Example 2:

```python
Input: nums = [1, 2, 3, 4]

Output: false
```

# Solution

This problem is fairly easy if you understand sets. You can brute force this solution with a nested for loop, checking each pair to see if any pairs match, then returning true if a match is found. However, this is a very inefficient algorithm that runs in O(n<sup><small>2</small></sup>) time. A much better solution would be to use a set. You can loop through the entire input array, adding each number to the set if it does not exist in the set. Since the lookup for sets is O(1) time due to hashing, the time complexity remains O(n). If you find the current value in the set, you instead return `true`. If you ever leave the loop, then no matches have been found and you can return `false`.

### Code

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for n in nums:
            if n in mySet:
                return True
            else:
                mySet.add(n)
        return False
```

# Solution 2

After reviewing some additional solutions, I found an interesting one line solution that I hadn't thought of. If a duplicate is found, then the length of the set created from the input would actually be smaller than the length of the input array itself. So a clever way to solve this is by comparing lengths, and returning true if the length of the set is not equal to the length of the input array.

### Code

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

# Time & Space Complexity

While both of these solutions runs at a much faster time complexity of O(n), it is important to note that they do take O(n) extra memory because of the set that is needed for this algorithm. So while the brute force solution only uses O(1) memory, it costs quadratic time making this is a worthwhile tradeoff.
