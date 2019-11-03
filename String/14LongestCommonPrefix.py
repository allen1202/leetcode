class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i, pairs in enumerate(zip(*strs)):
            if len(set(pairs)) != 1:
                return strs[0][:i]

        return min(strs)
