class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        # [0,1,3,0]

        # this will take len + 1 
        n = len(nums)
        count = 0

        for i in range(n):

            if nums[i] != count:
                return count

            count+=1

        return count
        
            
