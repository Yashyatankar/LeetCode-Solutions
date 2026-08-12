class Solution(object):

    def lowerbound(self, nums, target):
        
        n = len(nums)

        l = 0
        r = n-1

        ans = n
        
        while l<=r:

            mid = (l+r)//2

            if nums[mid] >= target:

                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans

    def upperbound(self, nums, target):
        n = len(nums)

        l = 0
        r = n-1

        ans = n
        
        while l<=r:

            mid = (l+r)//2

            if nums[mid] > target:

                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ub = self.upperbound(nums, target)
        lb = self.lowerbound(nums, target)

        if ub==lb:

            return [-1,-1]

        else:
            return [lb, ub-1]