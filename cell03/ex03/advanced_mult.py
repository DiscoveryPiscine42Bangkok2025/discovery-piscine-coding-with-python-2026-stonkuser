#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0
    while table <= 10:
        print(f"Table de {table}:", end=" ")

        i = 0
        while i <= 10:
            print(table * i, end="")
            if i < 10:
                print(" ", end="")
            i += 1

        print()
        table += 1
