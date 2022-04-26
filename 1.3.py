# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    with open("text.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
        maxim = 0
        a = []

        for line in lines:
            maxim = max(len(line), maxim)
        for line in lines:
            if len(line) == maxim:
                a.append(line)

    for i in a:
        print(i)