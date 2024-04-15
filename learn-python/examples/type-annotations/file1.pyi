from typing import overload, Literal
from a import A
from b import B

@overload
def test_annotation(plugin: Literal["A"]) -> A: ...

@overload
def test_annotation(plugin: Literal["B"]) -> B: ...