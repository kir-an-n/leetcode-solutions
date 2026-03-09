# Problem 268 - Missing Number
# Given an array nums containing n distinct numbers in range [0, n],
# return the only number in the range that is missing.
# Example: [3,0,1] → 2
# Approach: Sum formula - expected sum minus actual sum gives missing number

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum