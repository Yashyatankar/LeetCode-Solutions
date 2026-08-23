class Solution(object):
    def majorityElement(self, nums):
        maps = {}
        n = len(nums)
        max_number = n // 3

        for i in nums:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1

        result = []

        for num in maps:
            if maps[num] > max_number:
                result.append(num)

        return result