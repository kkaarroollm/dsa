# apply also inserting into binary tree
# do transversal of the tree
# do deletion
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator, Self


# search
# min/ max
# insert
# delete

@dataclass
class _Node:
    value: int
    left: _Node | None = None
    right: _Node | None = None

    def __iter__(self) -> Iterator[int]:
        yield from self.left or []
        yield self.value
        yield from self.right or []


    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)



@dataclass
class BST:
    root: _Node | None = None

    def __bool__(self):
        return bool(self.root)

    def __str__(self) -> str:
        return str(self.root)

    def insert(self, *values) -> Self:
        for value in values:
            self.__insert(value)
        return self

    def __insert(self, value) -> None:
        pass