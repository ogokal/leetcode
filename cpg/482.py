from typing import List


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        dashidx = 0
        for i, s in enumerate(S):
            if s == '-':
                dashidx += 1
                continue
        slen = len(S)
        charC = slen - dashidx
        rem = charC % K
        result = []
        cc = 0
        for i in range(slen):
            if S[i] == "-":
                continue
            result.append(S[i].upper())
            cc += 1
            if cc != charC and ((rem > 0 and cc == rem) or (cc % K == rem)):
                result.append("-")
        return "".join(result)


print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))
