# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        # In order to do level order traversal, we need to use queue
        q = deque()
        q.append(root) # Input the first thing
        
        # The list that is to be returned
        returnedList = []
        

        while q:
            elems = len(q)
            addedlist = []
            
            for i in range(elems):
                s = q.popleft()
                if s.left:
                    q.append(s.left)
                if s.right:
                    q.append(s.right)
                
                addedlist.append(s.val)
            
            returnedList.append(addedlist)

        return returnedList    


            



