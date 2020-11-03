
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        smap = {}
        tset = set()
        for i, ss in enumerate(s):
            if ss not in smap and t[i] not in tset:
                smap[ss] = t[i]
                tset.add(t[i])
            elif smap.get(ss, ss) != t[i]:
                return False
        return True


print(Solution().isIsomorphic("ab", "ca"))
print(Solution().isIsomorphic("ab", "aa"))
