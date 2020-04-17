#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def buildTree(self, preorder, inorder):
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        return self.helper(preorder, 0, len(preorder)-1,inorder,0,len(inorder) -1, dic)



    def helper(self, preorder, prestart, preend, inorder, instart, inend, dic):
        if prestart > preend:
            return

        root = TreeNode(preorder[prestart])

        if prestart == preend:
            return root


        else:

            midindex = dic[preorder[root.val]]
            leftnodes = midindex - instart
            rightnodes = inend - midindex
            leftsubtree = self.helper(preorder, prestart + 1,prestart+leftnodes,inorder,instart,midindex-1,dic)
            rightsubtree = self.helper(preorder,preend - rightnodes + 1,preend,inorder, midindex+1,inend,dic)
            root.left = leftsubtree
            root.right = rightsubtree

            return root

