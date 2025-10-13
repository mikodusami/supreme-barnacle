"""
Binary Search Study Guide and Code Template

This file serves as a comprehensive resource for mastering the Binary Search algorithm,
including core implementations, common interview patterns, and auxiliary utilities.
Binary search is an O(log N) search algorithm that works on sorted data.
"""

from typing import List, TypeVar, Any, Callable, Optional, Tuple

# Type variable for generics (e.g., int, float)
T = TypeVar('T')

# =============================================================================
# I. Core Implementation & Theory (The Foundation)
# =============================================================================

class BinarySearchCore:
    """
    Core implementation of Binary Search.
    The primary challenge is managing the search space (left, right boundaries).
    Three main templates: standard, lower_bound, and upper_bound.
    """

    @staticmethod
    def standard_search(arr: List[T], target: T) -> int:
        """
        Template 1: Standard Binary Search (Exact Match).
        Finds the index of an exact 'target' value.

        Search Space: [left, right] (inclusive bounds)
        Condition: The list must be sorted (ascending).

        Args:
            arr: A sorted list of elements.
            target: The value to search for.

        Returns:
            int: The index of the target if found, otherwise -1.

        Time Complexity: O(log N) - Reduces search space by half in each step.
        Space Complexity: O(1) - Only a few auxiliary variables (l, r, mid).
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            # Use 'mid = left + (right - left) // 2' to prevent potential integer overflow
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                # Target is in the right half: [mid + 1, right]
                left = mid + 1
            else: # arr[mid] > target
                # Target is in the left half: [left, mid - 1]
                right = mid - 1

        return -1

    @staticmethod
    def lower_bound(arr: List[T], target: T) -> int:
        """
        Template 2: Lower Bound Binary Search (First Occurrence / Insertion Point).
        Finds the index of the *first element* that is greater than or equal to 'target'.
        This is useful for finding the first occurrence in a list with duplicates
        or the correct insertion point to maintain sorted order.

        Search Space: [left, right] (inclusive bounds)
        Final Answer: 'left' pointer holds the result.

        Args:
            arr: A sorted list of elements.
            target: The value to find the lower bound for.

        Returns:
            int: The index of the first element >= target. Returns len(arr) if all elements are less than target.

        Time Complexity: O(log N)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        ans = len(arr) # Default if all elements are less than target

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] >= target:
                # Potential answer found. Try to find an even smaller index.
                ans = mid
                right = mid - 1
            else: # arr[mid] < target
                # Target must be in the right half.
                left = mid + 1

        # The 'left' pointer (which is equivalent to 'ans' here) is the correct insertion point.
        return left

    @staticmethod
    def upper_bound(arr: List[T], target: T) -> int:
        """
        Template 3: Upper Bound Binary Search (Last Occurrence + 1 / Next Element).
        Finds the index of the *first element* that is strictly greater than 'target'.
        This is useful for finding the last occurrence of a value (index - 1).

        Search Space: [left, right] (inclusive bounds)
        Final Answer: 'left' pointer holds the result.

        Args:
            arr: A sorted list of elements.
            target: The value to find the upper bound for.

        Returns:
            int: The index of the first element > target. Returns len(arr) if all elements are less than or equal to target.

        Time Complexity: O(log N)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        ans = len(arr) # Default if all elements are <= target

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] > target:
                # Potential answer found. Try to find an even smaller index.
                ans = mid
                right = mid - 1
            else: # arr[mid] <= target
                # Target must be in the right half.
                left = mid + 1

        # The 'left' pointer (which is equivalent to 'ans' here) is the correct upper bound.
        return left

# =============================================================================
# II. BinarySearchTemplates Class (Interview Snippets)
# =============================================================================

class BinarySearchTemplates:
    """
    A collection of function templates representing common interview problems
    and patterns that utilize or extend Binary Search.
    """

    @staticmethod
    def t01_search_rotated_sorted_array(nums: List[int], target: int) -> int:
        """
        Template for searching in a sorted array that has been rotated.
        Requires determining which side (left or right) is sorted to proceed.
        Time: O(log N), Space: O(1).
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted: nums[left] <= nums[mid]
            if nums[left] <= nums[mid]:
                # Target is in the left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # The right half must be sorted
            else:
                # Target is in the right sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    @staticmethod
    def t02_find_minimum_in_rotated_sorted_array(nums: List[int]) -> int:
        """
        Template for finding the minimum element in a rotated sorted array.
        The minimum element is the only one where its next element is larger,
        or it's the element that breaks the sorted property of the sub-array.
        Time: O(log N), Space: O(1).
        """
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left] # Not rotated or only 1 element

        while left < right:
            mid = left + (right - left) // 2
            # If mid is greater than right, min is in the right unsorted side
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid is less than or equal to right, min is in the left side (including mid)
            else:
                right = mid # Cannot be mid + 1 because mid could be the minimum

        return nums[left] # left == right is the minimum index

    @staticmethod
    def t03_search_in_unknown_size_array(reader: Any, target: int) -> int:
        """
        Template for searching in a sorted array where size is unknown (provided by an API/Reader).
        Requires an initial exponential search to find the search boundaries [left, right].
        Time: O(log N), Space: O(1).
        """
        # 1. Exponential search to find the bounds
        left, right = 0, 1
        # while reader.get(right) < target: # Assuming get() returns a sentinel for out-of-bounds
        while reader.get(right) < target: # Placeholder for real reader check
            left = right
            right *= 2

        # 2. Standard Binary Search within the known bounds [left, right]
        while left <= right:
            mid = left + (right - left) // 2
            val = reader.get(mid) # Placeholder for real reader check

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def t04_first_bad_version(n: int, is_bad: Callable[[int], bool]) -> int:
        """
        Template for finding the first 'bad' version (a standard lower_bound problem).
        The search space is integers from 1 to n.
        Time: O(log N), Space: O(1).
        """
        left, right = 1, n
        first_bad = n # Default if n is the only bad version

        while left <= right:
            mid = left + (right - left) // 2
            if is_bad(mid):
                # mid is a bad version, try to find an earlier bad version
                first_bad = mid
                right = mid - 1
            else:
                # mid is a good version, the first bad must be later
                left = mid + 1

        return first_bad

    @staticmethod
    def t05_find_peak_element(nums: List[int]) -> int:
        """
        Template for finding a peak element (an element greater than its neighbors) in an array.
        This is a modified binary search because the property of being "greater"
        allows us to discard one half safely, guaranteeing a peak remains.
        Time: O(log N), Space: O(1).
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # Check the slope
            if nums[mid] < nums[mid + 1]:
                # We are on the increasing slope, a peak must be to the right
                left = mid + 1
            else: # nums[mid] > nums[mid + 1] (or equal, though usually constraints ensure no equality)
                # We are on the decreasing slope, mid could be the peak, or the peak is to the left
                right = mid # Cannot be mid - 1 because mid could be the answer

        return left # left == right is the peak index

    @staticmethod
    def t06_square_root_integer(x: int) -> int:
        """
        Template for computing the integer square root (x^2 <= target).
        This is a standard binary search on the *result space* [0, x].
        Time: O(log X), Space: O(1).
        """
        if x < 2: return x
        left, right = 1, x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                # Potential answer, try for a larger one
                ans = mid
                left = mid + 1
            else:
                # Too large, search lower
                right = mid - 1
        return ans

    @staticmethod
    def t07_find_duplicate_number(nums: List[int]) -> int:
        """
        Template for finding the duplicate number in an array of size n+1 (numbers 1 to n).
        Uses Binary Search on the *value space* [1, n], not the index space.
        Condition check: count of numbers <= 'mid' is <= 'mid'.
        Time: O(N log N), Space: O(1).
        """
        n = len(nums) - 1 # Max possible value
        left, right = 1, n
        duplicate = -1

        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                # The duplicate must be in [left, mid]
                duplicate = mid
                right = mid - 1
            else:
                # The duplicate must be in [mid + 1, right]
                left = mid + 1

        return duplicate

    @staticmethod
    def t08_min_size_subarray_sum(nums: List[int], s: int) -> int:
        """
        Template for finding the minimum length of a contiguous subarray whose sum is at least 's'.
        Uses Binary Search on the *result space* [1, N] for the length.
        The check function is O(N) (or O(N log N) if not optimized).
        Time: O(N log N), Space: O(1).
        """
        def check(length: int) -> bool:
            """Checks if a subarray of 'length' exists with sum >= s."""
            current_sum = sum(nums[:length])
            if current_sum >= s: return True
            for i in range(length, len(nums)):
                current_sum += nums[i] - nums[i - length] # Sliding window
                if current_sum >= s: return True
            return False

        left, right = 1, len(nums)
        min_length = 0

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                # Possible answer, try smaller length
                min_length = mid
                right = mid - 1
            else:
                # Length is too small, need larger length
                left = mid + 1

        return min_length

    @staticmethod
    def t09_split_array_largest_sum(nums: List[int], k: int) -> int:
        """
        Template for minimizing the largest sum among 'k' subarrays after splitting the array.
        Uses Binary Search on the *result space* [max(nums), sum(nums)].
        Condition check: Can the array be split into 'k' or fewer subarrays, each with max sum <= 'mid'?
        Time: O(N log(Sum)), Space: O(1).
        """
        low = max(nums)
        high = sum(nums)
        min_max_sum = high

        def count_splits(max_sum: int) -> int:
            """Counts the minimum number of subarrays required if the max allowed sum is 'max_sum'."""
            splits = 1
            current_sum = 0
            for num in nums:
                if current_sum + num <= max_sum:
                    current_sum += num
                else:
                    splits += 1
                    current_sum = num
            return splits

        while low <= high:
            mid = low + (high - low) // 2
            num_splits = count_splits(mid)

            if num_splits <= k:
                # Possible answer, try smaller max sum
                min_max_sum = mid
                high = mid - 1
            else:
                # Max sum is too small, need a larger max sum
                low = mid + 1

        return min_max_sum

    @staticmethod
    def t10_binary_search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
        """
        Template for searching in a 2D matrix where each row is sorted, and the first
        element of each row is greater than the last element of the previous row.
        Treats the 2D array as a single sorted 1D array of size R*C.
        Time: O(log(R*C)), Space: O(1).
        """
        if not matrix or not matrix[0]: return False
        R, C = len(matrix), len(matrix[0])
        left, right = 0, R * C - 1

        while left <= right:
            mid = left + (right - left) // 2
            # Convert 1D index (mid) to 2D indices (r, c)
            r = mid // C
            c = mid % C
            mid_val = matrix[r][c]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    @staticmethod
    def t11_search_range(nums: List[int], target: int) -> List[int]:
        """
        Template for finding the starting and ending position of a given target value.
        Uses two applications of a modified binary search (or lower_bound/upper_bound).
        Time: O(log N), Space: O(1).
        """
        # Helper to find the leftmost index of the target
        def find_first_occurrence(arr: List[int], target: int) -> int:
            left, right = 0, len(arr) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] >= target:
                    if arr[mid] == target: ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        # Helper to find the index *after* the last occurrence
        def find_upper_bound(arr: List[int], target: int) -> int:
            left, right = 0, len(arr) - 1
            ans = len(arr)
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] > target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        start = find_first_occurrence(nums, target)
        if start == -1:
            return [-1, -1]
        
        # The index of the last element is the upper bound index minus 1
        end = find_upper_bound(nums, target) - 1
        
        return [start, end]

    @staticmethod
    def t12_kth_smallest_in_multiplication_table(m: int, n: int, k: int) -> int:
        """
        Template for finding the K-th smallest element in an m x n multiplication table.
        Uses Binary Search on the *result space* [1, m * n].
        Condition check: Count how many numbers in the table are less than or equal to 'mid'.
        Time: O(log(M*N) * (M+N)), Space: O(1).
        """
        def count_le_mid(mid: int) -> int:
            """Counts elements <= mid in the table."""
            count = 0
            for i in range(1, m + 1):
                # The number of multiples of 'i' that are <= mid is min(n, mid // i)
                count += min(n, mid // i)
            return count

        low, high = 1, m * n
        kth_smallest = high

        while low <= high:
            mid = low + (high - low) // 2
            if count_le_mid(mid) >= k:
                # mid is a possible answer, try smaller
                kth_smallest = mid
                high = mid - 1
            else:
                # Too few elements <= mid, search higher
                low = mid + 1
        return kth_smallest

    @staticmethod
    def t13_median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
        """
        Template for finding the median of two sorted arrays.
        Uses Binary Search on the *smaller array's index space* to find the optimal partition.
        This is a complex application often solved with the Partition Search approach.
        Time: O(log(min(N, M))), Space: O(1).
        """
        N1, N2 = len(nums1), len(nums2)
        # Ensure nums1 is the smaller array to minimize search space
        if N1 > N2:
            return BinarySearchTemplates.t13_median_of_two_sorted_arrays(nums2, nums1)

        low, high = 0, N1
        half_len = (N1 + N2 + 1) // 2

        while low <= high:
            # i is the cut position in nums1, j is the cut position in nums2
            i = low + (high - low) // 2
            j = half_len - i

            # Get the boundary elements for the left and right halves
            max_left1 = nums1[i - 1] if i > 0 else float('-inf')
            min_right1 = nums1[i] if i < N1 else float('inf')

            max_left2 = nums2[j - 1] if j > 0 else float('-inf')
            min_right2 = nums2[j] if j < N2 else float('inf')

            # Check for the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Correct partition found
                if (N1 + N2) % 2 == 1:
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            elif max_left1 > min_right2:
                # The cut in nums1 is too far right (max_left1 is too big)
                high = i - 1
            else: # max_left2 > min_right1
                # The cut in nums1 is too far left (max_left1 is too small)
                low = i + 1

        # Should never reach here for valid input
        return 0.0

    @staticmethod
    def t14_find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
        """
        Template for finding the 'k' closest elements to 'x' in a sorted array.
        Uses Binary Search to find the starting index of the window of size 'k'.
        The search space is the possible starting indices: [0, len(arr) - k].
        Time: O(log N + K), Space: O(1).
        """
        # Search space for the starting index 'i' of the k-size window [i, i + k - 1]
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = left + (right - left) // 2
            
            # The condition compares the element *just outside the left* edge of the window (arr[mid])
            # with the element *just outside the right* edge of the window (arr[mid + k])
            # The goal is to choose the window that is closer to x.
            
            # Compare distance: |x - arr[mid]| vs |x - arr[mid + k]|
            if x - arr[mid] > arr[mid + k] - x:
                # arr[mid] is further away from x than arr[mid + k], so shift window right
                left = mid + 1
            else:
                # arr[mid + k] is further away or equidistant (prefer smaller index), so shift window left
                right = mid

        return arr[left:left + k]

    @staticmethod
    def t15_find_pivot_index(nums: List[int]) -> int:
        """
        Template for finding the pivot index (an index where the sum of numbers
        to its left equals the sum of numbers to its right).
        While not strictly binary search, it's often framed as an optimized search.
        Prefix sums are used to make the O(N) check O(1).
        Time: O(N), Space: O(1) or O(N) for prefix sum array.
        """
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Check if left_sum == right_sum
            # right_sum = total_sum - left_sum - num
            # Check if left_sum == total_sum - left_sum - num
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
            
        return -1


# =============================================================================
# III. BinarySearchMentalToolBox Class (Auxiliary Functions)
# =============================================================================

class BinarySearchMentalToolBox:
    """
    A collection of auxiliary and utility functions for Binary Search,
    useful for generating test cases and validating the core search logic.
    """

    @staticmethod
    def tbx01_generate_sorted_test_case(size: int = 20, min_val: int = 1, max_val: int = 100, allow_duplicates: bool = True) -> List[int]:
        """
        Generates a sorted list of integers, suitable for Binary Search testing.
        """
        import random
        if allow_duplicates:
            arr = sorted([random.randint(min_val, max_val) for _ in range(size)])
        else:
            arr = sorted(list(set(random.randint(min_val, max_val) for _ in range(size))))
            # If the set size is too small, pad it.
            while len(arr) < size:
                arr.append(arr[-1] + 1 if arr else random.randint(min_val, max_val))
            arr = sorted(arr[:size])
        return arr

    @staticmethod
    def tbx02_find_correct_index_linear(arr: List[T], target: T) -> int:
        """
        Linear search validation (O(N)) for exact match to verify Binary Search results.
        Returns the index of the first occurrence.
        """
        try:
            return arr.index(target)
        except ValueError:
            return -1

    @staticmethod
    def tbx03_find_lower_bound_linear(arr: List[T], target: T) -> int:
        """
        Linear validation (O(N)) for the lower bound definition:
        index of the first element >= target.
        """
        for i, val in enumerate(arr):
            if val >= target:
                return i
        return len(arr)

    @staticmethod
    def tbx04_find_upper_bound_linear(arr: List[T], target: T) -> int:
        """
        Linear validation (O(N)) for the upper bound definition:
        index of the first element > target.
        """
        for i, val in enumerate(arr):
            if val > target:
                return i
        return len(arr)

    @staticmethod
    def tbx05_generate_rotated_test_case(size: int = 15) -> List[int]:
        """
        Generates a sorted, then rotated, list for testing t01 and t02.
        """
        import random
        base_arr = BinarySearchMentalToolBox.tbx01_generate_sorted_test_case(size, allow_duplicates=False)
        if not base_arr: return []
        pivot = random.randint(1, size - 1)
        rotated_arr = base_arr[pivot:] + base_arr[:pivot]
        return rotated_arr

    @staticmethod
    def tbx06_is_array_rotated_sorted(arr: List[int]) -> bool:
        """
        Checks if an array is a valid sorted and rotated array (O(N)).
        Counts the number of "disruption points" where arr[i] > arr[i+1].
        Must have exactly one disruption point (or zero if not rotated).
        """
        if not arr: return True
        disruptions = 0
        n = len(arr)
        for i in range(n):
            if arr[i] > arr[(i + 1) % n]:
                disruptions += 1
        return disruptions <= 1

    @staticmethod
    def tbx07_run_all_core_tests(arr: List[int], target: int) -> Tuple[int, int, int]:
        """
        Runs all three core BS templates and returns their results.
        """
        standard_idx = BinarySearchCore.standard_search(arr, target)
        lower_idx = BinarySearchCore.lower_bound(arr, target)
        upper_idx = BinarySearchCore.upper_bound(arr, target)
        return standard_idx, lower_idx, upper_idx

    @staticmethod
    def tbx08_reader_api_stub(arr: List[int]) -> Any:
        """
        Stub for the 'unknown size array' reader API (for t03).
        """
        class Reader:
            def get(self, index: int) -> int:
                if 0 <= index < len(arr):
                    return arr[index]
                # Return a value that signifies out-of-bounds but is also guaranteed to be > target
                return 2147483647 # Max possible int

        return Reader()

    @staticmethod
    def tbx09_get_last_occurrence(arr: List[T], target: T) -> int:
        """
        Finds the index of the *last element* equal to 'target'.
        Derived from upper_bound: index = upper_bound(target) - 1.
        """
        upper = BinarySearchCore.upper_bound(arr, target)
        if upper == 0 or arr[upper - 1] != target:
            return -1
        return upper - 1

    @staticmethod
    def tbx10_is_bad_version_stub(bad_version: int) -> Callable[[int], bool]:
        """
        Stub for the 'is_bad' function required by t04.
        """
        return lambda version: version >= bad_version

if __name__ == '__main__':
    # =========================================================================
    # Example Usage and Testing
    # =========================================================================
    
    # I. Core Implementation Test
    test_array = [2, 5, 5, 5, 8, 12, 12, 15]
    target_val = 5
    
    # Standard Search
    std_res = BinarySearchCore.standard_search(test_array, target_val) # Expected: 1 (or any index of 5)
    # Lower Bound
    lb_res = BinarySearchCore.lower_bound(test_array, target_val) # Expected: 1 (Index of first 5)
    # Upper Bound
    ub_res = BinarySearchCore.upper_bound(test_array, target_val) # Expected: 4 (Index of 8, first element > 5)
    
    # print(f"Array: {test_array}, Target: {target_val}")
    # print(f"Standard Search Index: {std_res}")
    # print(f"Lower Bound Index: {lb_res} (Element: {test_array[lb_res] if lb_res < len(test_array) else 'N/A'})")
    # print(f"Upper Bound Index: {ub_res} (Element: {test_array[ub_res] if ub_res < len(test_array) else 'N/A'})")

    # II. Interview Template Test (Rotated Array)
    rotated_arr = [4, 5, 6, 7, 0, 1, 2]
    # min_val = BinarySearchTemplates.t02_find_minimum_in_rotated_sorted_array(rotated_arr) # Expected: 0
    # search_res = BinarySearchTemplates.t01_search_rotated_sorted_array(rotated_arr, 1) # Expected: 5
    # print(f"\nMin in Rotated: {min_val}, Search '1' Index: {search_res}")
    
    # III. Mental ToolBox Test
    # ran_arr = BinarySearchMentalToolBox.tbx01_generate_sorted_test_case(size=10, allow_duplicates=True)
    # ran_target = ran_arr[4] if ran_arr else 0
    # print(f"\nRandom Array: {ran_arr}, Target: {ran_target}")
    # print(f"Linear LB Check: {BinarySearchMentalToolBox.tbx03_find_lower_bound_linear(ran_arr, ran_target)}")
    # print(f"Binary LB Check: {BinarySearchCore.lower_bound(ran_arr, ran_target)}")
    pass