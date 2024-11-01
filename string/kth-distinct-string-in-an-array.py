class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s_freq = {}
        '''
        traverse array and add strings to dict
        traverse dict w/ counter, if freq = 1 counter + 1, at k return key
        if none return ''
        '''
        count = 0
        for s in arr:
            s_freq[s] = s_freq.get(s, 0) + 1

        # print(s_freq)
        
        for key, val in s_freq.items():
            if val == 1:
                count += 1
                if count == k:
                    return key
        return ''

        # d 1
        # b 2
        # c 2
        # a 1