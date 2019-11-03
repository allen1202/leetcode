class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        index = 0
        while index < len(nums):
            if nums[index] <= num:
                result += strings[index]

                num -= nums[index]

            else:
                index += 1

        return result