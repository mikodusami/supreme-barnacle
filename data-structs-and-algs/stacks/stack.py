"""
Stack Study Guide and Code Template

This file serves as a comprehensive resource for mastering the Stack data structure,
including core implementations, common interview patterns, and auxiliary utilities.
"""

from typing import Any, List, Optional, TypeVar, Generic

# Type variable for generics
T = TypeVar('T')

# =============================================================================
# I. Core Implementation & Theory (The Foundation)
# =============================================================================

class ArrayStack(Generic[T]):
    """
    Core implementation of a Stack using a Python list (dynamic array).
    This is the most common and practical implementation in Python.
    A Stack is a LIFO (Last-In, First-Out) data structure.

    Core Operations and Complexities:
    - push(item): Add an element to the top of the stack.
        Time Complexity: O(1) Amortized (due to dynamic array resizing)
        Space Complexity: O(N) where N is the number of elements.
    - pop(): Remove and return the top element.
        Time Complexity: O(1)
        Space Complexity: O(1)
    - peek(): Return the top element without removing it.
        Time Complexity: O(1)
        Space Complexity: O(1)
    - is_empty(): Check if the stack is empty.
        Time Complexity: O(1)
        Space Complexity: O(1)
    - size(): Return the number of elements.
        Time Complexity: O(1)
        Space Complexity: O(1)
    """

    def __init__(self):
        """Initializes an empty ArrayStack."""
        self._items: List[T] = []

    def is_empty(self) -> bool:
        """
        Checks if the stack contains any elements.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return not self._items

    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack.

        Args:
            item: The element to be added.

        Time Complexity: O(1) Amortized
        Space Complexity: O(1)
        """
        self._items.append(item)

    def pop(self) -> T:
        """
        Removes and returns the item from the top of the stack.

        Raises:
            IndexError: If the stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """
        Returns the item from the top of the stack without removing it.

        Raises:
            IndexError: If the stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self) -> int:
        """
        Returns the current number of elements in the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items)

    def __len__(self) -> int:
        return self.size()

    def __str__(self) -> str:
        return f"Stack -> Top[{', '.join(map(str, reversed(self._items)))}]Bottom"


class Node(Generic[T]):
    """Helper class for LinkedStack nodes."""
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None

class LinkedStack(Generic[T]):
    """
    Alternative implementation of a Stack using a Singly Linked List.
    The 'head' of the list is considered the 'top' of the stack for O(1) operations.

    Core Operations and Complexities:
    - push(item): Add an element to the top (head) of the list.
        Time Complexity: O(1)
        Space Complexity: O(N)
    - pop(): Remove and return the top element (head).
        Time Complexity: O(1)
        Space Complexity: O(1)
    - peek(): Return the top element (head).
        Time Complexity: O(1)
        Space Complexity: O(1)
    """

    def __init__(self):
        """Initializes an empty LinkedStack."""
        self._top: Optional[Node[T]] = None
        self._size: int = 0

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._top is None

    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack (prepends to the linked list).

        Args:
            item: The element to be added.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self) -> T:
        """
        Removes and returns the item from the top of the stack (removes the head).

        Raises:
            IndexError: If the stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self) -> T:
        """
        Returns the item from the top of the stack without removing it.

        Raises:
            IndexError: If the stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.data

    def size(self) -> int:
        """
        Returns the current number of elements in the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._size

# =============================================================================
# II. StackTemplates Class (Interview Snippets)
# =============================================================================

