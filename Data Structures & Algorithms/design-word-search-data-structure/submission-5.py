class WordDictionary:

    def __init__(self):
        self.trie = {}
    
    # This will be the format of the trie: day -> {d:{a:{y:{.:.}}}}
    # 
    def addWord(self, word: str) -> None:
        d = self.trie # reference to the trie so that I can manipulate it
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['.'] = '.' # This is the stopping condition for each word       
    
# Okay, so here is the plan, I can do this iteratively with when I see a wildcard, I can iteratively search through all the possible subtrees and then look for a match. Otherwise, I can do a backtracking dfs search to search up all of the trees recursively. Let's see how this plays out. Backtracking makes sense here because when I see any wildcard, I need to try out brute force search of all of the subtrees which backtracking is good at. And why not just dfs? Because DFS only allows you to visit all nodes in the graph not undo stuff and brute force.

    def search(self, word: str) -> bool:
        length = len(word)
        curr = self.trie
    
    # We track where we are on the tree and the word
        def dfs(index, node):
            if index == length:
                return '.' in node

            if word[index] == '.':
                for key in node:
                    if key != '.':
                        if dfs(index+1, node[key]):
                            return True
                return False

            if word[index] not in node:
                return False

            return dfs(index + 1, node[word[index]])

        return dfs(0, curr)                    


        
           
