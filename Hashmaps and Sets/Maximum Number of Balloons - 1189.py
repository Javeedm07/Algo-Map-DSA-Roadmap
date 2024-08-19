class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = defaultdict(int)
        for i in text:
            hmap[i] += 1
        if any(c not in hmap for c in "balloon"):
            return 0
        else:
            return min(hmap['b'], hmap['a'], hmap['l']//2, hmap['o']//2, hmap['n'])
