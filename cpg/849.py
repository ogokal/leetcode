from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        mmax = 0
        sz = len(seats)
        i = 0
        while i < sz:
            if seats[i] == 0:
                mmax += 1
            else:
                break
            i += 1
        left = i+1
        rmax = 0
        i = sz-1
        while i >= 0:
            if seats[i] == 0:
                rmax += 1
            else:
                break
            i -= 1
        right = i-1

        mmax = max(mmax, rmax)
        count = 0
        while left <= right:
            if seats[left] == 0:
                count += 1
            else:
                count = 0
            if count == 1:
                mmax = max(mmax, 1)
            else:
                mmax = max(mmax,count-1)
            left += 1
        
        return mmax

print(Solution().maxDistToClosest([1,0,1]))

        