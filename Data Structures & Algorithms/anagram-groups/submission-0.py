class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for char in word:
                i = ord(char) - ord('a')
                freq[i] += 1

            hm[tuple(freq)].append(word)

        return list(hm.values())