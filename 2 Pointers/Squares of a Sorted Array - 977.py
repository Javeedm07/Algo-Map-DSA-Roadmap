class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for i in nums:
            squares.append(i**2)
        return sorted(squares)
