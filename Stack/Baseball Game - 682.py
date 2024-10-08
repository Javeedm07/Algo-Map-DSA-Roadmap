class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in operations:
            if i == 'C':
                ans.pop()
            elif i == 'D':
                ans.append(ans[-1] * 2)
            elif i == '+':
                ans.append(ans[-1] + ans[-2])
            elif int(i) == float(i):
                ans.append(int(i))
        return sum(ans)
