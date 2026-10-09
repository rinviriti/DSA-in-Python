"""Worked example: linear search in a list.

This is a teaching example, not a claimed LeetCode solution.
Time: O(n) in the worst case.
Extra space: O(1).
"""


def linear_search(values: list[int], target: int) -> int:
    """Return the first matching index; return -1 when target is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
