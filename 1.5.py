# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    print(len(set(a)))

    for i in set(a):
        c = 0
        for k in a:
            if (k == i):
                c += 1
        print(i, " - ", c)