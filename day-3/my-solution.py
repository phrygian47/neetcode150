class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[nums[i]] = i