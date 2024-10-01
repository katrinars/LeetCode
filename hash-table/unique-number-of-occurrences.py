class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        frequencies = freq.values()
        return len(frequencies) == len(set(frequencies))