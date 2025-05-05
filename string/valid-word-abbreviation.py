class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        pw, pa = 0, 0


        def helper(pa, pw):
            end = pa
            while end < len(abbr) and abbr[end].isnumeric():
                end += 1
            increment = int(abbr[pa:end])
            pw += increment
            return pw, end

        while pw < len(word) and pa < len(abbr):
            if word[pw] == abbr[pa]:
                pw += 1
                pa += 1
            elif abbr[pa].isnumeric():
                if abbr[pa] == '0':
                    return False
                else: 
                    pw, pa = helper(pa, pw)
            else: 
                return False
        if pw == len(word) and pa == len(abbr):
            return True
        else:
            return False
        
        

        