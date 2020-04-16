class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = 1
            else:
                return num

        return -1



# 时间O(n)，空间O（n）


