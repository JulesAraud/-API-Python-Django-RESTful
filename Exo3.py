class Solution:
    def romain(self, s: str) -> int:
        vals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev = 0


        for ch in reversed(s):
            v = vals[ch]
            if v < prev:
                total -= v
            else:
                total += v
            prev = v
        return total


sol = Solution()
print(sol.romain("MCMXCIV"))
