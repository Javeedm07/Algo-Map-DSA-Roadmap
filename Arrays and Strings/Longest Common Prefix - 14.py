class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        ans = strs[0]
        for i in range(1, len(strs)):
            s = ""
            for j in range(len(ans)):
                if ans[j] == (strs[i])[j]:
                    s += ans[j]
                else:
                    ans = s
                    break
        return ans
