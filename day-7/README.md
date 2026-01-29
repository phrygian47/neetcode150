# Longest Consecutive Sequence

Given an array of integers `nums`, return the _length_ of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

## Example 1:

```python
Input: nums = [2,20,4,10,3,4,5]

Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].
```

## Example 2:

```python
Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
# The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6]
```

Constraints

- `0 <= nums.length <= 1000`
- `-10^9 <= nums[i] <= 10^9`

# My solution

We could brute force this by checking each value and finding the length of each sequence starting with that value, however this leads to a lot of repetitive work and slow runtimes. A set helps us in this situation because of its O(1) lookup time, and we can eliminate a lot of repetition by finding a start of a sequence rather than checking each value. To find the start of a sequence there must be no values that are exactly 1 less in the set. So for each `n` in `numset`, we can check to see if `n - 1` exists in the numset, if it doesn't then we know we found the start of a sequence and can continue with our algorithm. We initialize a value to track the current sequence length `curr = 1`. We start at 1 because that is the smallest a sequence can be. Then while `n + 1` exists in `numset`, we can increment our `curr` value by 1 and increment `n` by one as well. Once `n + 1` is not found, we found the end of our sequence and find the `max(curr, longest)`.

# Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0
        for n in numset:
            if (n-1) not in numset:
                curr = 1
                while ((n + 1) in numset):
                    curr += 1
                    n += 1
                longest = max(curr, longest)
        return longest
```
