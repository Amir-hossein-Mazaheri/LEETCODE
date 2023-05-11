"""
This solution solved by "Two Pointers" which time complexity 
is nlogn that makes it better than n**2
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 2:
            return [0, 1]

        c_nums = sorted(nums)

        i = 0
        j = len(nums) - 1

        while i < j:
            s = c_nums[i] + c_nums[j]

            if s == target:
                a = nums.index(c_nums[i])
                nums[a] = None

                b = nums.index(c_nums[j])

                return sorted([a, b])

            elif s < target:
                i += 1
            elif s > target:
                j -= 1


s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([3, 2, 3], 6))
print(s.twoSum([-1, -2, -3, -4, -5], -8))
