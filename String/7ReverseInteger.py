class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>2**31:
            return 0
        if x<-2**31:
            return 0
        if x>=0 and x<=2**31:
            res=int(str(x)[::-1])
            return res if res<2**31 else 0
        else:
            res=-int(str(abs(x))[::-1])
            return res if res>-2**31 else 0
