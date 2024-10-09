class Solution:
    def minLength(self, s: str) -> int:
        s_list = []
        l = 0
        r = 1
        
        # traverse s, add chars to a list
        for char in s:
            s_list.append(char)
        # traverse list with back to back pointers
        while s and r < len(s_list)-1:
            string = s[l]+s[r]
            removed = False
            # for each, if == "AB" or "CD", then remove
            if string == "AB" or string == "CD":
                s_list.pop(l)
                s_list.pop(r)
                removed = True
            if not removed:
                l += 1
                r += 1
        # after final traversal, check length
        return len(s_list)

        


        