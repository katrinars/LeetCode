class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        intersection = []

        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1

        for num in nums2:
            if num in freq1:
                freq1[num] -= 1
                if freq1[num] == 0:
                    freq1.pop(num)
                intersection.append(num)

        return intersection

        

        





