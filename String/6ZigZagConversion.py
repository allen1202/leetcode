class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [''] * numRows
        start = 0
        flip = 1
        if numRows == 1:
            return s
        for letter in s:
            if start == 0:
                flip = 1

            if start == numRows - 1:
                flip = - 1

            res[start] += letter
            start += flip

        return ''.join(res)