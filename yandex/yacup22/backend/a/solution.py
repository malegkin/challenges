# https://contest.yandex.ru/yacup/contest/42202/problems/A/
# Time Limit

from typing import List


with open("input.txt") as f_in:
    n, m, q = f_in.readline().replace('\n', '').split(' ')
    n = int(n)
    m = int(m)
    last_max = last_min = -1

    out: List[int] = []
    dcr: List[int] = [0]*n
    dcs: List[List[bool]] = [[True]*m for _ in range(n)]
    dcs_as: List[int] = [m]*n

    for cmd in f_in.readlines():
        cmd = cmd.replace('\n', '').split(' ')

        if cmd[0] == 'DISABLE':
            dc_i = int(cmd[1]) - 1
            s_i = int(cmd[2])-1
            if dcs[dc_i][s_i]:
                dcs[dc_i][s_i] = False
                dcs_as[dc_i] -= 1
                last_max = -1 if dc_i == last_max else last_max
                last_min = -1 if dc_i != last_min else last_min
                # if dc_i != last_min:
                #     last_min = last_min if dcs_as[dc_i] * dcr[dc_i] > dcs_as[last_min] * dcr[last_min] else dc_i

        if cmd[0] == 'RESET':
            dc_i = int(cmd[1]) - 1
            dcs[dc_i] = [True]*m
            dcr[dc_i] += 1
            dcs_as[dc_i] = m

            last_min = -1 if dc_i == last_min else last_min
            last_max = last_max if dc_i == last_max else -1

        if cmd[0] == 'GETMAX':
            if last_max != -1:
                out.append(last_max)
            else:
                dc_max_i = 0
                dc_max_value = dcs_as[0] * dcr[0]
                for i in range(1, n):
                    if dcs_as[i] * dcr[i] > dc_max_value:
                        dc_max_i = i
                        dc_max_value = dcs_as[i] * dcr[i]
                last_max = dc_max_i
                out.append(dc_max_i)

        if cmd[0] == 'GETMIN':
            if last_min != -1:
                out.append(last_min)
            else:
                dc_min_i = 0
                dc_min_value = sum(dcs[0]) * dcr[0]
                for i in range(1, n):
                    if dcs_as[i] * dcr[i] < dc_min_value:
                        dc_min_i = i
                        dc_min_value = dcs_as[i] * dcr[i]

                last_min = dc_min_i
                out.append(dc_min_i)

    with open('output.txt', 'w') as f_out:
        f_out.write('\n'.join([f"{o + 1}" for o in out]))
