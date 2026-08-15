class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        l = 0
        r = x
        ans = 1

        while l<=r:
            
            mid = (l+r)//2
            squre = mid*mid

            if squre > x:

                r = mid-1
            else:
                ans = mid
                l = mid+1

        return ans 