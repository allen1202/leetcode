class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        self.res = []
        self.dfs(digits, 0, "")

        return self.res

    def dfs(self, digits, index, path):
        if len(path) == len(digits):
            self.res.append(path)
            return

        for i in range(index, len(digits)):
            for letter in self.dic[int(digits[i])]:
                self.dfs(digits, i + 1, path + letter)

