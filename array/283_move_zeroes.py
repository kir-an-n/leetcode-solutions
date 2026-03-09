# Problem 283 - Move Zeroes
# Given an array, move all zeros to the end while maintaining order
# Example: [0,1,0,3,12] → [1,3,12,0,0]
# Approach: Use a position pointer to place non-zeros, then fill rest with zeros

class Solution:
    def moveZeroes(self, nums):
        position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[position] = nums[i]
                position += 1
        while position < len(nums):
            nums[position] = 0
            position += 1