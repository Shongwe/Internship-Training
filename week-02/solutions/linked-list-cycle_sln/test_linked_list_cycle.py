from solution import ListNode, has_cycle


def test_cycle_exists():
    # Create linked list: 3 -> 2 -> 0 -> -4 -> (points back to 2)
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    tail = ListNode(-4)
    head.next.next.next = tail
    tail.next = head.next  # cycle

    assert has_cycle(head) is True


def test_no_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    assert has_cycle(head) is False


def test_single_node_no_cycle():
    head = ListNode(1)
    assert has_cycle(head) is False


def test_single_node_cycle():
    head = ListNode(1)
    head.next = head  # cycle to itself
    assert has_cycle(head) is True
