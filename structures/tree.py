from __future__ import annotations

class TNode:
    def __init__(
        self, val: int, left: TNode | None = None, right: TNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TNode({self.val})"



tree_root = TNode(
    1,
    left=TNode(
        2,
        left=TNode(
            4,
            left=TNode(8),
            right=TNode(9)
        ),
        right=TNode(
            5,
            left=TNode(10),
            right=TNode(11)
        )
    ),
    right=TNode(
        3,
        left=TNode(
            6,
            left=TNode(12),
            right=TNode(13)
        ),
        right=TNode(
            7,
            left=TNode(14),
            right=TNode(15)
        )
    )
)
