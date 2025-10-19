"""
Sliding Window Study Guide and Code Template

This file serves as a comprehensive resource for mastering the Sliding Window technique,
which is primarily used on arrays, lists, or strings to efficiently process contiguous subarrays/substrings.
"""

from typing import List, TypeVar, Any, Dict, Callable, Optional
from collections import defaultdict

# Type variable for element values
T = TypeVar('T')

# =============================================================================
# I. Core Implementation & Theory (The Foundation)
# =============================================================================

class SlidingWindowCore:
    """
    The Sliding Window is a technique that reduces the time complexity of certain problems
    from O(N^2) or O(N^3) down to O(N). It works by maintaining a 'window' (a subarray/substring)
    and iteratively moving the window's right boundary (expansion) and occasionally
    the left boundary (contraction).

    Two Main Templates:
    1. Fixed Size Window: The window size 'k' is constant. O(N) complexity.
       - Use: Maximum sum subarray of size k.
    2. Dynamic Size Window: The window size varies based on a condition. O(N) complexity.
       - Use: Longest/shortest subarray satisfying a condition (e.g., max distinct chars).

    Time Complexity for most problems: O(N)
    Space Complexity: O(1) or O(Alphabet Size) or O(N) depending on auxiliary data structure (e.g., hash map).
    """

    @staticmethod
    def fixed_size_template(arr: List[int], k: int) -> Any:
        """
        Template 1: Fixed Size Window (for problems like max subarray sum of size k).

        Process:
        1. Initialize the window by calculating the sum/metric for the first 'k' elements.
        2. Slide the window one step at a time, maintaining the window size:
           - Add the new element (arr[right]).
           - Remove the element leaving the window (arr[left]).
           - Update the result metric.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        n = len(arr)
        if n < k:
            return None # Or handle error/edge case

        # 1. Initialize the first window
        current_metric = sum(arr[:k])  # e.g., sum, count, etc.
        max_metric = current_metric    # e.g., max_sum, max_count, etc.

        # 2. Slide the window (right starts at k, left at 0)
        for right in range(k, n):
            # Expansion: Include the new element (arr[right])
            current_metric += arr[right]

            # Contraction: Exclude the element leaving the window (arr[right - k])
            current_metric -= arr[right - k]

            # Update the result
            max_metric = max(max_metric, current_metric)

        return max_metric

    @staticmethod
    def dynamic_size_shortest_window_template(arr: List[Any], condition_fn: Callable[[Dict[Any, int]], bool]) -> int:
        """
        Template 2a: Dynamic Window - Finding the *shortest* subarray satisfying a condition.
        (e.g., minimum size subarray sum >= S, shortest substring containing all characters of P).

        Process:
        1. Expand the window (right++) until the condition is MET.
        2. Contract the window (left++) until the condition is BROKEN.
        3. Record the length of the valid window just before contraction.

        Time Complexity: O(N) (Each pointer moves forward at most N times).
        Space Complexity: O(N) or O(Alphabet Size) for the frequency map.
        """
        left = 0
        min_length = float('inf')
        # Auxiliary structure to track window state (e.g., frequencies, sum, count)
        window_state = defaultdict(int)

        for right in range(len(arr)):
            # 1. EXPAND the window and update the state
            element_r = arr[right]
            window_state[element_r] += 1
            # Add element_r to sum/count/etc.

            # 2. CONTRACT the window while the condition is MET
            # This ensures we find the minimal valid window starting at the current 'right'
            while condition_fn(window_state):
                # Update the result: current window [left, right] is a valid solution
                min_length = min(min_length, right - left + 1)

                # Contraction: Remove element at 'left' and update the state
                element_l = arr[left]
                window_state[element_l] -= 1
                if window_state[element_l] == 0:
                    del window_state[element_l]
                # Subtract element_l from sum/count/etc.

                left += 1

        return min_length if min_length != float('inf') else 0

    @staticmethod
    def dynamic_size_longest_window_template(arr: List[Any], condition_fn: Callable[[Dict[Any, int]], bool]) -> int:
        """
        Template 2b: Dynamic Window - Finding the *longest* subarray satisfying a condition.
        (e.g., longest substring without repeating characters, longest subarray with max K distinct chars).

        Process:
        1. Expand the window (right++) and update the state.
        2. If the condition is BROKEN, contract the window (left++) until the condition is MET again.
        3. Record the maximum length of the window [left, right] at the end of each iteration.

        Time Complexity: O(N)
        Space Complexity: O(N) or O(Alphabet Size) for the frequency map.
        """
        left = 0
        max_length = 0
        # Auxiliary structure to track window state (e.g., frequencies, distinct count)
        window_state = defaultdict(int)

        for right in range(len(arr)):
            # 1. EXPAND the window and update the state
            element_r = arr[right]
            window_state[element_r] += 1
            # Add element_r to sum/count/etc.

            # 2. CONTRACT the window while the condition is BROKEN
            while not condition_fn(window_state):
                # Contraction: Remove element at 'left' and update the state
                element_l = arr[left]
                window_state[element_l] -= 1
                if window_state[element_l] == 0:
                    del window_state[element_l]
                # Subtract element_l from sum/count/etc.

                left += 1

            # 3. Update the result: The window [left, right] is now guaranteed to be valid
            # (and is the longest possible valid window ending at 'right').
            max_length = max(max_length, right - left + 1)

        return max_length

# =============================================================================
# II. SlidingWindowTemplates Class (Interview Snippets)
# =============================================================================

class SlidingWindowTemplates:
    """
    A collection of function templates representing common interview problems
    and patterns solved using the Sliding Window technique.
    """

    @staticmethod
    def t01_max_consecutive_sum(arr: List[int], k: int) -> int:
        """
        Fixed Size Window: Find the maximum sum subarray of size k.
        Time: O(N), Space: O(1).
        """
        return SlidingWindowCore.fixed_size_template(arr, k)

    @staticmethod
    def t02_longest_substring_non_repeating(s: str) -> int:
        """
        Dynamic Window (Longest): Longest substring without repeating characters.
        The condition is: len(window_state) == window_size.
        Time: O(N), Space: O(Alphabet Size).
        """
        seen_chars = {}  # {char: last_seen_index}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in seen_chars and seen_chars[char] >= left:
                # Repetition found: contract window by moving 'left' past the repeated character
                left = seen_chars[char] + 1

            # Update the last seen index
            seen_chars[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len

    @staticmethod
    def t03_min_subarray_sum(nums: List[int], target: int) -> int:
        """
        Dynamic Window (Shortest): Minimum size subarray whose sum is greater than or equal to 'target'.
        The condition is: current_sum >= target.
        Time: O(N), Space: O(1).
        """
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            # Contract while condition is MET
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

    @staticmethod
    def t04_longest_substring_k_distinct(s: str, k: int) -> int:
        """
        Dynamic Window (Longest): Longest substring with at most k distinct characters.
        The condition is: len(window_state) <= k.
        Time: O(N), Space: O(Alphabet Size).
        """
        counts = defaultdict(int)
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            counts[char] += 1

            # Contract while condition is BROKEN (i.e., too many distinct characters)
            while len(counts) > k:
                left_char = s[left]
                counts[left_char] -= 1
                if counts[left_char] == 0:
                    del counts[left_char]
                left += 1

            # Update the result
            max_len = max(max_len, right - left + 1)

        return max_len

    @staticmethod
    def t05_check_permutation_in_string(s1: str, s2: str) -> bool:
        """
        Fixed Size Window (with permutation check): Check if s2 contains a permutation of s1.
        Uses two frequency maps (or arrays) and checks for equality.
        Time: O(N_s2), Space: O(Alphabet Size).
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        # Frequency map/array for s1 (pattern) and the current window in s2
        s1_counts = defaultdict(int)
        window_counts = defaultdict(int)
        for char in s1:
            s1_counts[char] += 1

        def check_match(c1: Dict[str, int], c2: Dict[str, int]) -> bool:
            return c1 == c2

        # 1. Initialize the first window
        for i in range(n1):
            window_counts[s2[i]] += 1

        # 2. Check and Slide
        if check_match(s1_counts, window_counts):
            return True

        for right in range(n1, n2):
            # Expansion
            window_counts[s2[right]] += 1
            # Contraction
            left_char = s2[right - n1]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                del window_counts[left_char]

            if check_match(s1_counts, window_counts):
                return True

        return False

    @staticmethod
    def t06_longest_repeating_char_replacement(s: str, k: int) -> int:
        """
        Dynamic Window (Longest): Longest substring where all characters are the same after
        at most k replacements. Condition: (window_size - max_freq) <= k.
        Time: O(N), Space: O(Alphabet Size).
        """
        counts = defaultdict(int)
        left = 0
        max_len = 0
        max_freq = 0 # Max frequency of any character in the current window

        for right, char in enumerate(s):
            counts[char] += 1
            max_freq = max(max_freq, counts[char])

            window_size = right - left + 1
            # Contract while condition is BROKEN (replacements needed > k)
            while window_size - max_freq > k:
                left_char = s[left]
                counts[left_char] -= 1
                # max_freq doesn't necessarily need to be updated on contraction,
                # only on expansion, as the max will either remain or decrease, but
                # if it decreases, the window size has also decreased, and the invariant
                # check (window_size - max_freq <= k) still holds true for the current max_freq.
                left += 1
                window_size = right - left + 1 # Recalculate size

            # The current window is valid
            max_len = max(max_len, window_size)

        return max_len

    @staticmethod
    def t07_min_window_substring(s: str, t: str) -> str:
        """
        Dynamic Window (Shortest): Smallest substring in S that contains all characters of T.
        Uses two frequency maps and a 'formed' counter for the complex condition check.
        Time: O(N + M), Space: O(Alphabet Size).
        """
        if not t or not s: return ""

        target_counts = defaultdict(int)
        for char in t:
            target_counts[char] += 1
        required = len(target_counts) # Number of unique chars needed

        window_counts = defaultdict(int)
        formed = 0 # Number of unique characters in the window that match target_counts
        left = 0
        min_length = float('inf')
        result_start, result_end = 0, 0

        for right, char in enumerate(s):
            window_counts[char] += 1

            # Check if this character helps satisfy the required condition
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Contract while condition is MET (formed == required)
            while left <= right and formed == required:
                # Update the result: current window is valid
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    result_start = left
                    result_end = right

                # Contraction: Remove element at 'left'
                left_char = s[left]

                # Check if removing this char breaks the required condition
                if left_char in target_counts and window_counts[left_char] == target_counts[left_char]:
                    formed -= 1

                window_counts[left_char] -= 1
                left += 1

        return s[result_start:result_end + 1] if min_length != float('inf') else ""

    @staticmethod
    def t08_max_vowels_in_substring(s: str, k: int) -> int:
        """
        Fixed Size Window: Maximum number of vowels in any substring of length k.
        Time: O(N), Space: O(1).
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def is_vowel(char: str) -> int:
            return 1 if char in vowels else 0

        n = len(s)
        if n < k: return 0

        # 1. Initialize the first window count
        current_vowels = sum(is_vowel(s[i]) for i in range(k))
        max_vowels = current_vowels

        # 2. Slide the window
        for right in range(k, n):
            # Add new element's contribution
            current_vowels += is_vowel(s[right])
            # Subtract old element's contribution
            current_vowels -= is_vowel(s[right - k])
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels

    @staticmethod
    def t09_number_of_subarrays_with_product_less_than_k(nums: List[int], k: int) -> int:
        """
        Dynamic Window (Counting): Count subarrays whose product is less than k.
        For every valid window [left, right], all subarrays ending at 'right' are valid.
        (The number of such subarrays is 'right - left + 1').
        Time: O(N), Space: O(1).
        """
        if k <= 1: return 0

        product = 1
        count = 0
        left = 0

        for right, num in enumerate(nums):
            product *= num

            # Contract while condition is BROKEN (product >= k)
            while product >= k:
                product /= nums[left]
                left += 1

            # Update the count: All subarrays ending at 'right' are valid:
            # [right], [right-1, right], ..., [left, ..., right]
            # The number of such subarrays is (right - left + 1)
            count += (right - left + 1)

        return count

    @staticmethod
    def t10_longest_subarray_after_deleting_one_element(nums: List[int]) -> int:
        """
        Dynamic Window (Variation): Find the longest subarray of 1s after deleting one element.
        Equivalent to finding the longest subarray with at most one 0 (k=1).
        Time: O(N), Space: O(1).
        """
        k = 1  # Max number of zeros allowed
        left = 0
        zeros = 0
        max_len = 0 # The result is max_len - 1 (since one element must be deleted)

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1

            # Contract while condition is BROKEN (too many zeros)
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update max length of the valid window [left, right]
            max_len = max(max_len, right - left + 1)

        # The actual result is the length of the max valid window - 1 (for the deleted element)
        return max_len - 1

    @staticmethod
    def t11_max_consecutive_ones_iii(nums: List[int], k: int) -> int:
        """
        Dynamic Window (Longest): Find the maximum length of a contiguous subarray of 1s
        after flipping at most k zeros to ones.
        Condition: The number of zeros in the window must be <= k.
        Time: O(N), Space: O(1).
        """
        left = 0
        zeros = 0
        max_len = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1

            # Contract while condition is BROKEN (too many zeros)
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len

    @staticmethod
    def t12_fruits_into_baskets(fruits: List[int]) -> int:
        """
        Dynamic Window (Longest): Find the maximum number of fruits you can collect (total length)
        such that the chosen subarray contains at most two distinct types of fruit (k=2).
        This is equivalent to t04_longest_substring_k_distinct with k=2.
        Time: O(N), Space: O(1) (max 2 distinct fruit types in the map).
        """
        k = 2
        counts = defaultdict(int)
        left = 0
        max_len = 0

        for right, fruit_type in enumerate(fruits):
            counts[fruit_type] += 1

            # Contract while condition is BROKEN (more than k distinct types)
            while len(counts) > k:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

    @staticmethod
    def t13_sliding_window_median(nums: List[int], k: int) -> List[float]:
        """
        Fixed Size Window (Advanced): Calculate the median of the sliding window of size k.
        This problem is generally solved using a Heap-based approach (Two Heaps)
        or a Balanced BST (Multiset/Treap) to keep track of the median in O(log k) time per slide.
        The sliding window framework dictates the O(N) outer loop.
        Time: O(N log K), Space: O(K).
        """
        results = []
        # In a real implementation, you'd use a data structure (e.g., Two Heaps)
        # to maintain the sorted order and median in O(log k).
        
        # Placeholder for the O(N * k log k) naive solution for template completion
        for i in range(len(nums) - k + 1):
            window = sorted(nums[i:i + k])
            if k % 2 == 1:
                median = float(window[k // 2])
            else:
                median = (window[k // 2 - 1] + window[k // 2]) / 2.0
            results.append(median)
        
        return results

    @staticmethod
    def t14_longest_substring_with_at_most_two_distinct_characters(s: str) -> int:
        """
        Dynamic Window (Longest): Exactly the same as t12_fruits_into_baskets (k=2).
        Emphasizes the pattern's reusability across different problem descriptions.
        Time: O(N), Space: O(1).
        """
        k = 2
        counts = defaultdict(int)
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            counts[char] += 1

            while len(counts) > k:
                left_char = s[left]
                counts[left_char] -= 1
                if counts[left_char] == 0:
                    del counts[left_char]
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len


    @staticmethod
    def t15_find_all_anagrams_in_string(s: str, p: str) -> List[int]:
        """
        Fixed Size Window (with hash comparison): Find all start indices of p's anagrams in s.
        This is identical to t05_check_permutation_in_string, but we collect all starting indices.
        Time: O(N_s), Space: O(Alphabet Size).
        """
        n, m = len(s), len(p)
        if m > n: return []

        p_counts = defaultdict(int)
        s_counts = defaultdict(int)
        for char in p:
            p_counts[char] += 1

        # Helper function for matching (can be optimized to check only 26 elements)
        def check_match():
            return p_counts == s_counts

        results = []

        # 1. Initialize the first window
        for i in range(m):
            s_counts[s[i]] += 1

        # 2. Check and Slide
        if check_match():
            results.append(0)

        for right in range(m, n):
            # Expansion
            s_counts[s[right]] += 1
            # Contraction
            left_char = s[right - m]
            s_counts[left_char] -= 1
            if s_counts[left_char] == 0:
                del s_counts[left_char]

            if check_match():
                results.append(right - m + 1)

        return results

# =============================================================================
# III. SlidingWindowMentalToolBox Class (Auxiliary Functions)
# =============================================================================

class SlidingWindowMentalToolBox:
    """
    A collection of auxiliary and utility functions for Sliding Window problems,
    useful for test case generation and result validation.
    """

    @staticmethod
    def tbx01_generate_random_array(size: int = 20, min_val: int = 1, max_val: int = 100) -> List[int]:
        """Generates a random integer array for testing sum/product problems."""
        import random
        return [random.randint(min_val, max_val) for _ in range(size)]

    @staticmethod
    def tbx02_generate_random_string(size: int = 30, alphabet: str = 'abcde') -> str:
        """Generates a random string for character-based problems."""
        import random
        return "".join(random.choice(alphabet) for _ in range(size))

    @staticmethod
    def tbx03_validate_max_sum_k_linear(arr: List[int], k: int) -> int:
        """
        Linear validation (O(N^2) or O(N) using the core template) for max sum of size k.
        (Using O(N) approach here as the optimal validation).
        """
        return SlidingWindowCore.fixed_size_template(arr, k)

    @staticmethod
    def tbx04_validate_min_sum_s_brute(nums: List[int], target: int) -> int:
        """
        Brute-force validation (O(N^2)) for the minimum size subarray sum >= target.
        """
        min_length = float('inf')
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break  # Break inner loop for minimal length starting at 'i'
        return min_length if min_length != float('inf') else 0

    @staticmethod
    def tbx05_validate_longest_distinct_brute(s: str) -> int:
        """
        Brute-force validation (O(N^3) or O(N^2)) for longest substring without repeating characters.
        """
        max_length = 0
        n = len(s)
        for i in range(n):
            seen_chars = set()
            for j in range(i, n):
                if s[j] in seen_chars:
                    break
                seen_chars.add(s[j])
                max_length = max(max_length, j - i + 1)
        return max_length

    @staticmethod
    def tbx06_get_frequency_map(s: str) -> Dict[str, int]:
        """Utility to quickly generate a character frequency map."""
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        return dict(counts)

    @staticmethod
    def tbx07_check_permutation(s1: str, s2: str) -> bool:
        """Utility to check if one string is a permutation of the other."""
        return SlidingWindowMentalToolBox.tbx06_get_frequency_map(s1) == \
               SlidingWindowMentalToolBox.tbx06_get_frequency_map(s2)

    @staticmethod
    def tbx08_is_window_valid(window: str, p_counts: Dict[str, int]) -> bool:
        """
        Utility to check if a window contains all required characters (for min_window_substring).
        Checks if the window's character count is >= the pattern's count for every char in the pattern.
        """
        window_counts = SlidingWindowMentalToolBox.tbx06_get_frequency_map(window)
        for char, count in p_counts.items():
            if window_counts.get(char, 0) < count:
                return False
        return True

    @staticmethod
    def tbx09_get_all_subarrays(nums: List[T]) -> List[List[T]]:
        """Utility to generate all contiguous subarrays (for comprehensive testing)."""
        subarrays = []
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                subarrays.append(nums[i:j+1])
        return subarrays

    @staticmethod
    def tbx10_calculate_max_distinct(window_state: Dict[Any, int]) -> int:
        """Helper for dynamic longest templates: returns the number of distinct elements."""
        return len(window_state)

if __name__ == '__main__':
    # =========================================================================
    # Example Usage and Testing
    # =========================================================================

    # I. Core Implementation Test (Fixed Size)
    arr_fixed = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k_fixed = 4
    # max_sum = SlidingWindowCore.fixed_size_template(arr_fixed, k_fixed) # Expected: 39 (10 + 23 + 3 + 1 + 0) or 39 (4, 2, 10, 23)
    # print(f"Max Sum Size {k_fixed}: {max_sum}")

    # II. Interview Template Test (Min Subarray Sum)
    nums_min_sum = [2, 3, 1, 2, 4, 3]
    target_min_sum = 7
    # min_len = SlidingWindowTemplates.t03_min_subarray_sum(nums_min_sum, target_min_sum) # Expected: 2 (4, 3)
    # print(f"Min Subarray Sum >= {target_min_sum} Length: {min_len}")

    # III. Interview Template Test (Longest Non-Repeating)
    s_non_rep = "pwwkew"
    # max_non_rep = SlidingWindowTemplates.t02_longest_substring_non_repeating(s_non_rep) # Expected: 3 (wke)
    # print(f"Longest Non-Repeating: {max_non_rep}")

    # IV. Mental ToolBox Validation
    # brute_val = SlidingWindowMentalToolBox.tbx05_validate_longest_distinct_brute(s_non_rep)
    # print(f"Brute Force Validation: {brute_val}")

    pass