class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Okay so this is the dealio, I'll first go through the borders of the grid, then I'll see if I can find
        # any O's in the border. Then I run a BFS/DFS to identify any other O's connected to it (up, down, left, right connection, no diagonal connection)
        # then I mark it with T or something else. Then I do one pass on the grid to change the rest everything to Xs and after that I do another pass to change 
        # the T's to O's. 

        ROWS, COLS = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = []
        visit = set()
        
        # This is the core logic
        def bfs(i, j):
            stack.append((i, j))
            board[i][j] = "T"
            visit.add((i, j))

            while stack:
                r, c = stack.pop()
                for m, n in dirs:
                    a, b = r + m, c + n
                    if (a, b) not in visit and 0 <= a < ROWS and 0 <= b < COLS and board[a][b] == "O":
                        stack.append((a, b))
                        board[a][b] = "T"
                        visit.add((a, b))

        
        for i in range(COLS):
            if board[0][i] == "O":
                bfs(0, i)
            if board[ROWS-1][i] == "O":
                bfs(ROWS-1, i)

        for i in range(ROWS):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][COLS-1] == "O":
                bfs(i, COLS-1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"                                       

