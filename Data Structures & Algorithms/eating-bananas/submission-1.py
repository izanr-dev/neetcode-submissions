class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        total = sum(piles)
        res = r

        while l <= r:
            
            k = (r + l) // 2
            
            summ = 0
            hours = h
            pile = 0

            while hours > 0 and pile < len(piles):
                hours -= ((piles[pile] + k - 1) // k)
                if hours >= 0:
                    summ += piles[pile]
                pile+=1

            if summ >= total:
                res = min(k, res)
                r = k - 1
            
            else:
                l = k + 1


        return res
        