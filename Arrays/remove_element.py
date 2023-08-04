"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for _ in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)


nums_to_verify = [([3,2,2,3], [2,2]),
                  ([0,1,2,2,3,0,4,2], [0,1,3,0,4])]
test_count = 1
val_to_remove = 3

for nums, exp_nums in nums_to_verify:
    print(f"Test #{test_count}")
    print(nums)
    
    sol = Solution()
    count = sol.removeElement(nums, val_to_remove)
    assert nums == exp_nums
    
    print(nums)
    print()
    test_count += 1
    val_to_remove -= 1
