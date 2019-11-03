class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxlen = 0
        self.left = 0
        for i in range(len(s)):
            self.check(i, i, s)
            self.check(i, i + 1, s)

            print(self.maxlen)
        return s[self.left:self.left + self.maxlen]

    def check(self, i, j, s):

        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        length = j - i - 1
        if length > self.maxlen:
            self.maxlen = length
            self.left = i + 1

