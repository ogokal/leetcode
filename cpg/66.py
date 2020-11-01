
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            cur = digits[i] + carry
            carry = 1 if cur > 9 else 0
            if cur > 9:
                digits[i] = cur % 10
            else:
                digits[i] = cur
        if carry == 1:
            digits.insert(0, carry)
        return digits
