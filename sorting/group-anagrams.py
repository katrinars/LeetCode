class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        results = []

        for word in strs:
            letters = [char for char in word]
            letters.sort()
            letters = tuple(letters) # transform to hash

            if letters in words: 
                words[letters].append(word)
            else: 
                words[letters] = [word]

        for value in words.values():
            results.append(value)
            
        return results