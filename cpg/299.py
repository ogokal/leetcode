class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = {}
        lg = len(guess)
        ls = len(secret)
        pc = {}
        for i in range(ls):
            if i < lg:
                if secret[i] == guess[i]:
                    bulls[i] = secret[i]
                else:
                    if secret[i] not in pc:
                        pc[secret[i]] = 0
                    pc[secret[i]] += 1
        cows = 0
        for i, g in enumerate(guess):
            if i not in bulls and g in pc and pc[g] > 0:
                pc[g] -= 1
                cows += 1
        return str(len(bulls))+"A"+str(cows)+"B"


print(Solution().getHint("11", "01"))
