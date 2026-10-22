class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node pointing to head to handle edge cases (e.g., removing the head node)
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Advance fast pointer by n + 1 steps to create an n-node gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Skip the nth node from the end
        slow.next = slow.next.next

        return dummy.next
