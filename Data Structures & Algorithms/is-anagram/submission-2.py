from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countsS = Counter(s)
        countsT = Counter(t)
        
        if countsS == countsT:
            return True
        else:
            return False
        
