class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = dict()
        longest = 0

        left = 0
        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right],0) + 1
            while (right - left + 1) - max(charCount.values(), default=0) > k:
                charCount[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1 )

        return longest
        

            

        