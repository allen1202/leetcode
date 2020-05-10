# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.dic = {}
        self.visited = set()
        self.dfs(root)
        while p:
            self.visited.add(p.val)
            if p.val not in self.dic:
                break
            p = self.dic[p.val]

        # print(self.dic[5])
        while q:
            if q.val in self.visited:
                return q
            if q.val not in self.dic:
                break
            q = self.dic[q.val]

        return None

    def dfs(self, node):
        if node:
            if node.left:
                self.dic[node.left.val] = node
                self.dfs(node.left)
            if node.right:
                self.dic[node.right.val] = node
                self.dfs(node.right)


# 用一个map记录所有node的父节点，然后层层往上推。
