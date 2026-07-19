class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        s = s.strip()
        n = len(s)
        
        c = 0

        
        
        while i>=(-1*n) and s[i] != " ":
            
            i-=1 
            c+=1

        return c

            
                