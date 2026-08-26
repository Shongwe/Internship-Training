from solution import Node, clone_graph


def test_clone_graph():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned = clone_graph(node1)

    assert cloned.val == 1
    assert cloned is not node1
    assert cloned.neighbors[0] is not node2
    assert cloned.neighbors[1] is not node4
