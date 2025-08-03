import networkx as nx


def build_fib_graph(n: int) -> nx.DiGraph:
    G = nx.DiGraph()

    def add_nodes(current_n: int, parent: str = None):
        node = f"fib({current_n})"
        G.add_node(node)

        if parent:
            G.add_edge(parent, node)

        if current_n > 1:
            add_nodes(current_n - 1, node)
            add_nodes(current_n - 2, node)

    add_nodes(n)
    return G
