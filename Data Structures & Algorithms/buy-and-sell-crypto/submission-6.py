class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #This solution is O(N) time complexity  

        profit = 0
        minv = 101

        for number in prices:
            minv = min(minv, number)
            profit = max(number-minv, profit)

        return profit

    
        """
        #This solution is O(N2) time complexity

        profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, (prices[j] - prices[i]))

        return profit
        """



        

        