class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2: return
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == 0:
                break
            if nums1[p1] > nums2[p2]:
                nums1.insert(p1, nums2[p2])
                p1 += 1
                p2 += 1
            else:
                # nums1.insert(p1+1, nums2[p2])
                p1 += 1
                # p2 += 1
        if p2 < len(nums2):
            nums1[p1:] = nums2[p2:]

            