class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """

        matrix = [[0] * len(colsum) for _ in range(2)]

        for i in range(len(colsum)):
            if colsum[i] == 0:
                matrix[0][i] = 0
                matrix[1][i] = 0

            elif colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1

            else:
                if upper >= lower:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    matrix[1][i] = 1
                    lower -= 1

        if upper == 0 and lower == 0:
            return matrix

        else:
            return []