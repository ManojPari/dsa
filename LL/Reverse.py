class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Save the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node
    return prev  # New head of the reversed list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original linked list:")
print_linked_list(head)

# Reversing the linked list
reversed_head = reverse_linked_list(head)

print("Reversed linked list:")
print_linked_list(reversed_head)
