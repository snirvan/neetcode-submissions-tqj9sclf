class Solution:

    def encode(self, strs: List[str]) -> str:
        codedStr = ''
        for word in strs:
            codedStr = codedStr + f'{len(word)}#{word}'
        return codedStr
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wLen = int(s[i:j])
            ans.append(s[j+1:j+wLen+1])
            i = j+wLen+1
        return ans

# * 
# 2#we3#say1#:
# i = 0
# j = 1
# wLen = 2  

# :

