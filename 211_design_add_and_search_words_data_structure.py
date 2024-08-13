class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if not root:
                return False
            cur = root
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children:
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    k = ord(c) - ord("a")
                    if cur.children[k] == None:
                        return False
                    cur = cur.children[k]
            return cur.end

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
