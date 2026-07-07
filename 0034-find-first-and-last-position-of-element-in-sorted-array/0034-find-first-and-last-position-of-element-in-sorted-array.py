class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first_occurrence():
            start, end = 0, len(nums) - 1
            ans = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    ans = mid
                    end = mid - 1      # search left half
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return ans

        def last_occurrence():
            start, end = 0, len(nums) - 1
            ans = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    ans = mid
                    start = mid + 1    # search right half
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return ans

        return [first_occurrence(), last_occurrence()]