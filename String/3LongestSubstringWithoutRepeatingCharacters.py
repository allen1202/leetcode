class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left = 0
        maxlen = 0
        for i, letter in enumerate(s):
            if letter in dic and dic[letter] >= left:
                maxlen = max(maxlen, i - left)
                left = dic[letter] + 1
                dic[letter] = i


            else:
                maxlen = max(maxlen, i - left + 1)
                dic[letter] = i

        return maxlen