class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def rotate(self):
        for occ in range(self.k):
            last = self.nums.pop()
            self.nums.insert(0, last)
        return self.nums