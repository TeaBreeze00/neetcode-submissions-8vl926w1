class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #I'll be using a backtracking option.
        listToReturn = []

        def backtrack(openN, closeN, curr):

            if openN == closeN == n:
                listToReturn.append(curr)
            
            if openN < n:
                backtrack(openN + 1, closeN, curr + "(")

            if closeN < openN:
                backtrack(openN, closeN + 1, curr + ")")

        backtrack(0, 0, "")  
        return listToReturn          


        