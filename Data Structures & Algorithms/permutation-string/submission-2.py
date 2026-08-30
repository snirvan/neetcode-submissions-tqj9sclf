class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use arrays to keep track of char count in s1 and s2
        # sliding window of constant size iterate through s2
        # comparing arrays everytime if match return True
        # if doesn't match remove count of s[l] and incrament again
        # if iterate through all of s2 and array no match 
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26 
        s2_count = [0] * 26 
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_count:
            return True
        
        l = 0 
        for r in range(len(s1),len(s2)):
            s2_count[ord(s2[l])-ord('a')] -= 1
            s2_count[ord(s2[r])-ord('a')] += 1

            if s1_count == s2_count:
                return True
            
            l+=1
        return False
        
        




        