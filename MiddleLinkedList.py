"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Finding the middle node
middle = middleNode(head)
print(middle.val)  # Output: 3


# Creating a linked list with an even number of nodes: 1 -> 2 -> 3 -> 4 -> 5 -> 6
head_even = ListNode(1)
head_even.next = ListNode(2)
head_even.next.next = ListNode(3)
head_even.next.next.next = ListNode(4)
head_even.next.next.next.next = ListNode(5)
head_even.next.next.next.next.next = ListNode(6)

# Finding the middle node
middle_even = middleNode(head_even)
print(middle_even.val)  # Output: 4
