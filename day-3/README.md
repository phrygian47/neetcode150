# Two Sum

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`

You may assume that _every_ input has exactly one pair of indices `i` and `j` that satisfy the condition. Return the answer with the smaller index first.

## Example 1

```python
Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
```

Explanation: `nums[0] + nums[1] == 7`, so we return `[0, 1]`.

## Example 2

```python
Input: nums = [4,5,6], target = 10

Output: [0,2]
```

## Constraints

- `2 <= nums.length <= 1000`
- `-10,000,000 <= nums[i] <= 10,000,000`
- `-10,000,000 <= target <= 10,000,000`
- Only **one** valid answer exists.

# Solution

You could very clearly and easily brute force this with a nested for loop, but that is O(n<sup><small>2</small></sup>). This question is clearly asking for something better. A faster approach is to use a hash map. We know that there is one combination of `nums[i] + nums[j] == target`. Doing some elementary algebra, we can also deduce that `target - nums[i] == nums[j]`. Using this knowledge we can use a hash map to store the value and indices of each value in `nums` (val -> index). For each `nums[i]`, we compute `diff = target - nums[i]`. If `diff` is already in the map, we’ve found the pair and return `[map[diff], i]`. Otherwise, we record `nums[i]` in the map as `map[nums[i]] = i` and continue. Because we only match against values seen earlier, the stored index is always smaller than the current index.

## Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[nums[i]] = i
```

## Time & Space Complexity

This algorithm runs in O(n) time where n is the size of the input array. This is because hash map lookup is O(1) and we only scan the array once. This solution does take O(n) extra memory as we need to create a hash map to store our previously seen values.

I have solved this problem before, so looking at the neetcode solution for this problem yielded no extra interesting solutions for me, as this is the most efficient way to solve this problem.
