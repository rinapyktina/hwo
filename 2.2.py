# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    cnt = 0
    for i in a:
        if (a[i] > a[i + 1]):
            cnt += 1
    if (cnt > 0):
        print("NO")
    else:
        print("YESS")