# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

import copy
import math
from typing import List, Tuple
from collections import defaultdict
from unittest import TestCase


class BattleField:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x, self._y})"

    def is_adjacent(self, xy: 'BattleField') -> bool:
        return math.sqrt((xy._x - self._x)**2 + (xy._y - self._y)**2) < 1.5


class BattleShip:
    def __init__(self):
        self._fields: List[BattleField] = []

    def __str__(self):
        return f"[{', '.join([str(bf) for bf in self._fields])}]"

    def __len__(self):
        return len(self._fields)

    def append(self, bf: BattleField) -> bool:
        self._fields.append(bf)

    def is_adjacent(self, bf: BattleField) -> bool:
        return any(map(bf.is_adjacent, self._fields))

    def is_valid_ship(self):
        xs = set()
        ys = set()

        for bf in self._fields:
            xs.add(bf._x)
            ys.add(bf._y)

        return len(xs) == 1 or len(ys) == 1


def validate_battlefield(fields) -> bool:
    ships: List[BattleShip] = []
    for i in range(10):
        for j in range(10):
            if fields[i][j] == 1:
                bf = BattleField(i, j)
                for ship in ships:
                    if bf is not None and ship.is_adjacent(bf):
                        ship.append(bf)
                        bf = None
                if bf is not None:
                    bs = BattleShip()
                    bs.append(bf)
                    ships.append(bs)

    if len(ships) != 10:
        return False

    ship_cnt = defaultdict(int)
    for ship in ships:
        if not ship.is_valid_ship():
            return False

        ship_cnt[len(ship)] += 1

    if len(ship_cnt) != 4:
        return False

    for i in range(1, 5):
        if ship_cnt[i] + i != 5:
            return False

    return True


class TestSolution(TestCase):

    def test_solution(self):
        battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        battleField2 = copy.deepcopy(battleField)
        battleField2[0][0] = 0

        battleField3 = copy.deepcopy(battleField)
        battleField3[0][1] = 1

        battleField4 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for case, expected in [
            [battleField, True],
            [battleField2, False],
            [battleField3, False],
            [battleField4, False]
        ]:
            print(f"run_case {case}")
            self.assertEqual(expected, validate_battlefield(case))


    def test_adjacent_field(self):
        for case, expected in [
            [(0, 0), True], [(0, 1), True], [(0, 2), True], [(0, 3), False],
            [(1, 0), True], [(1, 1), True], [(1, 2), True], [(1, 3), False],
            [(2, 0), True], [(2, 1), True], [(2, 2), True], [(2, 3), False],
            [(3, 0), False], [(3, 1), False], [(3, 2), False], [(3, 3), False]
        ]:
            # print(f"run_case {case}")
            self.assertEqual(expected, BattleField(1, 1).is_adjacent(BattleField(*case)))
