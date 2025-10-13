## Monotonic Stacks

A **Monotonic Stack** is a specialized variation of the standard **Stack** data structure where the elements are kept in a specific order—either strictly increasing (or non-decreasing) or strictly decreasing (or non-increasing) from the bottom to the top. The "monotonic" refers to this consistent, non-changing trend in the sequence of values within the stack. This property is enforced during the `push` operation, making it an essential technique for solving problems that require finding the **Next Greater Element (NGE)** or **Next Smaller Element (NSE)** efficiently.

***

## I. Core Concepts

### What is Monotonicity?

The term **monotonic** comes from mathematics and describes a sequence that is consistently moving in one direction.

* **Monotonically Increasing (or Non-Decreasing) Stack:** As you traverse the elements from the bottom of the stack to the top, the value of each element must be greater than or equal to the value of the element below it. $A_1 \le A_2 \le A_3 \le \dots \le A_n$, where $A_n$ is the top element.
* **Monotonically Decreasing (or Non-Increasing) Stack:** As you traverse the elements from the bottom of the stack to the top, the value of each element must be less than or equal to the value of the element below it. $A_1 \ge A_2 \ge A_3 \ge \dots \ge A_n$, where $A_n$ is the top element.

**Simple Explanation (Non-Technical):** A Monotonic Stack is a stack of numbers where the numbers are *always* arranged in order (either getting bigger or getting smaller) from the bottom plate to the top plate. If a new number breaks that order, you must remove the plates that spoil the order before placing the new one.

### How Monotonic Stacks Operate

The key difference from a standard stack is the process of insertion (`push`). Before a new element is pushed onto the top, it must satisfy the monotonicity property with respect to the current top element.

1.  **Check Monotonicity:** When a new element, $X$, arrives, you compare it with the element currently at the top of the stack, $T$.
2.  **Maintain Order (Pop):** If $X$ violates the stack's monotonicity rule (e.g., in a Monotonically Increasing Stack, if $X < T$), the element $T$ is **popped** off the stack. This process repeats: as long as the new element violates the rule, elements are continuously popped.
3.  **Insert (Push):** Once the top element satisfies the rule (or the stack is empty), the new element $X$ is **pushed** onto the stack.

**Simple Explanation (Non-Technical):**
* **Monotonically Increasing Stack (Getting Bigger):** If you try to put a *smaller* number on top of a *bigger* number, the bigger number (and any others below it that are too big) must first be removed. Only then can the new, smaller number be placed on top of a smaller number.
* **The Power:** When an element is popped, the incoming element ($X$) is guaranteed to be the **Next Smaller Element (NSE)** for all the elements it popped. This relationship is what makes Monotonic Stacks useful.

### Applications: Next Greater/Smaller Element

Monotonic Stacks are highly efficient for computing the **Next Greater Element (NGE)** or **Next Smaller Element (NSE)** for every element in an array in a single pass ($O(N)$ time complexity).

#### Finding the Next Greater Element (NGE)

To find the NGE for all elements in an array:

1.  Use a **Monotonically Decreasing Stack**. (The stack stores indices or values in decreasing order).
2.  Iterate through the array. For the current element, $X$:
    * While the stack is *not empty* and $X$ is **greater than** the element at the top of the stack ($X$ violates the decreasing order):
        * **Pop** the top element, $T$.
        * $X$ is the **Next Greater Element** for $T$.
    * **Push** $X$ onto the stack.

**Why it works:** When $T$ is popped, it means $X$ is the *first* element encountered to the right of $T$ that is larger than $T$. All elements between $T$ and $X$ were smaller than $T$, which is why $T$ was allowed to stay on top of them.

***

## II. Mathematical Concepts: Time Complexity

The major advantage of the Monotonic Stack is its time efficiency.

### Amortized $O(1)$ Operations (Total $O(N)$ Time)

The overall time complexity for processing an entire array of $N$ elements is $O(N)$. This is achieved through **Amortized Analysis**.

