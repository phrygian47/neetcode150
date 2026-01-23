class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for c in s:
            hash1[c] = hash1.get(c, 0) + 1
        for c in t:
            hash2[c] = hash2.get(c, 0) + 1
        return hash1 == hash2