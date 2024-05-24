from typing import Callable, TypeVar, List

T = TypeVar('T')

def make_matrix(size: int, value: Callable[[int, int], T]) -> List[List[T]]:
    return [[value(row, col, size) for col in range(size)] for row in range(size)]
