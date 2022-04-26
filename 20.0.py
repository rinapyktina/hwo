# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = [float(x) for x in input().split()]
    maxim = max(a)
    print(maxim)

    cnt = 0
    for i in a:
        if maxim == i:
            cnt += 1
    print(cnt)