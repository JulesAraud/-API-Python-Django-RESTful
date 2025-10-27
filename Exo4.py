class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        carry = 1  


        for i in range(n - 1, -1, -1):
            new_val = digits[i] + carry
            digits[i] = new_val % 10
            carry = new_val // 10
            if carry == 0:
                break 
        if carry:
            digits.insert(0, carry)

        return digits


sol = Solution()
print(sol.plusOne([4, 3, 2, 1]))
