class Solution:
    def divide(self, dividend, divisor):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            value = divisor
            count = 1

            while dividend >= (value << 1):
                value <<= 1
                count <<= 1

            dividend -= value
            result += count

        return -result if negative else result