# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    i = 0
    n = len(a)

    while i < n - 1:
        m = i
        j = i + 1

        while j < n:
            if a[j] < a[m]:
                m = j
            j += 1
        a[i], a[m] = a[m], a[i]
        i += 1

    print(a)