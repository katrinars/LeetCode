class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for word in words[1:]:
            new_count = Counter(word)
            count = count & new_count
        return [char for key, value in count.items() for char in [key]*value]

    