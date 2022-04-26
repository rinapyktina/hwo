# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    pos = 0
    neg = 0
    for i in a:
        if (a[i] > 0):
            pos += 1
        elif (a[i] < 0):
            neg += 1
    print(pos, neg)