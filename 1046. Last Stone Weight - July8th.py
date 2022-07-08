class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            
            max_stone = max(stones)
            stones.remove(max_stone)
            
            second_max_stone = max(stones)
            stones.remove(second_max_stone)
            
            new_stone = max_stone - second_max_stone
            
            if new_stone != 0:
                stones.append(new_stone)
            
        if (len(stones) == 1):            
            return stones[0]
        
        return 0