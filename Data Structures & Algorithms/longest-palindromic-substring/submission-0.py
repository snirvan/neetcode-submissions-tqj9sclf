class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_str = ''
        
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l + 1
                if length > longest:
                    longest = length
                    longest_str = s[l:r+1]
                l -= 1
                r += 1

            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r-l + 1
                if length > longest:
                    longest = length
                    longest_str = s[l:r+1]
                l -= 1
                r += 1

        return longest_str
        
            
