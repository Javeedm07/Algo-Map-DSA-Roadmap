class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's majority Algorithm
        count = 0
        for i in nums:
            if count == 0:
                count = 1
                maj = i
            elif i == maj:
                count += 1
            else:
                count -= 1
        return maj
