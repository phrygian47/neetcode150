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