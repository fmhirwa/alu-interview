#!/usr/bin/python3
"""Prototype: def rain(walls)
Return: An integer indicating total amount of rainwater retained.
If the list is empty, will return 0."""


def rain(walls):
    if len(walls) < 3:
        return 0

    total_water = 0
    left = 0
    right = len(walls) - 1
    left_max = walls[left]
    right_max = walls[right]

    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            total_water += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            total_water += right_max - walls[right]
            right -= 1

    return total_water
