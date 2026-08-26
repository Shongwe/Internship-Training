class Node:
    """Represent a node in an undirected graph."""

    def __init__(self, val: int = 0, neighbors: list | None = None):
        """
        Initialize a graph node.

        Args:
            val: The value of the node.
            neighbors: A list of neighboring nodes.
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    """
    Create a deep copy of a connected undirected graph.

    Args:
        node: The starting node of the graph.

    Returns:
        The starting node of the cloned graph, or None if the
        input graph is empty.
    """
    if node is None:
        return None

    visited = {}

    def dfs(original: Node) -> Node:
        """Clone a node and recursively clone its neighbors."""
        if original in visited:
            return visited[original]

        copy = Node(original.val)
        visited[original] = copy

        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)