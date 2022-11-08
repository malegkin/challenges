# https://contest.yandex.ru/yacup/contest/42202/problems/E/
# 21 case - TL == 25
import os
from typing import Set, List
from collections import defaultdict


with open("input.txt") as f:
    n = int(f.readline())       # black folders
    bfs: Set[str] = set()
    for _ in range(n):
        bfs.add(os.path.dirname(f.readline().replace('\n', '')))

    # files
    files = dict()
    for _ in range(int(f.readline())):
        fn = l = f.readline().replace('\n', '')
        l = os.path.dirname(l)
        while len(l) > 0:
            # print(l)
            if l in bfs:
                l = fn
                _, ext = os.path.splitext(fn)

                while len(l) > 0:
                    # print(f"{l=}")
                    if l not in files:
                        files[l] = defaultdict(int)
                    # print(f"{l}{ext} += 1")
                    files[l][ext] += 1
                    if l == '/':
                        break
                    l = os.path.dirname(l)
                break

            if l == '/':
                break
            l = os.path.dirname(l)

    with open('output.txt', 'w') as f_out:
        for _ in range(int(f.readline())):
            d = os.path.dirname(f.readline().replace('\n', ''))
            if d not in files:
                f_out.write("0\n")
                continue
            s = 0
            out = []
            for ext in files[d]:
                s += files[d][ext]
                out.append(f"{ext}: {files[d][ext]}")
            out = '\n'.join(out)
            f_out.write(f"{len(files[d])}\n{out}\n")


