class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        mid = (l + r) // 2

        while l <= r:
            mid = (l + r) // 2
            if target not in matrix[mid]:
                if target < matrix[mid][0]:
                    r = mid - 1
                elif target > matrix[mid][-1]:
                    l = mid + 1
                else:
                    return False
            else: 
                return True
        return False