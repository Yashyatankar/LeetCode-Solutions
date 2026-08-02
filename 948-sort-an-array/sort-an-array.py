class Solution(object):

    def merge(self, nums, l, mid, r):

        a = []
        b = []

        # Copy left half
        for i in range(l, mid + 1):
            a.append(nums[i])

        # Copy right half
        for i in range(mid + 1, r + 1):
            b.append(nums[i])

        i = 0
        j = 0
        k = l

        # Compare both arrays
        while i < len(a) and j < len(b):

            if a[i] <= b[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1

            k += 1

        # Copy remaining elements of a
        while i < len(a):
            nums[k] = a[i]
            i += 1
            k += 1

        # Copy remaining elements of b
        while j < len(b):
            nums[k] = b[j]
            j += 1
            k += 1

    def mergeSort(self, nums, l, r):

        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        self.merge(nums, l, mid, r)

    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums