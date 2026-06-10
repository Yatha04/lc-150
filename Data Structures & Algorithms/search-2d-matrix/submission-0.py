class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #2 ways: either do one binary search through all the elements but for each row do int division to figure out
        #which row and col it's talking about. 
        #Or, do a binary search on the 0th element of each row to find the row and then do a binary search on that particular column



        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n

        while left < right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val > target:
                right = mid
            else:
                left = mid + 1
        return False