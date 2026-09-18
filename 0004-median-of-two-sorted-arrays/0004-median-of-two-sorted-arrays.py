class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = []
        i = 0
        j = 0
        #sorted List
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        while i < len(nums1):
            merge.append(nums1[i])
            i += 1
        while j < len(nums2):
            merge.append(nums2[j])
            j += 1
        n = len(merge)

        if n % 2 == 1:
            return float(merge[n // 2])
        else:
            return float(merge[n // 2 - 1] + merge[n // 2]) / 2.0

        
    
             
           

        