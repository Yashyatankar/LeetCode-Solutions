class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums)-1

        i = 0

        while i<=right:
            if nums[i] == 0:

                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp
                left+=1
                i+=1

            elif nums[i] == 1:

                i+=1

            else:

                temp = nums[i]
                nums[i] = nums[right]
                nums[right] = temp

                right-=1
            
