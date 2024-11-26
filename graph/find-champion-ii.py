class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winners = set(num for num in range(n))
        
        for round in edges:
            winners.discard(round[1])

        if len(winners) != 1:
            return -1
        else: 
            return winners.pop()