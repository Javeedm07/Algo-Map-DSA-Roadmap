class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for i in set(stones):
            if i in jewels:
                c += stones.count(i)
        return c
