class TrieNode:
    def __init__ (self):
        self.node = {}
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur.node:
                cur.node[c] = TrieNode()
            cur = cur.node[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur.node:
                return False
            cur = cur.node[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur.node:
                return False
            cur = cur.node[c]
        return True
        