1.  **Iterating through the array:** Every element is processed exactly once (a total of $N$ operations).
2.  **Stack Operations:**
    * **Push:** Every element is pushed onto the stack exactly once. (Total $N$ pushes).
    * **Pop:** An element can be popped **at most once**. Once an element is popped, it is never reinserted. (Maximum $N$ pops).

$$\text{Total Cost} = \text{Cost}(\text{N iterations}) + \text{Cost}(\text{N pushes}) + \text{Cost}(\text{N pops})$$

$$\text{Total Cost} \approx O(N) + O(N \cdot 1) + O(N \cdot 1) = O(N)$$

**Simple Explanation (Non-Technical):** Even though the inner `while` loop, which performs the **pop** operations, *looks* like it could make the algorithm slow (because it might pop many elements at once), the total number of pops across the *entire* process can never be more than the total number of items in the array ($N$). Since every item is looked at once, pushed once, and popped at most once, the total effort is directly proportional to the size of the input array. This makes it a very efficient, linear-time algorithm.

***

## III. Relationships and Real-Life Example

### Relationships

* **Monotonic Stack** is a *variation* of the **Stack** (LIFO ADT).
* It leverages the **LIFO** property to define a nearest neighbor relationship. When an element is popped, the new element being pushed is the *first* element encountered that broke the order, which, due to LIFO, is the nearest element to the right (or left, depending on the traversal direction).
* The overall efficiency is analyzed using **Amortized Analysis**, ensuring the total process remains $O(N)$, similar to the analysis for dynamic arrays.

### Real-Life Technical Example: Stock Market Analysis

Consider an application that analyzes stock price data for optimal trading. A common task is to find the **first day (to the right) where the stock price was higher** than the current day's price. This is exactly the **Next Greater Element (NGE)** problem.

**Scenario (Monotonically Decreasing Stack for NGE):**

| Day | Stock Price ($)|
| :--- | :--- |
| D1 | 8 |
| D2 | 6 |
| D3 | 7 |
| D4 | 9 |

1.  **Day D1 (Price 8):** Stack is empty. **Push 8**. Stack: [8]
2.  **Day D2 (Price 6):** $6 < 8$. No violation. **Push 6**. Stack: [8, 6]
3.  **Day D3 (Price 7):** $7 > 6$. **Violation!**
    * **Pop 6**. The NGE for 6 is 7. (D3 is the first day after D2 with a higher price).
    * Now, $7 < 8$. No violation. **Push 7**. Stack: [8, 7]
4.  **Day D4 (Price 9):** $9 > 7$. **Violation!**
    * **Pop 7**. The NGE for 7 is 9.
    * $9 > 8$. **Violation!**
    * **Pop 8**. The NGE for 8 is 9.
    * Stack is empty. **Push 9**. Stack: [9]

The Monotonic Stack technique efficiently processed the entire price series in one pass, instantly finding the next higher price for optimal trading decisions.

***

## IV. Definitions

| Term | Definition | Simple Explanation (Non-Technical) |
| :--- | :--- | :--- |
| **Monotonic Stack**| A stack that maintains its elements in a strict order (always increasing or always decreasing) from bottom to top. | A pile where the numbers must be sorted from the lowest to the highest, or vice versa. |
| **Monotonically Increasing** | A sequence where each subsequent element is greater than or equal to the previous element. | The numbers are always getting bigger (or staying the same). |
| **Monotonically Decreasing** | A sequence where each subsequent element is less than or equal to the previous element. | The numbers are always getting smaller (or staying the same). |
| **Next Greater Element (NGE)**| The first element to the right (or left, depending on context) of a given element that has a strictly greater value. | The very next number in the list that is bigger than the current number. |
| **Next Smaller Element (NSE)**| The first element to the right (or left) of a given element that has a strictly smaller value. | The very next number in the list that is smaller than the current number. |
