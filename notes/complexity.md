# Complexity notes

## Common patterns

| Operation / algorithm | Typical time | Notes |
|---|---|---|
| Direct list indexing | O(1) | Access by known index |
| Scan an unsorted list | O(n) | Worst case visits every element |
| Nested scans of the same n elements | O(n²) | Example: trying every pair |
| Python `set` / `dict` lookup | O(1) average | Worst-case behavior is not guaranteed constant |
| Binary search on sorted data | O(log n) | Halves the search interval |
| Python list sort | O(n log n) typical/worst | Uses Timsort; implementation dependent |

## Important distinctions

- Time complexity describes how runtime scales with input size.
- Auxiliary space complexity excludes the input itself unless stated otherwise.
- A faster average-case hash-table lookup often uses extra memory.
- Explain assumptions before claiming complexity.

## Self-check

1. What is the worst-case time of visiting every list element once?
2. What changes if a second full scan is nested inside the first?
3. Why can a dictionary-based solution use more space than a nested-loop solution?
