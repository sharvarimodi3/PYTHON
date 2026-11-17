class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("None")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(1, position - 1):
            if temp is None:
                break
            temp = temp.next

        if temp is None:
            print("Position out of bounds.")
            return

        new_node.next = temp.next
        temp.next = new_node

    def print_middle(self):
        if not self.head:
            print("List is empty, no middle node exists.")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f"Middle node value: {slow.data}")

    def delete_node(self, position):
        if not self.head:
            print("List is empty, nothing to delete.")
            return

        temp = self.head

        if position == 1:
            self.head = temp.next
            temp = None
            return

        prev = None
        for _ in range(1, position):
            if temp is None:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print("Position out of bounds.")
            return

        prev.next = temp.next
        temp = None

    def reverse_list(self):
        prev = None
        current = self.head
         
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def print_consecutive_sums(self):
        if not self.head or not self.head.next:
            print("Not enough elements to calculate consecutive sums.")
            return

        temp = self.head
        print("Consecutive pairs sums: ", end="")
        while temp and temp.next:
            pair_sum = temp.data + temp.next.data
            print(f"{pair_sum} ", end="")
            temp = temp.next
        print()

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(20)
    llist.head.next.next = Node(30)
    llist.head.next.next.next = Node(40)

    print("Initial List:")
    llist.print_list()

    print("\n--- 3. Inserting 25 at position 3 ---")
    llist.insert_at_position(25, 3)
    llist.print_list()

    print("\n--- 4. Finding Middle Node ---")
    llist.print_middle()

    print("\n--- 7. Calculating Consecutive Sums ---")
    llist.print_consecutive_sums()

    print("\n--- 5. Deleting node at position 4 ---")
    llist.delete_node(4)
    llist.print_list()

    print("\n--- 6. Reversing the List ---")
    llist.reverse_list()
    llist.print_list()