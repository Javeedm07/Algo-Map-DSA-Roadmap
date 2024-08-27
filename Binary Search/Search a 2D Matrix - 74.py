class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            mid_ele = matrix[i][j]
            if mid_ele == target:
                return True
            elif mid_ele > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
