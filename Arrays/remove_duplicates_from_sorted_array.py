"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[count-1]:
                nums[count] = nums[i]
                count +=1
        return count


nums_to_verify = [([1,1,2], [1,2]),
                  ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4])]
test_count = 1

for nums, exp_nums in nums_to_verify:
    print(f"Test #{test_count}")
    print(nums)
    
    sol = Solution()
    count = sol.removeDuplicates(nums)
    assert nums[:count] == exp_nums
    
    print(nums[:count])
    print()
    test_count += 1
