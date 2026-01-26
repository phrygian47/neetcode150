# Products of Array Except Self

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

## Solution

Intuitively you can solve this problem fairly easily using the division operator. You can find the product of the entire array, then populate an output array with the total product divided by the value that is found in `nums[i]`. However this problem specifically states to not use the `/` operator. You can also run into issues where `nums[i] == 0`. So the best way to solve this is with prefix and postfix product arrays. We can even go further and keep track of both within one output array. By keeping track of the prefix product, starting at 1, we can iterate through `nums` and store that prefix value at `output[i]`. Then update our prefix by multiplying it with the value at `nums[i]`. Using the same array used to store prefix products, we then initialize our `postfix = 1`, starting at the end of `nums`, we update the value in our output as `output[i] *= postfix`. Then we update our postfix value again by multiplying it with the value at `nums[i]`.

## Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
```

## Time & Space Complexity

Since we only ever iterate through the nums as 2 linear passes, this algorithm runs in O(2n) time, which simplifies to O(n) time while taking O(n) space for the output array.
