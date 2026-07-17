class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])

        col_end = m-1
        row_end = n-1

        row_start = 0
        col_start = 0

        c = 0

        ans = []

        total = n*m

        while c<total:

            #row_start = col_start -> col_end

            for i in range(col_start, col_end + 1):
                ans.append(matrix[row_start][i])
                c+=1
            
            row_start+=1
                
            if c == total:
                break

            #col_end = row_start -> row_end

            for i in range(row_start, row_end+1):
                ans.append(matrix[i][col_end])
                c+=1
            col_end-=1

            if c == total:
                break

            #row_end = col_end -> col_start

            for i in range(col_end, col_start - 1, -1):
                ans.append(matrix[row_end][i])
                c+=1
            row_end-=1

            if c == total:
                break     

            #col_start = row_end -> row_start

            for i in range(row_end, row_start -1, -1):
                ans.append(matrix[i][col_start])
                c+=1    
            col_start +=1

            if c == total:
                break 

        return ans

            