
# https://www.lintcode.com/problem/strobogrammatic-number/description
class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        # write your code here
        same = {"0", "1", "8"}
        opp = {
            "6": "9",
            "9": "6"
        }
        l = 0
        nn = len(num)
        r = nn-1
        if nn % 2 == 1 and num[r//2] not in same:
            return False
        if num[0] == "0" and nn > 1:
            return False
        while l < r:
            if (num[l] in same and num[r] not in same) or (num[r] in same and num[l] not in same):
                return False
            if num[l] in opp and opp[num[l]] != num[r]:
                return False
            if num[l] not in same and num[l] not in opp:
                return False
            if num[r] not in same and num[r] not in opp:
                return False
            l += 1
            r -= 1
        return True


print(Solution().isStrobogrammatic("80"))
