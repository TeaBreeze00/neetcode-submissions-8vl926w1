class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Why don't we initiate a dfs search when we get a letter match and then return true if the dfs returns the full word?
        m = len(board)  # rows
        n = len(board[0])  # cols

        def dfs(i, j):
            stack = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            # Each stack entry represents ONE complete path
            stack.append((i, j, 1, {(i, j)}))

            while stack:
                x, y, idx, visited = stack.pop()

                if idx == len(word):
                    return True

                for di, dj in directions:
                    ni = x + di
                    nj = y + dj

                    if (0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and board[ni][nj] == word[idx]):
                        new_visited = visited.copy()
                        new_visited.add((ni, nj))

                        stack.append((ni, nj, idx + 1, new_visited))

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j):
                        return True

        return False
