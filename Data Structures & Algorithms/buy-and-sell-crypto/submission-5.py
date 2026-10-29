class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        minv = 101

        for number in prices:
            minv = min(minv, number)
            profit = max(number-minv, profit)

        return profit

        """
        profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, (prices[j] - prices[i]))

        return profit
        """



        

        