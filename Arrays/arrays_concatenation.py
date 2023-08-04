"""
Given an integer array nums of length n,
you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_lst = []

        for i in range(len(nums)):
            new_lst.insert(i, nums[i])
            new_lst.append(nums[i])
        
        return new_lst


nums_to_verify = [([1,2,1], [1,2,1,1,2,1]),
                  ([1,3,2,1], [1,3,2,1,1,3,2,1])]
test_count = 1

for nums, exp_lst in nums_to_verify:
    print(f"Test #{test_count}")
    print(nums)
    
    sol = Solution()
    concatenated_lst = sol.getConcatenation(nums)
    assert concatenated_lst == exp_lst
    
    print(nums)
    print()
    test_count += 1
