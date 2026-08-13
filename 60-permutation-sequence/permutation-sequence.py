class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        result = []

        k -= 1

        for i in range(n, 0, -1):
            fact = 1
            for j in range(1, i):
                fact *= j

            index = k // fact
            k %= fact

            result.append(str(numbers.pop(index)))

        return "".join(result)