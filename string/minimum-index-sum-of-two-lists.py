class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {}
        mins = []

        for i, string in enumerate(list1):
            if string in list2:
                index[string] = i + list2.index(string)
        
        for key, value in index.items():
            if value == min(index.values()):
                mins.append(key)
        return mins

