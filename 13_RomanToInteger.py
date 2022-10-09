class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = None
        for c in s:
            try:
                if roman[prev] < roman[c]:
                    result -= roman[prev]
                    result += (roman[c] - roman[prev])
                else:
                    result += roman[c]
            except KeyError:
                result += roman[c]
            prev = c
        return result
