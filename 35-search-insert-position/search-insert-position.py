class Solution(object):

    def lowerBound(self, nums, target):

        l = 0
        n = len(nums)
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

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.lowerBound(nums,target)
        
            