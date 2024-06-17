class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Print the original linked list
print("Original Linked List:")
current = head
while current is not None:
    print(current.value, end=" ")
    current = current.next

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("\nReversed Linked List:")
current = head
while current is not None:
    print(current.value, end=" ")
    current = current.next
