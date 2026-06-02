class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        seen = {}
        def func(amt):
            if amt == 0:
                return 0
            
            minCoins = float('inf')

            for coin in coins:
                if coin > amt:
                    continue

                if (coin, amt) in seen:
                    count = seen[(coin, amt)]
                
                else:
                    count = seen[(coin, amt)] = func(amt-coin)
                    
                minCoins = minCoins if minCoins <= count else count

            return minCoins + 1

        minCoins = float('inf')

        for coin in coins:
            if coin > amount:
                continue
            
            count = seen[(coin, amount)] if (coin, amount) in seen else func(amount-coin)
            minCoins = minCoins if minCoins <= count else count
        
        return minCoins+1 if minCoins !=float('inf') else -1


        
        
        

