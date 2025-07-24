from collections import deque
from tree import TNode


# Recursive Pre Order Traversal (DFS) Time: O(n), Space: O(n)
def pre_order(node: TNode | None):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)


# Recursive In Order Traversal (DFS) Time: O(n), Space: O(n)
def in_order(node: TNode | None):
    if not node:
        return
    pre_order(node.left)
    print(node)
    pre_order(node.right)


# Iterative Pre Order Traversal (DFS) Time: O(n), Space: O(n)


def pre_order_iterative(node: TNode | None):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if not node:
            return
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)


# Level Order Traversal (BFS) Time: O(n), Space: O(n)


def level_order(node: TNode):
    q: deque = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# Check if Value Exists (DFS): Time O(n), Space: O(n)


def search(node: TNode | None, target: int):
    if not node:
        return False

    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)


# Binary Search Tree
root = TNode(
    8,
    left=TNode(3, left=TNode(1), right=TNode(6, left=TNode(4), right=TNode(7))),
    right=TNode(10, right=TNode(14, left=TNode(13))),
)


# Time: O(log n), Space: O(log n)
def search_bst(node: TNode, target: int):
    if not node:
        return False

    if node.val == target:
        return True

    if target < node.val:
        return search(node.left, target)
    return search(node.right, target)


print(search_bst(root, 3))
