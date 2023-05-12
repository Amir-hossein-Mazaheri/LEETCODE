class Solution:
    __nums = None

    def searchInsert(self, nums: list[int], target: int, range=None) -> int:
        l = len(nums)

        if not range:
            self.__nums = nums
            if target <= nums[0]:
                return 0

        if l < 3:
            if l == 2:
                r0 = range[0] if range else 0
                r1 = range[1] if range else 1

                if target == self.__nums[r0]:
                    return r0
                if target == self.__nums[r1]:
                    return r1

                if target > self.__nums[r1]:
                    return r1 + 1

                if self.__nums[r0] < target < self.__nums[r1]:
                    return r0 + 1

                if target < self.__nums[r0]:
                    if r0 > 0 and target < self.__nums[r0 - 1]:
                        return r0 - 1

                    return r0
            else:
                r0 = range[0] if range else 0

                if target == nums[0]:
                    return r0

                if target < nums[0]:
                    return r0

                if target > nums[0]:
                    return r0 + 1

        first_half = (l // 2) - 1
        second_half = first_half + 1

        if nums[0] <= target <= nums[first_half]:
            return self.searchInsert(nums[:first_half + 1], target, [range[0], range[0] + first_half] if range else [0, first_half])

        return self.searchInsert(nums[second_half:], target, [range[0] + second_half, range[1]] if range else [second_half, l - 1])


s = Solution()

print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 4))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 2, 3, 4, 5, 6, 7, 8], 6))
print(s.searchInsert([1, 3, 5, 6], 0))
print(s.searchInsert([1, 3, 4], 1))
print(s.searchInsert([1], 2))
print(s.searchInsert([1, 3], 2))
print(s.searchInsert([1, 2, 4, 6, 7], 3))
