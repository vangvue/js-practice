# https://leetcode.com/problems/baseball-game/
# 682. Baseball Game
#
# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
#
# At the beginning of the game, you start with an empty record.
# You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record
# and is one of the following:
#
# An integer x - Record a new score of x.
#
# "+" - Record a new score that is the sum of the previous two scores.
# It is guaranteed there will always be two previous scores.
#
# "D" - Record a new score that is double the previous score.
# It is guaranteed there will always be a previous score.
#
# "C" - Invalidate the previous score, removing it from the record.
# It is guaranteed there will always be a previous score.
#
# Return the sum of all the scores on the record.

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if len(ops) == 1:
            return ops[0]
        opsStr = "+DC"
        numsArr = []
        charArr = []
        result = 0

        for index in ops:
            if index in opsStr:
                if index == "+": numsArr.append(numsArr[-1] + numsArr[-2])
                elif index == "D": numsArr.append(numsArr[-1] * 2)
                elif index == "C": del numsArr[-1]
            else: numsArr.append(int(index))

        return sum(numsArr)
