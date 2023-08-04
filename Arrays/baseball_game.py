"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
"""


class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        
        for oper in operations:
            if oper == "+":
                score.append(sum(score[-2:]))
            elif oper == "D":
                score.append(score[-1] * 2)
            elif oper == "C" and len(score) > 0:
                score.pop()
            else:
                score.append(int(oper))
        
        score_sum = sum(score) if len(score) > 0 else 0

        return score_sum


test_data = [(["5","2","C","D","+"], 30),
             (["1","C"], 0),
             (["5","-2","4","C","D","9","+","+"], 27)]
test_counter = 1

for opers, exp_sum in test_data:
    print(f"\nTest #{test_counter}")
    print(opers)
    
    sol = Solution()
    sum_score = sol.calPoints(opers)
    assert sum_score == exp_sum, f"Expected: {exp_sum}, Received: {sum_score}"
    
    print("Sum:", sum_score)
    test_counter += 1
