class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        length = 0
        longest = 0

        for right in range(0,len(s)):
            curr = s[right]
            while(curr in seen):
                seen.remove(s[left])
                left += 1
                length -= 1
            seen.add(curr)
            length += 1
            longest = max(longest, length)
        
        return longest
            
            
        