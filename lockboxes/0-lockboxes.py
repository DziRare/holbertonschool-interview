#!/usr/bin/python3
"""Lockboxes Problem"""


def canUnlockAll(boxes):
    """Lockboxes Function"""
    aquired_keys = boxes[0]
    visited_boxes = {0}

    while aquired_keys:
        next_box = aquired_keys.pop()
        visited_boxes.add(next_box)
        aquired_keys += boxes[next_box]
        boxes[next_box] = []

    return len(visited_boxes) == len(boxes)


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
