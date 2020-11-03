class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "u", "o"}
        chars = list(s)
        l = 0
        slen = len(s)
        r = slen-1
        while l < r:
            while l < slen and s[l].lower() not in vowels:
                l += 1
            while r > -1 and s[r].lower() not in vowels:
                r -= 1
            if l < r:
                chars[r], chars[l] = chars[l], chars[r]
            l += 1
            r -= 1
        return "".join(chars)
