class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maps = dict({})

        for i in nums:
            
            if i in maps:

                maps[i] += 1
                return True
            else:
                maps[i] = 1

        return False
            
            
            