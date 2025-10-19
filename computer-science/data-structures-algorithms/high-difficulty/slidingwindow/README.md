## Sliding Window 🪟

The **Sliding Window** technique is an algorithmic approach used to efficiently solve problems that involve finding a sub-section (like a sub-array, sub-string, or sub-list) within a larger, linear data structure. It works by maintaining a window of a certain size (or dynamic size) that "slides" over the data, processing the elements within the current window and minimizing redundant calculations.

***

## I. Core Concepts of Sliding Window

### What is a Sliding Window?

The Sliding Window is not a data structure itself, but rather a **computational pattern** that efficiently reduces the time complexity of certain problems from $O(N^2)$ to $O(N)$. It operates on linear data structures (like arrays or strings) by establishing a contiguous range of elements—the "window"—and moving this range across the data.

The core idea is to avoid re-calculating the properties of the entire sub-section every time the window moves one position. Instead, the calculation for the new window is derived from the old window by:

1.  **Removing** the element that slides out (the *left* edge).
2.  **Adding** the new element that slides in (the *right* edge).

**Simple Explanation (Non-Technical):** Imagine calculating the average temperature for every consecutive seven days in a year. Instead of re-adding seven new temperatures every day, you just subtract the temperature from the day that passed and add the temperature from the new day. This dramatically speeds up the process.

### Types of Sliding Windows

Sliding window problems typically fall into two categories:

1.  **Fixed-Size Window:** The window size ($K$) remains constant throughout the traversal.
    * *Example:* Finding the maximum sum of all sub-arrays of size 3.
2.  **Dynamic-Size Window:** The window size changes based on a specific condition being met. The right edge expands to include new elements, and the left edge contracts until the condition is satisfied.
    * *Example:* Finding the *longest* sub-string with no repeating characters.

***

## II. How Sliding Window Operations Work

A typical Sliding Window solution uses two pointers, $L$ (left) and $R$ (right), to define the boundaries of the current window $[L, R]$. The process is a single pass through the array.

### The Algorithm Flow (Dynamic Size Example)

This flow is typical for problems where you're looking for the shortest/longest sub-array that satisfies a condition.

1.  **Initialization:** Set $L=0$ and initialize a variable (like `current_sum`, `count`, or a **HashMap/Set**) to track the properties of the window.
2.  **Expansion (The Outer Loop):** The right pointer ($R$) moves forward one step at a time, incorporating a new element into the window. This typically happens in a main `for` or `while` loop that iterates $R$ from 0 to $N-1$.
3.  **Contraction (The Inner Loop):** After adding the $R$ element, an inner `while` loop checks if the **window condition** has been **violated** or if a desirable state is reached (e.g., sum is too large, or too many unique characters).
    * If the condition is violated, the left pointer ($L$) moves forward, shrinking the window and **removing** the element at $L$ from the current calculation, until the condition is valid again.
4.  **Result Update:** After each valid adjustment of the window (often after $R$ moves, but sometimes after $L$ moves), the maximum or minimum length/sum is updated.

### Time Complexity Analysis

The Sliding Window technique results in **linear time complexity, $O(N)$**.

$$\text{Time Complexity} = \text{O(N for Right Pointer)} + \text{O(N for Left Pointer)}$$

The key is that although the left pointer $L$ moves inside a loop that is controlled by the right pointer $R$, **neither pointer ever moves backward**. Since both $L$ and $R$ can traverse the array of $N$ elements at most once, the total number of operations is proportional to $N$.

**Simple Explanation (Non-Technical):** Since you only look at each element a maximum of twice (once when the right edge $R$ includes it, and possibly once when the left edge $L$ excludes it), the total time it takes to solve the problem is directly tied to the length of the array $N$. This is much faster than the $O(N^2)$ approach, which would involve two loops and re-checking every possible sub-array.

***

## III. Relationships and Real-Life Example

### Relationships

* **Sliding Window and HashMaps/Sets:** In dynamic window problems (like finding the longest sub-string without repeating characters), a **HashMap (Dictionary)** or **Set** is often used *inside* the window to efficiently track the frequency or presence of elements. This allows the $O(1)$ lookup speed of HashMaps/Sets to maintain the overall $O(N)$ speed of the windowing process.
* **Sliding Window and Prefix Sums:** For fixed-size window problems involving sums, the brute-force $O(N^2)$ solution is often improved by using the **Prefix Sum** technique, which also achieves $O(N)$. However, the Sliding Window is generally preferred for its simplicity and single pass when the sums are consecutive.

### Real-Life Technical Example: Data Stream Analysis

In modern systems that process continuous data streams (like stock market tickers or website traffic logs), the Sliding Window technique is used to monitor short-term trends.

**Scenario: Finding Hourly Request Spikes**

An API gateway needs to track the number of failed requests to detect potential Denial-of-Service (DoS) attacks. It applies a **fixed-size window** of one hour (e.g., 3600 data points, one for each second).

1.  **Initialization:** The window starts at $\text{Time } 0$ and spans to $\text{Time } 3600$. The total failure count in this window is calculated.
2.  **Sliding:** At $\text{Time } 1$, the window slides one second forward to span $[\text{Time } 1, \text{Time } 3601]$.
3.  **Efficiency:** Instead of re-summing 3600 data points:
    * The failure count from $\text{Time } 0$ is **subtracted** (the element that slides out).
    * The failure count from $\text{Time } 3601$ is **added** (the element that slides in).
4.  **Detection:** If the new total failure count exceeds a pre-set threshold, an alert is triggered.

This $O(N)$ sliding process allows the system to continuously monitor the massive stream of data in real-time without computational bottlenecks.

***

## IV. Definitions

| Term | Definition | Simple Explanation (Non-Technical) |
| :--- | :--- | :--- |
| **Sliding Window** | An algorithmic technique that uses a two-pointer approach to efficiently process a contiguous sub-section of linear data. | A method of scanning a list by moving a fixed or flexible-sized viewing box along it. |
| **$O(N)$** | **Linear Time Complexity**. The total time taken to solve the problem is directly proportional to the size ($N$) of the input data. | The time taken increases step-for-step with the size of the list; very fast. |
| **Left Pointer ($L$)** | The pointer that defines the starting boundary of the current window. It contracts the window. | The oldest item in the viewing box that is about to be removed. |
| **Right Pointer ($R$)** | The pointer that defines the ending boundary of the current window. It expands the window. | The newest item in the viewing box that was just added. |
| **Contiguous** | Elements that are adjacent or sequentially ordered in the original data structure. | Items that are right next to each other in the original list. |