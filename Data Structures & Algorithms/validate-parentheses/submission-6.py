class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = {')':'(', '}': '{', ']': '['}

        for char in s:
            #only push it onto the stack if it's an opening bracket
            #if it's a closing bracket, check if it matches the top of the stack if the stack is non-empty else just add the bracket
            #if it matches, then pop the stack item
            if char not in brackets:
                stack.append(char)
                print(char)

            else:
                if stack:
                    top = stack[-1]
                    if brackets[char] == top:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)            

        if len(stack) == 0:
            return True

        return False   