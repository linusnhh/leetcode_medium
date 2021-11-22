class Solution:
    def __init__(self, nums, k, s):
        self.nums = nums
        self.k = k
        self.s = s

    def rotate(self):
        for occ in range(self.k):
            last = self.nums.pop()
            self.nums.insert(0, last)
        return self.nums

    def lengthOfLongestSubstring(self):
        seen = {}
        maximum_length = 0
        start = 0
        for occ in range(len(self.s)):
            if self.s[occ] in seen:
                start = max(start, seen[self.s[occ]] + 1)
            seen[self.s[occ]] = occ
            maximum_length = max(maximum_length, occ - start + 1)
        return maximum_length
