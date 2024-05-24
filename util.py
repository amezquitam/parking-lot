from typing import Callable, Any

def make_matrix(size: int, value: Callable[[int, int], Any]):
    return [[value(row, col, size) for col in range(size)] for row in range(size)]
