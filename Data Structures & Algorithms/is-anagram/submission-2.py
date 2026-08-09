class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = {}
        for char in s:
            hm[char] = hm.get(char,0) + 1

        for char in t:
            if char not in hm:
                return False
            
            hm[char] -= 1

            if hm[char] < 0:
                return False

        return sum(hm.values()) == 0