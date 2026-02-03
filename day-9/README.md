# Two Integer Sum II

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 < index2`. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

## Example

```python
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
```

## Constraints

- `2 <= numbers.length <= 1000`
- `-1000 <= numbers[i] <= 1000`
- `-1000 <= target <= 1000`

## My solution

The key to solving this problem is the understanding that the input array is sorted in non-decreasing order, meaning it is from lowest to highest. The other key is understanding 2 pointers. We start by initializing two pointers `l` and `r`, with `l` pointing to the start of the array `numbers` and `r` pointing to the end of the array `numbers`. We cannot use the same index twice, and we are guaranteed one solution, so we use a while loop to iterate as long as `l < r`. Through each iteration, we calculate `numbers[l] + numbers[r]`. If this value is greater than `target`, since we know the array is sorted, we simply decrement our pointer `r` to decrease the total as `numbers[r - 1] <= numbers[r]`. If it is less than `target`, we increment our left pointer `l` so that it increases the total. We do this until a solution is found. Once `numbers[l] + numbers[r] == target`, we return the values `[l + 1, r + 1]`. Note that the question specifies a 1-indexed array, so we add 1 to each of our pointers. Since we are guaranteed a solution we should never leave the loop.

## Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
```
