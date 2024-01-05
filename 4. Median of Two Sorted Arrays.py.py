class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            m = len(nums1)
            n = len(nums2)

            start = 0
            end = m-1

            while start <= end:
                partition_nums1 = (start + end) // 2
                partition_nums2 = (m + n + 1) // 2 - partition_nums1
                maxLeftNums1 = float(
                    "-infinity") if partition_nums1 == 0 else nums1[partition_nums1 - 1]
                # If there are no elements left on the right side after partition
                minRightNums1 = float(
                    "infinity") if partition_nums1 == m else nums1[partition_nums1]
                # Similarly for nums2
                maxLeftNums2 = float(
                    "-infinity") if partition_nums2 == 0 else nums2[partition_nums2 - 1]
                minRightNums2 = float(
                    "infinity") if partition_nums2 == n else nums2[partition_nums2]
                # Check if we have found the match
                if maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1:
                    # Check if the combined array is of even/odd length
                    if (m + n) % 2 == 0:
                        return (max(maxLeftNums1, maxLeftNums2) + min(minRightNums1, minRightNums2)) / 2
                    else:
                        return max(maxLeftNums1, maxLeftNums2)
                # If we are too far on the right, we need to go to left side
                elif maxLeftNums1 > minRightNums2:
                    end = partition_nums1 - 1
                # If we are too far on the left, we need to go to right side
                else:
                    start = partition_nums1 + 1

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A   # choice min nums2 going to binary search
        total = len(A)+len(B)
        half = total // 2
        l, r = 0, len(A)-1

        while True:
            i = (l+r)//2  # A
            j = half - i - 2  # B
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(A) else float("infinity")
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1

        p1 = 0
        p2 = 0
        new = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                new.append(nums1[p1])
                p1 += 1
            else:
                new.append(nums2[p2])
                p2 += 1
        while p1 < len(nums1):
            new.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            new.append(nums2[p2])
            p2 += 1
        if len(new) % 2 == 0:
            index = len(new) // 2
            median = (new[index] + new[index-1]) / 2
        else:
            median = float(new[len(new)//2])
        return median
