class Solution:
    def countAndSay(self, n):
        result = "1"

        for _ in range(n - 1):
            next_result = ""
            i = 0

            while i < len(result):
                j = i

                while j < len(result) and result[j] == result[i]:
                    j += 1

                next_result += str(j - i) + result[i]
                i = j

            result = next_result

        return result