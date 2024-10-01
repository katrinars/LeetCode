class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        if index == -1:
            return word
        else:
            p1 = index
            p2 = 0
            newword = []
            while p1 >= p2:
                newword.append(word[p1])
                p1 -= 1
        return ''.join(let for let in newword) + word[index+1:]
        
        