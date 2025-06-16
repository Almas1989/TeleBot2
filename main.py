import math
import pprint
from typing import Tuple

print("Hello, World!")


def foo(x: int) -> Tuple[int, float]:
    """Returns a tuple of the sum and product of x and y."""
    return x, math.pi

pprint.pprint('Hello')


print(foo(4))