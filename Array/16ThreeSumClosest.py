class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = (nums[i] + nums[l] + nums[r])
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return res

