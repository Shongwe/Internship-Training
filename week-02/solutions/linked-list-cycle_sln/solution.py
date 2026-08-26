class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's Tortoise & Hare algorithm.
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


def main():
    # Test cases
    head1 = ListNode(3)
    head1.next = ListNode(2)
    head1.next.next = ListNode(0)
    tail1 = ListNode(-4)
    head1.next.next.next = tail1
    tail1.next = head1.next  # cycle
    print("Cycle exists (expected True):", has_cycle(head1))

    head2 = ListNode(1)
    head2.next = ListNode(2)
    print("Cycle exists (expected False):", has_cycle(head2))

    head3 = ListNode(1)
    print("Cycle exists (expected False):", has_cycle(head3))

    head4 = ListNode(1)
    head4.next = head4  # cycle to itself
    print("Cycle exists (expected True):", has_cycle(head4))


if __name__ == "__main__":
    main()
