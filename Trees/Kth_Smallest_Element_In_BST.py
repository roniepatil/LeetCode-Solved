'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            k -= 1
            if not k:
                return cur.val
            cur = cur.right


a = Solution()
node_2 = TreeNode(2)
node_1 = TreeNode(1, None, node_2)
node_4 = TreeNode(4)
root = TreeNode(3, node_1, node_4)
print(a.kthSmallest(root,1))