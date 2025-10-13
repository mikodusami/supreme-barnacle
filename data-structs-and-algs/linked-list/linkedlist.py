"""
Linked List Study Guide and Code Template

This file serves as a comprehensive resource for mastering the Linked List data structure,
including core implementations (Singly and Doubly), common interview patterns, and auxiliary utilities.
"""

from typing import Any, List, Optional, TypeVar, Generic

# Type variable for generics
T = TypeVar('T')

# =============================================================================
# I. Core Implementation & Theory (The Foundation)
# =============================================================================

# --- Node Definitions ---

class SLLNode(Generic[T]):
    """
    Node structure for a Singly Linked List.
    """
    def __init__(self, data: T):
        """Initializes a Singly Linked List Node."""
        self.data: T = data
        self.next: Optional['SLLNode[T]'] = None

class DLLNode(Generic[T]):
    """
    Node structure for a Doubly Linked List.
    """
    def __init__(self, data: T):
        """Initializes a Doubly Linked List Node."""
        self.data: T = data
        self.next: Optional['DLLNode[T]'] = None
        self.prev: Optional['DLLNode[T]'] = None

# --- Singly Linked List ---

class SinglyLinkedList(Generic[T]):
    """
    Core implementation of a Singly Linked List (SLL).
    Operations are typically performed from the head.

    Core Operations and Complexities:
    - insert_at_front(data): Prepend to the list.
        Time Complexity: O(1)
        Space Complexity: O(1)
    - insert_at_end(data): Append to the list.
        Time Complexity: O(N) (Requires traversal to the tail)
        Space Complexity: O(1)
    - delete_node(key): Find and remove the first node with the given data key.
        Time Complexity: O(N) (Requires traversal)
        Space Complexity: O(1)
    - search(key): Find the first node with the given data key.
        Time Complexity: O(N)
        Space Complexity: O(1)
    - get_at_index(index): Retrieve element at a specific index.
        Time Complexity: O(N)
        Space Complexity: O(1)
    """

    def __init__(self):
        """Initializes an empty Singly Linked List."""
        self.head: Optional[SLLNode[T]] = None
        self._size: int = 0

    def is_empty(self) -> bool:
        """Checks if the list is empty."""
        return self.head is None

    def size(self) -> int:
        """Returns the number of elements."""
        return self._size

    def insert_at_front(self, data: T) -> None:
        """
        Inserts a new node at the beginning of the list (O(1)).

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_at_end(self, data: T) -> None:
        """
        Inserts a new node at the end of the list (O(N)).

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        new_node = SLLNode(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def delete_node(self, key: T) -> bool:
        """
        Deletes the first node with the specified data key (O(N)).

        Returns:
            bool: True if node was found and deleted, False otherwise.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:  # Key not found
            return False

        if not prev:  # Head node deletion
            self.head = current.next
        else:  # Middle or tail node deletion
            prev.next = current.next

        self._size -= 1
        return True

    def search(self, key: T) -> Optional[SLLNode[T]]:
        """
        Searches for a node with the specified data key (O(N)).

        Returns:
            Optional[SLLNode[T]]: The node if found, None otherwise.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def __str__(self) -> str:
        """String representation of the SLL."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return f"SLL: Head -> {' -> '.join(nodes)} -> None"

# --- Doubly Linked List ---

class DoublyLinkedList(Generic[T]):
    """
    Core implementation of a Doubly Linked List (DLL).
    Supports traversal in both forward and backward directions.

    Core Operations and Complexities (Optimized):
    - insert_at_front(data): Prepend to the list.
        Time Complexity: O(1)
        Space Complexity: O(1)
    - insert_at_end(data): Append to the list.
        Time Complexity: O(1) (Requires a 'tail' pointer)
        Space Complexity: O(1)
    - delete_node(node): Remove a given node.
        Time Complexity: O(1) (If the node reference is given)
        Space Complexity: O(1)
    """
    def __init__(self):
        """Initializes an empty Doubly Linked List."""
        self.head: Optional[DLLNode[T]] = None
        self.tail: Optional[DLLNode[T]] = None  # Crucial for O(1) append
        self._size: int = 0

    def is_empty(self) -> bool:
        """Checks if the list is empty."""
        return self.head is None

    def size(self) -> int:
        """Returns the number of elements."""
        return self._size

    def insert_at_front(self, data: T) -> None:
        """
        Inserts a new node at the beginning of the list (O(1)).

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DLLNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def insert_at_end(self, data: T) -> None:
        """
        Inserts a new node at the end of the list (O(1) with tail pointer).

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DLLNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def delete_node_ref(self, node: DLLNode[T]) -> bool:
        """
        Deletes a specific node given its reference (O(1)).
        Assumes the node is part of this list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not node:
            return False

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next # Node was the head

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev # Node was the tail

        # Clean up node references
        node.next = None
        node.prev = None
        self._size -= 1
        return True

    def __str__(self) -> str:
        """String representation of the DLL (forward traversal)."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return f"DLL: Head <=> {' <=> '.join(nodes)} <=> Tail"

# =============================================================================
# II. LinkedListTemplates Class (Interview Snippets)
# =============================================================================

class LinkedListTemplates:
    """
    A collection of function templates representing common interview problems
    and patterns that utilize the Linked List data structure.
    All assume SLLNode as the standard node structure.
    """

    @staticmethod
    def t01_reverse_list(head: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for iteratively reversing a Singly Linked List (P-I-N pattern).
        Time: O(N), Space: O(1).
        """
        prev = None
        current = head
        while current:
            next_node = current.next # Store next
            current.next = prev      # Reverse current node's pointer
            prev = current           # Move pointers one step ahead
            current = next_node
        return prev # New head is 'prev'

    @staticmethod
    def t02_reverse_list_recursive(head: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for recursively reversing a Singly Linked List.
        Time: O(N), Space: O(N) (stack space).
        """
        if head is None or head.next is None:
            return head

        new_head = LinkedListTemplates.t02_reverse_list_recursive(head.next)
        head.next.next = head # The node after head points back to head
        head.next = None      # Head's next is now None (it's the new tail)
        return new_head

    @staticmethod
    def t03_detect_cycle(head: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for detecting a cycle and finding the start of the cycle
        using Floyd's Tortoise and Hare algorithm (Two Pointers).
        Time: O(N), Space: O(1).
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected. Find the start point.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow # The starting node of the cycle
        return None # No cycle

    @staticmethod
    def t04_get_middle_node(head: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for finding the middle node of a Linked List.
        The 'Hare' moves twice as fast as the 'Tortoise'.
        Time: O(N), Space: O(1).
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow # Returns the second middle node in an even-length list

    @staticmethod
    def t05_merge_two_sorted_lists(l1: Optional[SLLNode[int]], l2: Optional[SLLNode[int]]) -> Optional[SLLNode[int]]:
        """
        Template for merging two sorted Singly Linked Lists.
        Uses a dummy head node to simplify the logic.
        Time: O(N + M), Space: O(1) (no new nodes created).
        """
        dummy = SLLNode(0) # Sentinel node
        current = dummy

        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach the remaining list (one must be None)
        current.next = l1 if l1 else l2
        return dummy.next

    @staticmethod
    def t06_remove_nth_from_end(head: Optional[SLLNode[T]], n: int) -> Optional[SLLNode[T]]:
        """
        Template for removing the N-th node from the end of a list.
        Uses Two Pointers (Fast/Slow) separated by 'n' distance.
        Time: O(N), Space: O(1).
        """
        dummy = SLLNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # Advance fast pointer 'n' steps ahead
        for _ in range(n):
            if fast.next is None: return head # Should not happen with valid input
            fast = fast.next

        # Move both until fast reaches the end
        # slow will be pointing to the node *before* the one to be removed
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete the node (slow.next is the Nth from end)
        slow.next = slow.next.next
        return dummy.next

    @staticmethod
    def t07_reorder_list(head: Optional[SLLNode[T]]) -> None:
        """
        Template for reordering a list from L0 -> L1 -> L2 -> ... -> LN
        to L0 -> LN -> L1 -> L(N-1) -> L2 -> L(N-2) -> ...
        Requires three steps: 1) Find Middle, 2) Reverse Second Half, 3) Merge.
        Time: O(N), Space: O(1).
        """
        if not head or not head.next: return

        # 1. Find the middle (using t04_get_middle_node logic, but need to split)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Head of the second half
        head2 = slow.next
        slow.next = None # Break the list

        # 2. Reverse the second half (using t01_reverse_list logic)
        head2_rev = LinkedListTemplates.t01_reverse_list(head2)

        # 3. Merge the two lists (L1 and L2_rev)
        p1, p2 = head, head2_rev
        while p2:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2

    @staticmethod
    def t08_is_palindrome(head: Optional[SLLNode[T]]) -> bool:
        """
        Template for checking if a Linked List is a palindrome.
        Steps: Find middle, reverse second half, compare, restore.
        Time: O(N), Space: O(1).
        """
        if not head or not head.next: return True

        # 1. Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        head2_rev = LinkedListTemplates.t01_reverse_list(slow)
        p1 = head
        p2 = head2_rev

        # 3. Compare the two halves
        is_pal = True
        while p2:
            if p1.data != p2.data:
                is_pal = False
                break
            p1 = p1.next
            p2 = p2.next

        # (Optional) Restore the original list structure
        # LinkedListTemplates.t01_reverse_list(head2_rev)

        return is_pal

    @staticmethod
    def t09_get_intersection_node(headA: Optional[SLLNode[T]], headB: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for finding the intersection point of two lists.
        Two-pointer trick: Traverse A, then B. Traverse B, then A.
        Total distance traversed is equal: len(A) + len(B).
        Time: O(N + M), Space: O(1).
        """
        pA = headA
        pB = headB
        if not pA or not pB: return None

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA # pA (or pB) is the intersection or None

    @staticmethod
    def t10_partition_list(head: Optional[SLLNode[int]], x: int) -> Optional[SLLNode[int]]:
        """
        Template for partitioning a list around a value 'x'.
        All nodes less than 'x' come before nodes greater than or equal to 'x'.
        Uses two dummy nodes to build two separate lists and link them.
        Time: O(N), Space: O(1).
        """
        less_dummy = SLLNode(0)
        greater_dummy = SLLNode(0)
        less_ptr = less_dummy
        greater_ptr = greater_dummy
        current = head

        while current:
            if current.data < x:
                less_ptr.next = current
                less_ptr = less_ptr.next
            else:
                greater_ptr.next = current
                greater_ptr = greater_ptr.next
            current = current.next

        # Join the two lists
        greater_ptr.next = None # Crucial to terminate the second list
        less_ptr.next = greater_dummy.next
        return less_dummy.next

    @staticmethod
    def t11_swap_nodes_in_pairs(head: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for swapping adjacent nodes in pairs (e.g., 1->2->3->4 becomes 2->1->4->3).
        Uses a dummy node and three pointers (prev, curr, next_node).
        Time: O(N), Space: O(1).
        """
        dummy = SLLNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            # Nodes to be swapped: n1 = prev.next, n2 = prev.next.next
            n1 = prev.next
            n2 = n1.next

            # Perform the swap:
            prev.next = n2
            n1.next = n2.next
            n2.next = n1

            # Move prev pointer two steps forward for the next pair
            prev = n1
        return dummy.next

    @staticmethod
    def t12_rotate_list(head: Optional[SLLNode[T]], k: int) -> Optional[SLLNode[T]]:
        """
        Template for rotating the list to the right by k places.
        Steps: 1) Count length, 2) Form a cycle, 3) Break the cycle at the new head/tail.
        Time: O(N), Space: O(1).
        """
        if not head or k == 0: return head

        # 1. Get length and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Form a cycle (make it circular)
        tail.next = head

        # 3. Calculate rotation point
        # k = k % length. We need to move to length - k (new tail)
        # The new head is at (length - k) % length steps from the old head.
        k %= length
        steps_to_new_tail = length - k

        # Traverse to the new tail
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # 4. Break the cycle and set new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head

    @staticmethod
    def t13_flatten_multilevel_doubly_linked_list(head: Optional[DLLNode]) -> Optional[DLLNode]:
        """
        Template for flattening a multi-level Doubly Linked List where nodes have a 'child' pointer.
        Uses a Stack (or recursion) for DFS-like traversal.

        Note: Requires a DLLNode structure with an additional 'child' attribute.
        (Assuming the problem provides such a structure, though not defined here).
        Time: O(N), Space: O(N) (stack space).
        """
        # Placeholder for implementation logic
        # Implementation uses a Stack to store 'next' pointers when diving into a 'child' list.
        return head

    @staticmethod
    def t14_add_two_numbers(l1: Optional[SLLNode[int]], l2: Optional[SLLNode[int]]) -> Optional[SLLNode[int]]:
        """
        Template for adding two numbers represented by linked lists (digits in reverse order).
        Uses a dummy head and a carry variable.
        Time: O(max(N, M)), Space: O(max(N, M)).
        """
        dummy = SLLNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            current.next = SLLNode(new_digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    @staticmethod
    def t15_copy_list_with_random_pointer(head: Optional[SLLNode[T]]) -> Optional[SLLNode[T]]:
        """
        Template for deep copying a list where nodes have both 'next' and 'random' pointers.
        Uses the three-step approach for O(1) space (excluding copy structure) or a HashMap for O(N) space.
        Time: O(N), Space: O(1) or O(N).
        """
        # O(N) Space approach (using a hash map to map original node to copy node)
        if not head: return None
        old_to_new = {None: None}
        current = head
        while current:
            old_to_new[current] = SLLNode(current.data) # Placeholder for the node with random ptr
            current = current.next

        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new[current.next]
            # Assume a 'random' attribute exists for the actual solution
            # copy.random = old_to_new[current.random]
            current = current.next

        # Return the copy of the head
        return old_to_new[head]

# =============================================================================
# III. LinkedListMentalToolBox Class (Auxiliary Functions)
# =============================================================================

class LinkedListMentalToolBox:
    """
    A collection of auxiliary and utility functions for Linked Lists,
    useful for testing, debugging, and structural analysis.
    """

    @staticmethod
    def tbx01_list_to_sll(data_list: List[T]) -> SinglyLinkedList[T]:
        """
        Converts a standard Python list into a Singly Linked List object.
        """
        sll = SinglyLinkedList[T]()
        if not data_list:
            return sll
        
        # Build in reverse order for O(1) prepending, or use O(N) append for natural order
        for item in reversed(data_list):
            sll.insert_at_front(item)
        return sll

    @staticmethod
    def tbx02_sll_to_list(sll: SinglyLinkedList[T]) -> List[T]:
        """
        Dumps the contents of an SLL into a standard Python list.
        """
        data_list = []
        current = sll.head
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list

    @staticmethod
    def tbx03_create_cycle(sll: SinglyLinkedList[T], pos: int) -> None:
        """
        Creates a cycle in the SLL where the tail points to the node at 'pos' (0-indexed).
        If pos is -1, no cycle is created.
        """
        if sll.is_empty() or pos < 0:
            return

        tail = None
        target_node = None
        current = sll.head
        index = 0

        while current.next:
            if index == pos:
                target_node = current
            current = current.next
            index += 1

        if index == pos: # Handle case where pos is the last node
            target_node = current

        tail = current
        if tail and target_node:
            tail.next = target_node

    @staticmethod
    def tbx04_check_structural_integrity_sll(head: Optional[SLLNode[T]]) -> bool:
        """
        Checks for basic structural integrity (no self-loops and no cycles on a small list).
        Primarily a traversal check; detects cycles on large lists via slow/fast.
        Returns False if a cycle is detected.
        """
        if not head: return True
        slow = head
        fast = head
        limit = 2000 # Heuristic limit for cycle detection if length is unknown

        for _ in range(limit):
            if fast is None or fast.next is None:
                return True # Reached end, no cycle

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return False # Cycle detected

        return True # Assumes no cycle if limit reached

    @staticmethod
    def tbx05_print_list_with_limit(head: Optional[SLLNode[Any]], limit: int = 15) -> str:
        """
        Prints the list's contents but stops after 'limit' nodes to prevent infinite loops from cycles.
        """
        nodes = []
        current = head
        count = 0
        while current and count < limit:
            nodes.append(str(current.data))
            current = current.next
            count += 1

        output = " -> ".join(nodes)
        if current:
            output += " -> ... (Cycle/Truncated)"
        else:
            output += " -> None"
        return output

    @staticmethod
    def tbx06_find_node_at_index(head: Optional[SLLNode[T]], index: int) -> Optional[SLLNode[T]]:
        """
        Finds the node at a specific zero-based index in the list.
        """
        current = head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None

    @staticmethod
    def tbx07_length_of_list(head: Optional[SLLNode[T]]) -> int:
        """
        Calculates the length of the list (stops if cycle detected by limit).
        """
        length = 0
        current = head
        limit = 2000
        while current and length < limit:
            length += 1
            current = current.next
        return length

    @staticmethod
    def tbx08_create_two_intersecting_slls(list_a: List[int], list_b_tail: List[int], intersect_idx: int) -> tuple[SinglyLinkedList[int], SinglyLinkedList[int]]:
        """
        Creates two SLLs that intersect at a specific node of list A.
        """
        sll_a = LinkedListMentalToolBox.tbx01_list_to_sll(list_a)
        intersection_node = LinkedListMentalToolBox.tbx06_find_node_at_index(sll_a.head, intersect_idx)

        sll_b = SinglyLinkedList[int]()
        current_b = None
        
        # Build B's non-intersecting part
        for val in list_b_tail:
            new_node = SLLNode(val)
            if not sll_b.head:
                sll_b.head = new_node
                current_b = new_node
            else:
                current_b.next = new_node
                current_b = new_node
            sll_b._size += 1

        # Link B's tail to A's intersection node
        if current_b and intersection_node:
            current_b.next = intersection_node
            # Recalculate size of B from the intersection point
            sll_b._size = len(list_b_tail) + (sll_a._size - intersect_idx)

        return sll_a, sll_b

    @staticmethod
    def tbx09_print_dll_backward(dll: DoublyLinkedList[T]) -> str:
        """
        Prints the DLL contents traversing from tail to head using the prev pointer.
        """
        nodes = []
        current = dll.tail
        while current:
            nodes.append(str(current.data))
            current = current.prev
        return f"DLL: Tail <- {' <- '.join(nodes)} <- Head"

    @staticmethod
    def tbx10_reverse_list_in_groups(head: Optional[SLLNode[T]], k: int) -> Optional[SLLNode[T]]:
        """
        Auxiliary function for reversing the list in groups of size k.
        A classic, complex list manipulation pattern.
        """
        current = head
        prev_tail = None # Tail of the previously reversed segment
        new_head = None # New head of the entire list

        while current:
            # 1. Identify the current group to reverse
            segment_head = current
            segment_prev = None
            segment_end = current
            count = 0
            while segment_end and count < k:
                segment_end = segment_end.next
                count += 1
            
            # If the remaining list is smaller than k, don't reverse
            if count < k and not segment_end:
                 if prev_tail:
                    prev_tail.next = segment_head
                 break

            # 2. Reverse the segment (k nodes)
            new_segment_head = None # Will be the original segment_tail
            p = segment_head
            for _ in range(k):
                next_node = p.next
                p.next = segment_prev
                segment_prev = p
                p = next_node
            new_segment_head = segment_prev # The new head of this reversed segment

            # 3. Connect the reversed segment to the result
            if not new_head:
                new_head = new_segment_head
            if prev_tail:
                prev_tail.next = new_segment_head

            # 4. Update pointers for the next iteration
            prev_tail = segment_head # The old head is now the tail
            current = p # Start of the next segment (or None)

        return new_head or head

if __name__ == '__main__':
    # =========================================================================
    # Example Usage and Testing
    # =========================================================================

    # I. Core Implementation Test (SinglyLinkedList)
    sll = SinglyLinkedList[int]()
    sll.insert_at_front(10)
    sll.insert_at_end(30)
    sll.insert_at_front(5)
    sll.insert_at_end(40)
    # print(str(sll)) # SLL: Head -> 5 -> 10 -> 30 -> 40 -> None

    # sll.delete_node(30)
    # print(str(sll)) # SLL: Head -> 5 -> 10 -> 40 -> None

    # II. Interview Template Test (Reverse List)
    # reversed_head = LinkedListTemplates.t01_reverse_list(sll.head)
    # sll_reversed = SinglyLinkedList[int]()
    # sll_reversed.head = reversed_head
    # sll_reversed._size = sll.size()
    # print(LinkedListMentalToolBox.tbx05_print_list_with_limit(sll_reversed.head, 15)) # 40 -> 10 -> 5 -> None

    # III. Mental ToolBox Test
    list_a_data = [1, 2, 3, 4, 5, 6]
    list_b_tail_data = [10, 20, 30]
    list_a, list_b = LinkedListMentalToolBox.tbx08_create_two_intersecting_slls(list_a_data, list_b_tail_data, 3)
    # print(f"List A: {LinkedListMentalToolBox.tbx05_print_list_with_limit(list_a.head)}") # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    # print(f"List B: {LinkedListMentalToolBox.tbx05_print_list_with_limit(list_b.head)}") # 10 -> 20 -> 30 -> 4 -> 5 -> 6 -> None
    # print(f"Intersection Node: {LinkedListTemplates.t09_get_intersection_node(list_a.head, list_b.head).data}") # 4

    # DLL Test
    dll = DoublyLinkedList[str]()
    dll.insert_at_front("C")
    dll.insert_at_end("D")
    dll.insert_at_front("B")
    # print(str(dll)) # DLL: Head <=> B <=> C <=> D <=> Tail
    # print(LinkedListMentalToolBox.tbx09_print_dll_backward(dll)) # DLL: Tail <- D <- C <- B <- Head
    pass