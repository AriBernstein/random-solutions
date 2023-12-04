#!/usr/bin/env python

import copy
import time
from typing import List

# Frustratingly simple and bueatifully pythonic solutions, courtesy of
# https://stackoverflow.com/a/2574090

versions:List[str] = []

with open("order_software_versions/versions_3.txt") as f:
    for l in f:
        line_val = l.strip()
        if line_val == "": continue
        versions.append(line_val[1:])


def solution_1(versions:List[str]) -> list:
    v = copy.deepcopy(versions)
    v.sort(key=lambda s: list(map(int, s.split('.'))))
    return v


def solution_2(versions:List[str]) -> list:
    v = copy.deepcopy(versions)
    v.sort(key=lambda s: [int(u) for u in s.split('.')])
    return v    


start = time.time()
solution_1(versions)
end = time.time()
print(f"solution 1 seconds: {end - start}")


start = time.time()
solution_2(versions)
end = time.time()
print(f"solution 2 seconds: {end - start}")