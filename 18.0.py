# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    with open("text.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            j = None
            for i in line:
                if j == i:
                    print(line)
                j = i