#!/usr/bin/env python
from typing import List, Tuple
import time

NUM_SEGMENTS = 3

versions:List[str] = []

with open("order_software_versions/versions_3.txt") as f:
    for l in f:
        line_val = l.strip()

        if line_val == "": continue
        
        versions.append(list(
            map(lambda x: int(x), line_val[1:].split('.'))
        ))

# Keep track of indices, initialize (default) with full list
def order_segments(cur_seg:int=0, start_index:int=0, end_index=len(versions)-1):
    
    if cur_seg == NUM_SEGMENTS: return

    # Sort based on version/sub-version subset
    versions[start_index:end_index + 1] = sorted(
        versions[start_index:end_index + 1], key = lambda x: x[cur_seg]
    )

    # Find indices for each version/sub-version in the current segment
    current_segment_indeces: List[Tuple[int, int]] = []
    current_version = versions[start_index][cur_seg]
    cur_version_starting_index = start_index

    # for i, v in enumerate(versions[start_index:end_index]):
    for i in range(start_index, end_index + 1):
        
        if versions[i][cur_seg] != current_version:
            current_segment_indeces.append((cur_version_starting_index, i - 1))
            cur_version_starting_index = i
            current_version = versions[i][cur_seg]
        
        if i == end_index:
            current_segment_indeces.append((cur_version_starting_index, i))

    # Recurse on each version/sub-version
    for v in current_segment_indeces:
        order_segments(cur_seg + 1, v[0], v[1])


def back_to_str(version_lst: List[int]) -> str:
    return f"v{'.'.join(list(map(lambda x: str(x), version_lst)))}"

start = time.time()
order_segments()
end = time.time()
print(f"my solution seconds: {end - start}")

# for i, v in enumerate(list(map(back_to_str, versions))):
#     print(f"{i + 1}: {v}")