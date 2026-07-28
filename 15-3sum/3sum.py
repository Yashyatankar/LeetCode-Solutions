class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # since sorted, if smallest is positive, no triplet can sum to 0
            if nums[i] > 0:
                break

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip duplicates for j and k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return res