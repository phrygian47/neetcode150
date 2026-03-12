# Container With Most Water

You are given an integer array `heights` where `heights[i]` represents the height of the _i<sup>th</sup>_ bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

## Exmaple 1

```
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
```

## Example 2
```
Input: height = [2,2,2]

Output: 4
```

## Constraints
- `2 <= height.length <= 1000`
- `0 <= height[i] <= 1000`

# My Solution

This problem is easily brute forceable by checking every pair for every index. When checking a pair, we find the area of the water filling the space between the pairs by taking the lowest value `[i, j]` 
and multiplying it by the difference between the two indices. This approach works, but is very time inefficient, taking O(n<sup>2</sup>) time to complete

A better solution is to use two pointers. We initialize a pointer at the start and end of the array so that we start with the widest possible container. Then we calculate the area similary as before, and then increment or decrement the left or right pointer
depending on which is smaller. We always want to use the smaller value, as changing the biggest value will potentialy keep the height the same but decrease the width

## Code

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        ans = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            ans = max(curr, ans)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans
````
