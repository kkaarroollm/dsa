import networkx as nx


def hierarchy_pos(
    G: nx.DiGraph,
    root: str | None = None,
    width: float = 1.0,
    vert_gap: float = 0.2,
    vert_loc: float = 0,
    x_center: float = 0.5,
    pos: dict[str, tuple[float, float]] | None = None,
    parent: str | None = None,
) -> dict[str, tuple[float, float]]:
    if pos is None:
        pos = {}
    pos[root] = (x_center, vert_loc)
    children = list(G.successors(root))
    if children:
        dx = width / len(children)
        next_x = x_center - width / 2 - dx / 2
        for child in children:
            next_x += dx
            pos = hierarchy_pos(
                G,
                root=child,
                width=dx,
                vert_gap=vert_gap,
                vert_loc=vert_loc - vert_gap,
                x_center=next_x,
                pos=pos,
                parent=root,
            )
    return pos
