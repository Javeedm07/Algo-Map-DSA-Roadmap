#1st approach - using list
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = list(magazine)
        for i in ransomNote:
            if i not in l:
                return False
            l.remove(i)
        return True
      
#2nd approach - using hash map
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = {}
        for i in magazine:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        for i in ransomNote:
            if i not in hmap:
                return False
            elif hmap[i] == 1:
                del hmap[i]
            else:
                hmap[i] -= 1
        return True
