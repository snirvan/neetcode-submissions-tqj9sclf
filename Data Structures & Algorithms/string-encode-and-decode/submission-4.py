class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        delimiter = "_"
        for word in strs:
            str_len = str(len(word))
            result += str_len
            result += delimiter
            result += word
        return result


            



    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "_":
                j+=1
            str_len = int(s[i:j])
            i = j+1
            j = i + str_len
            word = s[i:j]
            result.append(word)
            i = j
            
        return result

    #5_Hello5_World
