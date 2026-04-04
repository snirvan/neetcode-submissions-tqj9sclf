class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = dict()
        for s in s1:
            s1_dict[s] = s1_dict.get(s,0) + 1
        
        l,r = 0, len(s1)-1

        s2_dict = dict()
        while r < len(s2):
            for s in s2[l:r+1]:
                s2_dict[s] = s2_dict.get(s,0) + 1
            if s1_dict == s2_dict:
                return True
            s2_dict.clear()
            l += 1
            r += 1

        return False
