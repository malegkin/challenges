# https://www.codewars.com/kata/53f40dff5f9d31b813000774
# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the
# original string.
# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the
# given string. "whi" is a triplet for the string "whatisup".
# As a simplification, you may assume that no letter occurs more than once in the secret string.
# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain
# sufficient information to deduce the original string. In particular, this means that the secret string will never
# contain letters that do not occur in one of the triplets given to you.

import random
import string
import itertools
from timeit import timeit
from unittest import TestCase
from collections import deque, defaultdict


def recoverSecret(triplets, c_type=list):
    letters = c_type(set([l for t in triplets for l in t]))

    for t in triplets * len(letters):
        for i in range(len(t) - 1):
            a, b = letters.index(t[i]), letters.index(t[i + 1])
            if (a > b): letters[b], letters[a] = letters[a], letters[b]

    return ''.join(letters)


def recoverSecretPopularButInvalidSolution(triplets, c_type=list):
    """ best solution from all submitted"""
    def fix(l, a, b):
        """let l.index(a) < l.index(b)"""
        if l.index(a) > l.index(b):
            l.remove(a)
            l.insert(l.index(b), a)

    r = sorted(c_type(set([i for l in triplets for i in l])))

    for l in triplets:
        fix(r, l[0], l[1])
        fix(r, l[1], l[2])

    return ''.join(r)


class TestSolution(TestCase):
    def test_solution_like_codewars(self):
        for solution in [recoverSecret, recoverSecretPopularButInvalidSolution]:
                for secret, triplets in [
                    ["whatisup",  [['t', 'u', 'p'], ['w', 'h', 'i'], ['t', 's', 'u'], ['a', 't', 's'], ['h', 'a', 'p'],
                                   ['t', 'i', 's'], ['w', 'h', 's']]],
                    ["whatisup",  [['t', 'u', 'p'], ['w', 'h', 'i'], ['t', 's', 'u'], ['a', 't', 's'], ['h', 'a', 'p'],
                                   ['t', 'i', 's'], ['w', 'h', 's']]],
                    ["mathisfun", [['t', 's', 'f'], ['a', 's', 'u'], ['m', 'a', 'f'], ['a', 'i', 'n'], ['s', 'u', 'n'],
                                   ['m', 'f', 'u'], ['a', 't', 'h'], ['t', 'h', 'i'], ['h', 'i', 'f'], ['m', 'h', 'f'],
                                   ['a', 'u', 'n'], ['m', 'a', 't'], ['f', 'u', 'n'], ['h', 's', 'n'], ['a', 'i', 's'],
                                   ['m', 's', 'n'], ['m', 's', 'u']]],
                    ["congrats", [['g', 'a', 's'], ['o', 'g', 's'], ['c', 'n', 't'], ['c', 'o', 'n'], ['a', 't', 's'],
                                  ['g', 'r', 't'], ['r', 't', 's'], ['c', 'r', 'a'], ['g', 'a', 't'], ['n', 'g', 's'],
                                  ['o', 'a', 's']]]
                ]:
                    print(f"run_test {solution.__name__} {secret}")

    def test_solution_all_permutations(self):
        for solution in [recoverSecret, recoverSecretPopularButInvalidSolution]:
                for secret, triplets in [
                    ["whatisup",  [['t', 'u', 'p'], ['w', 'h', 'i'], ['t', 's', 'u'], ['a', 't', 's'], ['h', 'a', 'p'],
                                   ['t', 'i', 's'], ['w', 'h', 's']]]
                ]:
                    print(f"run_test {solution.__name__}  {secret}")
                    secrets = defaultdict(int)
                    for pts in itertools.permutations(triplets):
                        secrets[solution(triplets)] += 1

                    self.assertEqual(1, len(secrets))
                    self.assertEqual(secret, max(secrets, key=secrets.get))

    def test_list_vs_deque(self):
        triplets = [random.sample(string.ascii_lowercase, 3) for _ in range(1000)]
        for solution in [recoverSecret, recoverSecretPopularButInvalidSolution]:
            for c_type in [list, deque]:
                print(f"{solution.__name__}: {c_type.__name__} {timeit(lambda: solution(triplets, c_type), number=10):.3f}")
