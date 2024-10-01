class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num in nums2:
            nums1.insert(0, num)
        while len(nums1) > m+n:
            nums1.pop(-1)
        nums1.sort()
            