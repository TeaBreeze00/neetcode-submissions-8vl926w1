class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #This is the approach, I have 3 hashmaps, I am going to 
        #iterate through the entire sudoku by rows, columns and boxes and ensure
        #they meet the criteria of having 1-9 without duplicates
        
        #If any list if equal to this list they're valid otherwise they're not valid
        
        #The idea here is any sudoku grid row and column integer divided by 3 will
        #give us the corresponding grid of the sudoku grid

        for row in range(9):
            seen = set()   #hashset for checking by the rows

            for col in range(9):
                if (board[row][col] == "."):
                    continue
                if (board[row][col] in seen):
                    return False
                seen.add(board[row][col])   

        for col in range(9):
            seen = set()

            for row in range(9):
                if (board[row][col] == "."):
                    continue
                if(board[row][col] in seen):
                    return False
                seen.add(board[row][col])
        
        seen = defaultdict(set) # Here the key will be (r/3, c/3), giving us the subsequent grid number

        for row in range(9):     # This is going by the grid

            for col in range(9):

                if(board[row][col] == "."):
                    continue

                if(board[row][col] in seen[(row//3, col//3)]):
                    return False    

                seen[(row//3, col//3)].add(board[row][col])        

        return True