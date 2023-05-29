# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
#   1. LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the
# security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses
# the key-card three or more times in a one-hour period.
#   2. You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name
# and the time when their key-card was used in a single day.
#   3. Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
#   4. Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending
# order alphabetically.
#   5. Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not
# considered to be within a one-hour period.
#   6. Constraints:
#       1 <= keyName.length, keyTime.length <= 10^5
#       keyName.length == keyTime.length
#       keyTime[i] is in the format "HH:MM".
#       [keyName[i], keyTime[i]] is unique.
#       1 <= keyName[i].length <= 10
#       keyName[i] contains only lowercase English letters.


from typing import List
from unittest import TestCase
from collections import defaultdict


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        users = defaultdict(list)
        for i in range(len(keyName)):
            kt = keyTime[i].split(':')
            users[keyName[i]].append(60*int(kt[0]) + int(kt[1]))

        out = []
        for user in users.keys():
            uses = sorted(users[user])
            for i in range(len(uses) - 2):
                if uses[i+2] - uses[i] <= 60:
                    out.append(user)
                    break

        return sorted(out)


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [{"keyName": ["alice","alice","alice","bob","bob","bob","bob"],
              "keyTime": ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]},
             ["bob"]],
            [{"keyName": ["daniel","daniel","daniel","luis","luis","luis","luis"],
              "keyTime": ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]},
             ["daniel"]]
        ]:
            print(f"run test {case}")
            self.assertListEqual(expected, Solution().alertNames(**case))