class StackTemplates:
    """
    A collection of function templates representing common interview problems
    and patterns that utilize the Stack data structure.
    """

    @staticmethod
    def t01_valid_parentheses(s: str) -> bool:
        """
        Template for checking if a string containing '()', '{}', '[]' is valid.
        Uses a stack to store opening brackets and match them with closing ones.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        # Iterate and push openers, pop and check for matches on closers.
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

    @staticmethod
    def t02_remove_adjacent_duplicates(s: str) -> str:
        """
        Template for removing all adjacent duplicate characters in a string
        (e.g., 'abbaca' -> 'aaca' -> 'ca'). Stack holds characters that remain.
        """
        stack = []
        # Push if stack is empty or top is different, otherwise pop (remove duplicate).
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

    @staticmethod
    def t03_next_greater_element(nums: List[int]) -> List[int]:
        """
        Template for finding the Next Greater Element for every element in an array.
        Uses a Monotonic Stack (decreasing) to efficiently find the next larger number.
        """
        stack = []  # Stores indices
        result = [-1] * len(nums)
        # Iterate and maintain a stack of indices for which NGE hasn't been found.
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            stack.append(i)
        return result

    @staticmethod
    def t04_largest_rectangle_in_histogram(heights: List[int]) -> int:
        """
        Template for finding the largest rectangle area in a histogram.
        A classic Monotonic Stack problem (increasing). Stack stores indices.
        """
        stack = [-1]  # Sentinel for calculation
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1  # current index minus new top index minus 1
                max_area = max(max_area, height * width)
            stack.append(i)

        # Process remaining bars
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area

    @staticmethod
    def t05_min_stack_design(operation_list: List[tuple]) -> List[Any]:
        """
        Template for designing a MinStack (a stack that supports push, pop, top,
        and retrieving the minimum element in O(1) time). Typically uses two stacks.
        """
        class MinStack:
            def __init__(self):
                self.stack = ArrayStack()       # Main data stack
                self.min_stack = ArrayStack()   # Auxiliary stack for minimums

            def push(self, val: int) -> None:
                self.stack.push(val)
                new_min = min(val, self.min_stack.peek() if not self.min_stack.is_empty() else val)
                self.min_stack.push(new_min)

            def pop(self) -> Optional[int]:
                if self.stack.is_empty(): return None
                self.min_stack.pop()
                return self.stack.pop()

            def getMin(self) -> Optional[int]:
                return self.min_stack.peek() if not self.min_stack.is_empty() else None

        # This part is just to show how to use the template/class
        results = []
        ms = MinStack()
        for op, val in operation_list:
            if op == 'push': ms.push(val)
            elif op == 'pop': results.append(ms.pop())
            elif op == 'getMin': results.append(ms.getMin())
            elif op == 'top': results.append(ms.stack.peek() if not ms.stack.is_empty() else None)
        return results

    @staticmethod
    def t06_decode_string(s: str) -> str:
        """
        Template for decoding a string with encoded parts like '3[a2[c]]'.
        Uses two stacks: one for numbers (counts) and one for strings.
        """
        count_stack = []
        string_stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0
                current_string = ""
            elif char == ']':
                repeat_count = count_stack.pop()
                prev_string = string_stack.pop()
                current_string = prev_string + current_string * repeat_count
            else:
                current_string += char
        return current_string

    @staticmethod
    def t07_reverse_polish_notation(tokens: List[str]) -> int:
        """
        Template for evaluating an expression in Reverse Polish Notation (Postfix).
        Uses a stack to hold operands, popping two for an operation result.
        """
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+': stack.append(operand1 + operand2)
                elif token == '-': stack.append(operand1 - operand2)
                elif token == '*': stack.append(operand1 * operand2)
                elif token == '/': stack.append(int(operand1 / operand2)) # Integer division for RPN
        return stack[0]

    @staticmethod
    def t08_simplify_path(path: str) -> str:
        """
        Template for simplifying a Unix-style absolute path.
        Stack is used to process directory names, ignoring '.', '..', and empty strings.
        """
        stack = []
        components = path.split('/')
        for comp in components:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        return "/" + "/".join(stack)

    @staticmethod
    def t09_basic_calculator_ii(s: str) -> int:
        """
        Template for implementing a basic calculator that evaluates a simple expression string
        containing non-negative integers, '+', '-', '*', '/' and spaces.
        Uses a stack to handle operator precedence (*, / before +, -).
        """
        num = 0
        last_op = '+'
        stack = []
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if (not char.isdigit() and not char.isspace()) or i == len(s) - 1:
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    stack.append(stack.pop() * num)
                elif last_op == '/':
                    # Note: Python's // behaves like integer division toward negative infinity,
                    # but problem usually requires truncation toward zero.
                    top = stack.pop()
                    stack.append(int(top / num))
                last_op = char
                num = 0
        return sum(stack)

    @staticmethod
    def t10_daily_temperatures(temperatures: List[int]) -> List[int]:
        """
        Template for calculating the number of days until a warmer temperature occurs.
        Uses a Monotonic Stack (decreasing) to store the indices of temperatures.
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices [i]
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer

    @staticmethod
    def t11_implement_queue_using_stacks(ops: List[str]) -> List[Any]:
        """
        Template for implementing a Queue (FIFO) using two Stacks.
        One stack for input (push), one for output (pop/peek).
        Transfer is done only when output stack is empty and a pop/peek is requested.
        """
        class MyQueue:
            def __init__(self):
                self.s_in = ArrayStack()
                self.s_out = ArrayStack()

            def push(self, x: int) -> None:
                self.s_in.push(x)

            def _transfer(self) -> None:
                if self.s_out.is_empty():
                    while not self.s_in.is_empty():
                        self.s_out.push(self.s_in.pop())

            def pop(self) -> Optional[int]:
                self._transfer()
                return self.s_out.pop() if not self.s_out.is_empty() else None

            def peek(self) -> Optional[int]:
                self._transfer()
                return self.s_out.peek() if not self.s_out.is_empty() else None

        # This part is for demonstration of usage
        results = []
        q = MyQueue()
        # Assume ops is a list of tuples like [('push', 1), ('pop', None), ...]
        # Placeholder for actual execution logic
        return results # Placeholder

    @staticmethod
    def t12_remove_k_digits(num: str, k: int) -> str:
        """
        Template for removing K digits from a number to make the smallest possible new number.
        Uses a Monotonic Stack (increasing) to greedily build the smallest number.
        """
        stack = []
        removals = k
        for digit in num:
            while stack and removals > 0 and stack[-1] > digit:
                stack.pop()
                removals -= 1
            stack.append(digit)

        # Handle case where all digits are in non-decreasing order (e.g., "12345")
        final_stack = stack[:-removals] if removals > 0 else stack

        # Join and remove leading zeros
        result = "".join(final_stack).lstrip('0')
        return result if result else "0"

    @staticmethod
    def t13_asteroid_collision(asteroids: List[int]) -> List[int]:
        """
        Template for simulating asteroid collisions. Positive moves right, negative moves left.
        Stack stores asteroids moving right or the survivors.
        """
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue # The right-mover is destroyed, check the new top
                elif stack[-1] == abs(a):
                    stack.pop()
                break # Current left-mover is destroyed or both are destroyed
            else:
                stack.append(a)
        return stack

    @staticmethod
    def t14_trapping_rain_water(heights: List[int]) -> int:
        """
        Template for calculating the water trapped between blocks.
        Uses a stack to store indices, calculating trapped water when a taller bar is found.
        """
        stack = [] # Stores indices of bars forming a decreasing sequence
        total_water = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] < height:
                bottom_index = stack.pop()
                if not stack:
                    break
                left_boundary_index = stack[-1]
                # Water trapped = min(left, right) - height_at_bottom * width
                h = min(height, heights[left_boundary_index]) - heights[bottom_index]
                w = i - left_boundary_index - 1
                total_water += h * w
            stack.append(i)
        return total_water

    @staticmethod
    def t15_remove_outermost_parentheses(s: str) -> str:
        """
        Template for removing the outermost parentheses of every primitive decomposition of a valid parentheses string.
        Uses a counter or a stack to track the nesting level.
        """
        stack_level = 0
        result = []
        for char in s:
            if char == '(':
                if stack_level > 0:
                    result.append(char)
                stack_level += 1
            elif char == ')':
                stack_level -= 1
                if stack_level > 0:
                    result.append(char)
        return "".join(result)

