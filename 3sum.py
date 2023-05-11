""" 
This problem learned me how to use "Two Pointers" algorithm
which is a very simple algorithm that you want to find a pair that 
meets your desire instead of using two loops to find the pair/pairs you can
use one loop just by cost of sorting your array

How Two Pointers Work?
basically you point to the first and the last item of your array
and check the pair e.g. you want you pair summation to be zero if it's
larger that zero then you move your last item pointer one element backward

WHY?

because the array is sorted and if you move the first pointer one element forward
you're making the gap bigger so you do the other option which is moving last pointer one
element backward

but if it's smaller that zero you move the first pointer one element forward

TRICKS?

you can find one or more pairs but to find more than one pair just look the solution
"""


class Solution:
    def threeSum(self, nums: list[int]):
        # to use two pointers algorithm
        nums.sort()
        l = []
        n_len = len(nums) - 1

        for i in range(len(nums) - 2):
            j = i + 1
            k = n_len

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    el = sorted([nums[i], nums[j], nums[k]])

                    if el not in l:
                        l.append(el)

                    j += 1

                elif s > 0:
                    k -= 1

                else:
                    j += 1

        return l


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, 4]))
print(s.threeSum([0, 1, 1]))
print(s.threeSum([0, 0, 0]))
