class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = TrieNode()
            curr = curr.children[x]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(index, root):
            curr = root

            for x in range(index, len(word)):
                if word[x] == ".":
                    for child in curr.children.values():
                        if dfs(x+1, child):
                            return True
                    return False
                else:
                    if word[x] not in curr.children:
                        return False
                    curr = curr.children[word[x]]
            
            return curr.word

        return dfs(0,self.root)


# dfs:
# if word[index] != ".":
    # if 
# base case:

        
