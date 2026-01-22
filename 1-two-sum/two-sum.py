class Solution(object):
    def twoSum(self, nums, target):
        # We use range(len(nums)) to get the index (i)
        for i in range(len(nums)):
            # We start the second loop from the next number
            for j in range(i + 1, len(nums)):
                # Check if the sum of numbers at index i and j equals target
                if nums[i] + nums[j] == target:
                    return [i, j]