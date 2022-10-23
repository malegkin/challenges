# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
# The purpose of this kata is to write a program that can do some algebra.
# Write a function expand that takes in an expression with a single, one character variable, and expands it. The
# expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single
# character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable.
# If a = -1, a "-" will be placed in front of the variable.
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients
# of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are
# the powers that x is being raised to in each term and are in decreasing order.
# If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one, the
# coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included. If the power
# of the term is 0, only the coefficient should be included. If the power of the term is 1, the caret and power should
# be excluded.
import re
import math
from unittest import TestCase


def expand(expr):
    # (ax+b)**n
    br = re.compile("\(([-\d]*)([a-z])[+]*([-\d]+)\)\^([-\d]+)").match(expr)
    a = 1 if br[1] == '' else int('-1' if br[1] == '-' else br[1])
    x = br[2]
    b = int(br[3])
    n = int(br[4])

    if n == 0:
        return "1"
    if n == 1:
        return f"{a if abs(a) != 1 else '' if a == 1 else '-' }{x}{b:+d}"

    out = f"{a**n if abs(a) != 1 else '' if a**n == 1 else '-' }{x}^{n}"
    for i in range(n-1, 0, -1):
        cnk = math.factorial(n) // (math.factorial(i)*math.factorial(n-i))
        out += f"{cnk * a**i * b**(n-i):+d}"
        out += f"{x}^{i}" if i > 1 else x

    out += f"{b**n:+d}"

    return out


P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')


def expand_best(expr):
    a, v, b, e = P.findall(expr)[0]

    if e == '0': 
        return '1'

    o = [int(a != '-' and a or a and '-1' or '1'), int(b)]
    e, p = int(e), o[:]

    for _ in range(e - 1):
        p.append(0)
        p = [o[0] * coef + p[i - 1] * o[1] for i, coef in enumerate(p)]

    res = '+'.join(f'{coef}{v}^{e - i}' if i != e else str(coef) for i, coef in enumerate(p) if coef)

    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-', '-')


class TestSolution(TestCase):
    def test_solution(self):
        for exx in [expand, expand_best]:
            self.assertEqual("1", exx("(x+1)^0"))
            self.assertEqual("1", exx("(x-1)^0"))
            self.assertEqual("x+1", exx("(x+1)^1"))
            self.assertEqual("x-1", exx("(x-1)^1"))
            self.assertEqual("-2x-1", exx("(-2x-1)^1"))
    
            self.assertEqual("x^2+2x+1", exx("(x+1)^2"))
            self.assertEqual("x^2-2x+1", exx("(x-1)^2"))
    
            self.assertEqual("625m^4+1500m^3+1350m^2+540m+81", exx("(5m+3)^4"))
            self.assertEqual("8x^3-36x^2+54x-27", exx("(2x-3)^3"))
            self.assertEqual("1", exx("(7x-7)^0"))
    
            self.assertEqual("625m^4-1500m^3+1350m^2-540m+81", exx("(-5m+3)^4"))
            self.assertEqual("-8k^3-36k^2-54k-27", exx("(-2k-3)^3"))
            self.assertEqual("1", exx("(-7x-7)^0"))
    
            self.assertEqual("-j^3+27j^2-243j+729", exx("(-j+9)^3"))
            self.assertEqual("k^4-24k^3+216k^2-864k+1296", exx("(-k+6)^4"))
            self.assertEqual("s^2-28s+196", exx("(-s+14)^2"))
            self.assertEqual("-c-17", exx("(-c-17)^1"))
