"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def buildTree(self, preorder, inorder):
        def build(preorder, inorder):
            if not inorder:
                return None
            value = preorder.popleft()
            index = inorder.index(value)

            root = TreeNode(value)

            root.left = build(preorder, inorder[:index])
            root.right = build(preorder, inorder[index + 1:])

            return root
        
        return build(deque(preorder), inorder)



def main():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    solution = Solution()

    result = solution.buildTree(preorder, inorder)

    stack = deque([(result, 0)])
    ans = []
    
    while stack:
        node, level = stack.popleft()
        
        if node:           
            ans.append(node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
        else:
            ans.append(None)
    
    while ans[-1] == None:
        if ans[-1] == None:
            ans.pop()

    print(ans)

if __name__ == "__main__":
    main()