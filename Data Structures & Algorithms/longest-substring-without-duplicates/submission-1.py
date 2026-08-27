class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxCount = 0
        seen = set()
        l = 0 
        for r in range(len(s)):
            if s[r] not in seen:
                count += 1
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    count -= 1
                
                count += 1
                seen.add(s[r])

            maxCount = max(count, maxCount)

        return maxCount
                
