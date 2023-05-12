"""
Another type of "Two Pointers" is using a "fast" and a "slow" pointer which is used
in the second Solution class

its not as useful as the other kind of "Two Pointers" but it can give nice and
creative ways of solving problems

in this problem the fast pointer gets incremented in each iteration but the slow
pointer gets incremented if the value of fast pointer doesn't match the value of slow
pointer if might seem weird but it work flawlessly but it doesn't change the array length

this is how it works:

f and s means fast and slow pointers

Step 1:
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
f = 1 , s = 0

Step 2:
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
f = 2, s = 0

Step 3:
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
f = 3, s = 1
NOTE: when two values doesn't match the value element in the s+1 index will
become the value of element in f index

Step 4:
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
f = 4, s = 1

Step 5:
[0, 1, 2, 1, 1, 2, 2, 3, 3 , 4]
f = 5, s = 2
NOTE: the same as Step 3

Step 6:
[0, 1, 2, 1, 1, 2, 2, 3, 3 , 4]
f = 6, s = 2

Step 7:
[0, 1, 2, 3, 1, 2, 2, 3, 3 , 4]
f = 7, s = 3
NOTE: the same as Step 3

Step 8:
[0, 1, 2, 3, 1, 2, 2, 3, 3 , 4]
f = 8, s = 3

Step 9:
[0, 1, 2, 3, 4, 2, 2, 3, 3 , 4]
f = 9, s = 4

as you can see the array is unique until the s index which thats what question asked us
but you can remove the duplicates by slicing it
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # this syntax just change the original reference to the nums list
        nums[:] = sorted(set(nums))

        return len(nums)


# second solution without using Two Pointers
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow += 1

            fast += 1

        return [slow + 1, nums]


s = Solution()

print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates([1, 1, 1, 1]))
