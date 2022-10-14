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
from timeit import timeit
from unittest import TestCase
from collections import deque


def recoverSecret(triplets, c_type=list):
    secret = c_type()
    for triplet in triplets:
        [x, y, z] = triplet

        if x not in secret:
            secret.insert(0, x)

        if y not in secret:
            secret.insert(secret.index(x) + 1, y)
        if secret.index(y) < secret.index(x):
            secret.remove(y)
            secret.insert(secret.index(x), y)

        if z not in secret:
            secret.insert(secret.index(y) + 1, z)
        if secret.index(z) < secret.index(y):
            secret.remove(z)
            secret.insert(secret.index(y), z)

    return ''.join(secret)


def recoverSecretFaster(triplets):
    """ best solution from all submitted"""
    def fix(l, a, b):
        """let l.index(a) < l.index(b)"""
        if l.index(a) > l.index(b):
            l.remove(a)
            l.insert(l.index(b), a)

    r = list(set([i for l in triplets for i in l]))
    for l in triplets:
        fix(r, l[1], l[2])
        fix(r, l[0], l[1])
    return ''.join(r)


class TestSolution(TestCase):
    def test_solution(self):

        for c_type in [list, deque]:
            for secret, triplets in [
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
                print(f"run_test {c_type.__name__} {secret}")
                self.assertEqual(secret, recoverSecret(triplets, c_type))

    def test_list_vs_deque(self):
        triplets = [random.sample(string.ascii_lowercase, 3) for _ in range(1000)]
        for c_type in [list, deque]:
            print(f"{c_type.__name__} {timeit(lambda: recoverSecret(triplets, c_type), number=100):.3f}")
        print(f"recoverSecretFaster: {timeit(lambda: recoverSecretFaster(triplets), number=100):.3f}")
