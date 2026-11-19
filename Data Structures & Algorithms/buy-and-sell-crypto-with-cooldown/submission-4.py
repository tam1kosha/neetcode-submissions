class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)
        
        def dfs(buy, sell) -> int:
            if sell >= n:
                return 0
            
            if (buy, sell) in dp:
                return dp[(buy, sell)]

            dp[(buy, sell)] = max(
                prices[sell] - prices[buy] + dfs(sell + 2, sell + 3),
                dfs(buy, sell + 1),
                dfs(buy + 1, sell + 1) 
                )
            
            return dp[(buy, sell)]

        return dfs(0, 1)

            
            
            