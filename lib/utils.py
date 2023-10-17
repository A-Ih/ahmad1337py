from typing import Callable

def two_sum(a: int, b: int):
    return a + b

class RequirementError(Exception):
    pass

def require(condition: bool, lazy_msg: Callable[[], str]) -> None:
    if condition:
        return
    raise RequirementError(lazy_msg())
    