
class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both pointers together
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the required node
        slow.next = slow.next.next

        return dummy.next
