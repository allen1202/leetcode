class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_value = nums[i] + nums[left] + nums[right]

                if sum_value == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1

                elif sum_value < 0:
                    left += 1

                else:
                    right -= 1
            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]:
                i += 1

        return res
