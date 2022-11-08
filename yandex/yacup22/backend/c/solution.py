# https://contest.yandex.ru/yacup/contest/42202/problems/C/
# 119 case Time Limit (
import re
import string
from collections import Counter
from functools import cache

DEFAULT_CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

@cache
def base2int(value, base, chars=None, allow_negative=True):
    # this is the "fountain" we'll get the weird base's digits from
    chars = DEFAULT_CHARS if chars is None else chars
    charmap = {chars[i]: i for i in range(0, len(chars))}  # make dict of {char:position} pairs



    converted = 0  # converted integer
    sign = 1  # 1= positive, -1= negative; multiply int by this to correct sign

    num = list(value)  # working copy of str as list
    num.reverse()  # makes the integer position equal to exponent

    if num[-1] == '-':
        # remember, "leading" char is now at the end due to the above reverse()
        if not allow_negative and '-' not in charmap:
            # this error won't raise if '-' is being used as a digit!
            raise ValueError("Negative values not allowed")
        # NOTE: if you want a leading '-' to be treated as a char, you must
        #       set allow_negative = False; else we assume it means "negative"
        sign = -1 if allow_negative else 1
        num.pop()  # remove the sign, kind of like abs() on an int

    for exp in range(0, len(num)):
        # for each char index, use it as an exponent as well as an index, and...
        try:
            converted += charmap[num[exp]] * (base ** exp)  # value of digit times base to the power of position
        except KeyError as e:
            raise KeyError(f"digit {e} not found in '{chars}'")

    converted *= sign  # multiply by sign to correct negative if needed
    return converted  # return the converted int


def get_sum(args, from_base):
    out = 0

    for arg in args:
        if arg[0] == '+':
            out += base2int(arg[1], from_base)
        else:
            out -= base2int(arg[1], from_base)

    return out


with open("input.txt") as f_in:
    l_in, r_in = f_in.readline().upper().replace('\n', '').split('=')
    l_in = f"+ {l_in}"
    r_in = f"+ {r_in}"

    l_all = re.findall(r'([+-]+)\s*([\dA-Z]+)', l_in)
    r_all = re.findall(r'([+-]+)\s*([\dA-Z]+)', r_in)

    b_min = max(max(Counter(l_in)), max(Counter(r_in)))

    b_min = int(b_min) if b_min in string.digits else (ord(b_min) - ord('A') + 10)

    out = -1
    for b in range(b_min + 1, 1024):
        try:
            if get_sum(l_all, b) == get_sum(r_all, b):
                out = b
                break
        except:
            pass

    print(out)
