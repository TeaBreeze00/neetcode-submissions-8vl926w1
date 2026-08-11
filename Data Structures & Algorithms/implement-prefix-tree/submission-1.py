class PrefixTree:
    # We'll start our implementation with a nested hashmap which has the easiest implementation.

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie # pointer to the current nested dict, initialized to the mother trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['.'] = '.'        

    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]

        return '.' in d # if the word ends and has a period key!
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True
        
        