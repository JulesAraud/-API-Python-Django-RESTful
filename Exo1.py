class Solution:
    def Palindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - l - 1              # renoi le debut et la taille 


        best_start, best_len = 0, 1
        for i in range(n):


            l1, len1 = expand(i, i)
            if len1 > best_len:
                best_start, best_len = l1, len1
            
            
            l2, len2 = expand(i, i + 1)
            if len2 > best_len:
                best_start, best_len = l2, len2

        return s[best_start:best_start + best_len]


sol = Solution()
print(sol.Palindrome("azebabadababrty"))