class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        mid = (l + r) // 2

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else: 
                break
        
        row = matrix[mid]
        l, r = 0, len(row) - 1
        rowMid = (l + r) // 2
        while l <= r:
            rowMid = (l + r) // 2
            print(rowMid)
            if target < row[rowMid]:
                r = rowMid - 1
            elif target > row[rowMid]:
                l = rowMid + 1
            else:
                return True
        return False