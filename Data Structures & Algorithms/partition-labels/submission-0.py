class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #x: 3           
        #y: 4
        #z: 7
        #b: 9
        #i: 10
        #s: 11
        #l 12
        #xyxxyzbzbbisl
        #         9
#end = 9
#res = [5,5]
#ls = 10


        chars = defaultdict(int)
        for i in range(len(s)):
            if s[i] in chars:
                if i > chars[s[i]]:
                    chars[s[i]] = i
            else:
                chars[s[i]] = i


        end = chars[s[0]]
        res = []
        last_split = 0
        for i in range(0,len(s)):
            if i == end:
                res.append(i - last_split+1)
                last_split = i+1
                if i+1 < len(s):
                    end = chars[s[i+1]]

            elif chars[s[i]] > end:
                end = chars[s[i]]
        
        return res
            

 