# =============================================================================
# III. StackMentalToolBox Class (Auxiliary Functions)
# =============================================================================

class StackMentalToolBox:
    """
    A collection of auxiliary and utility functions for stacks,
    useful for testing, debugging, and structural analysis.
    """

    @staticmethod
    def tbx01_generate_random_stack(min_val: int = 1, max_val: int = 100, size: int = 10) -> ArrayStack[int]:
        """
        Generates an ArrayStack with a specified number of random integer elements.
        """
        import random
        stack = ArrayStack[int]()
        for _ in range(size):
            stack.push(random.randint(min_val, max_val))
        return stack

    @staticmethod
    def tbx02_transfer_to_list(stack: ArrayStack[T]) -> List[T]:
        """
        Dumps the contents of an ArrayStack into a list, ordered from top to bottom.
        Modifies the original stack (destructive).
        """
        result = []
        while not stack.is_empty():
            result.append(stack.pop())
        return result

    @staticmethod
    def tbx03_transfer_to_list_non_destructive(stack: ArrayStack[T]) -> List[T]:
        """
        Returns the contents of an ArrayStack as a list (top-to-bottom) without modifying the original stack.
        Requires O(N) auxiliary space for a temporary stack.
        """
        temp_stack = ArrayStack[T]()
        # Copy contents to temporary stack (reverses order)
        for item in stack._items: # Accessing internal list for non-destructive read
            temp_stack.push(item)

        result = []
        # Pop from temporary stack (restores original order)
        while not temp_stack.is_empty():
            result.append(temp_stack.pop())

        return result

    @staticmethod
    def tbx04_check_monotonicity_increasing(stack: List[int]) -> bool:
        """
        Checks if the provided list (representing a stack, top is at the end) is monotonically increasing
        from bottom to top (i.e., stack[-1] >= stack[-2] >= ...).
        Useful for debugging Monotonic Stack problems.
        """
        for i in range(len(stack) - 1):
            if stack[i] > stack[i+1]: # Comparing current to the one above it
                return False
        return True

    @staticmethod
    def tbx05_check_monotonicity_decreasing(stack: List[int]) -> bool:
        """
        Checks if the provided list (representing a stack, top is at the end) is monotonically decreasing
        from bottom to top (i.e., stack[-1] <= stack[-2] <= ...).
        """
        for i in range(len(stack) - 1):
            if stack[i] < stack[i+1]:
                return False
        return True

    @staticmethod
    def tbx06_recursive_stack_reversal(stack: ArrayStack[T]) -> None:
        """
        Reverses the contents of a stack using recursion without using another stack or auxiliary data structure.
        Helper function required to insert at the bottom.
        """
        def insert_at_bottom(stk: ArrayStack[T], item: T) -> None:
            if stk.is_empty():
                stk.push(item)
            else:
                temp = stk.pop()
                insert_at_bottom(stk, item)
                stk.push(temp)

        if not stack.is_empty():
            temp = stack.pop()
            StackMentalToolBox.tbx06_recursive_stack_reversal(stack)
            insert_at_bottom(stack, temp)

    @staticmethod
    def tbx07_check_invariant_linked_stack(stack: LinkedStack) -> bool:
        """
        Checks the structural invariant of a LinkedStack: size must match the number of traversed nodes.
        """
        count = 0
        current = stack._top
        while current is not None:
            count += 1
            current = current.next
        return count == stack._size

    @staticmethod
    def tbx08_evaluate_stack_equality(s1: ArrayStack[T], s2: ArrayStack[T]) -> bool:
        """
        Compares two stacks for equality by recursively checking their contents without modifying them.
        This is typically for test case comparison.
        """
        if s1.size() != s2.size():
            return False

        temp1 = []
        temp2 = []
        is_equal = True

        # Destructive comparison
        while not s1.is_empty() and not s2.is_empty():
            item1 = s1.pop()
            item2 = s2.pop()
            temp1.append(item1)
            temp2.append(item2)
            if item1 != item2:
                is_equal = False
                break

        # Restore stacks
        for item in reversed(temp1):
            s1.push(item)
        for item in reversed(temp2):
            s2.push(item)

        return is_equal

    @staticmethod
    def tbx09_get_kth_element_from_top(stack: ArrayStack[T], k: int) -> Optional[T]:
        """
        Returns the K-th element from the top of the stack (1-indexed). O(1) for ArrayStack.
        """
        if k <= 0 or k > stack.size():
            return None
        # ArrayStack's top is at index -1, k-th element is at index -k
        return stack._items[-k]

    @staticmethod
    def tbx10_visualize_stack(stack: ArrayStack[Any], label: str = "Stack") -> None:
        """
        Prints a simple vertical visualization of the ArrayStack contents.
        """
        print(f"--- {label} (Size: {stack.size()}) ---")
        if stack.is_empty():
            print("  [ Empty ]")
            print("----------------------")
            return

        items = list(reversed(stack._items)) # Reverse to show top first
        for i, item in enumerate(items):
            pointer = " <- TOP" if i == 0 else ""
            print(f"| {str(item):<10} |{pointer}")
        print("-------------")
        print("  [ Bottom ]")

if __name__ == '__main__':
    # =========================================================================
    # Example Usage and Testing
    # =========================================================================

    # I. Core Implementation Test (ArrayStack)
    s = ArrayStack[int]()
    s.push(10)
    s.push(20)
    s.push(30)
    # print(str(s)) # Output: Stack -> Top[30, 20, 10]Bottom

    # II. Interview Template Test (Valid Parentheses)
    # print(f"Valid Parentheses '([]){{}}': {StackTemplates.t01_valid_parentheses('([]){{}')}")

    # III. Mental ToolBox Test
    random_stack = StackMentalToolBox.tbx01_generate_random_stack(size=5)
    # StackMentalToolBox.tbx10_visualize_stack(random_stack, "Random Stack")

    # LinkedStack Test
    ls = LinkedStack[str]()
    ls.push("A")
    ls.push("B")
    ls.pop()
    # print(f"Linked Stack Size: {ls.size()}, Top: {ls.peek()}")
    # print(f"Linked Stack Invariant Check: {StackMentalToolBox.tbx07_check_invariant_linked_stack(ls)}")
    pass