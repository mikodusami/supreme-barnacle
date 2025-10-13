"""
Hashing Study Guide and Code Template (Hash Table / Dictionary)

This file serves as a comprehensive resource for mastering Hashing, focusing on the
core Hash Table data structure and related interview concepts.
"""

from typing import Any, List, Optional, TypeVar, Generic, Tuple, Callable

# Type variables for key and value
K = TypeVar('K')
V = TypeVar('V')

# =============================================================================
# I. Core Implementation & Theory (The Foundation)
# =============================================================================

class HashMapChaining(Generic[K, V]):
    """
    Core implementation of a Hash Table using Separate Chaining for collision resolution.
    Each slot in the array (bucket) stores a linked list (or standard Python list) of key-value pairs.

    Core Concepts:
    - Hash Function: Converts a key into an index (bucket address).
    - Compression Function: Maps the hash value to an index within the table size.
    - Load Factor (alpha): N / M, where N is the number of items and M is the number of buckets.
      When alpha exceeds a threshold (e.g., 0.75), resizing (rehashing) is typically performed.

    Core Operations and Complexities (Average Case / Worst Case):
    - put(key, value): Insert or update a key-value pair.
        Time Complexity: O(1) / O(N) (Worst case when all keys map to the same bucket)
        Space Complexity: O(N)
    - get(key): Retrieve the value associated with the key.
        Time Complexity: O(1) / O(N)
        Space Complexity: O(1)
    - delete(key): Remove the key-value pair.
        Time Complexity: O(1) / O(N)
        Space Complexity: O(1)
    """
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity: int = DEFAULT_CAPACITY):
        """Initializes the hash map with a fixed number of buckets."""
        self._capacity = capacity
        # Buckets is a list of lists, where each inner list stores (key, value) tuples
        self._buckets: List[List[Tuple[K, V]]] = [[] for _ in range(capacity)]
        self._size = 0
        self.LOAD_THRESHOLD = 0.75

    def _hash(self, key: K) -> int:
        """
        Custom Hash and Compression Function.
        Uses Python's built-in hash() for distribution, then applies modulo for compression.
        """
        return hash(key) % self._capacity

    def _resize(self) -> None:
        """
        Doubles the capacity and rehashes all existing items.
        Time Complexity: O(N + M_new) where N is items, M_new is new capacity.
        """
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0 # Size will be rebuilt by put calls

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value) # Use existing put method for rehashing

    def put(self, key: K, value: V) -> None:
        """
        Inserts or updates a key-value pair.

        Time Complexity: O(1) Avg., O(N) Worst
        Space Complexity: O(1) Avg., O(N) Worst (during resize)
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        # Check if key already exists (update)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Key does not exist (insert)
        bucket.append((key, value))
        self._size += 1

        # Check load factor and resize if necessary
        if self._size / self._capacity > self.LOAD_THRESHOLD:
            self._resize()

    def get(self, key: K) -> Optional[V]:
        """
        Retrieves the value associated with the key.

        Time Complexity: O(1) Avg., O(N) Worst
        Space Complexity: O(1)
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None # Key not found

    def delete(self, key: K) -> bool:
        """
        Removes the key-value pair.

        Returns:
            bool: True if key was deleted, False if key not found.

        Time Complexity: O(1) Avg., O(N) Worst
        Space Complexity: O(1)
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True

        return False

    def contains(self, key: K) -> bool:
        """Checks if the key exists."""
        return self.get(key) is not None

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        items = []
        for bucket in self._buckets:
            for key, val in bucket:
                items.append(f"{key}: {val}")
        return f"{{ {', '.join(items)} }}"


# Note: Open Addressing (e.g., Linear Probing, Quadratic Probing, Double Hashing)
# is another fundamental implementation but is more complex to implement cleanly
# without sentinel tombstone values and is less common in Python's standard library.
# The `HashMapChaining` serves as the primary core template.

# =============================================================================
# II. HashingTemplates Class (Interview Snippets)
# =============================================================================

class HashingTemplates:
    """
    A collection of function templates representing common interview problems
    and patterns that utilize Hash Maps (dictionaries in Python) and Sets.
    """

    @staticmethod
    def t01_two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        """
        Template for the Two Sum problem. Uses a hash map to store 'complement' needed.
        Map: {complement_needed: index_of_first_number}.
        Time: O(N), Space: O(N).
        """
        seen = {} # {number: index}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None

    @staticmethod
    def t02_valid_anagram(s: str, t: str) -> bool:
        """
        Template for checking if two strings are anagrams. Uses two hash maps (or a single counter map).
        Time: O(N), Space: O(1) (since the alphabet size is constant, 26).
        """
        if len(s) != len(t): return False
        char_counts = {} # {char: count}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        for char in t:
            count = char_counts.get(char)
            if count is None or count <= 0:
                return False
            char_counts[char] -= 1
        # Optional: Check if all counts are zero, but the checks above usually suffice.
        return True

    @staticmethod
    def t03_longest_consecutive_sequence(nums: List[int]) -> int:
        """
        Template for finding the length of the longest consecutive elements sequence.
        Uses a set for O(1) lookups to optimize the search process.
        Time: O(N), Space: O(N).
        """
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            # Check if 'num' is the start of a sequence (i.e., num - 1 is NOT in the set)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length

    @staticmethod
    def t04_group_anagrams(strs: List[str]) -> List[List[str]]:
        """
        Template for grouping anagrams together. Uses the sorted string (canonical form) as the hash key.
        Time: O(N * K log K) where N is list size, K is max string length (due to sorting).
        Space: O(N * K) to store the result.
        """
        groups = {} # {canonical_form (tuple/str): list_of_anagrams}
        for s in strs:
            # Canonical form: a tuple of sorted characters (immutable, hashable)
            key = tuple(sorted(s))
            groups.setdefault(key, []).append(s)
        return list(groups.values())

    @staticmethod
    def t05_top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
        """
        Template for finding the k most frequent elements.
        Uses a hash map for frequency counting, followed by a sorting or bucket/heap method.
        Time: O(N + M log M) where M is the number of distinct elements, or O(N) using bucket sort.
        Space: O(N).
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Using sorting on the dictionary items
        # items = list(counts.items()) # list of (num, count)
        # items.sort(key=lambda item: item[1], reverse=True)
        # return [item[0] for item in items[:k]]

        # Better: Using Bucket Sort (O(N) overall complexity)
        # Buckets are indexed by frequency (0 to N)
        freq_buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq_buckets[count].append(num)

        result = []
        # Iterate buckets from highest frequency to lowest
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

    @staticmethod
    def t06_contains_duplicate_ii(nums: List[int], k: int) -> bool:
        """
        Template for finding a duplicate where the two indices i and j satisfy |i - j| <= k.
        Uses a hash map to store the last seen index of each number.
        Time: O(N), Space: O(N).
        """
        seen_indices = {} # {number: last_seen_index}
        for i, num in enumerate(nums):
            if num in seen_indices and i - seen_indices[num] <= k:
                return True
            seen_indices[num] = i
        return False

    @staticmethod
    def t07_isomorphic_strings(s: str, t: str) -> bool:
        """
        Template for checking if two strings are isomorphic (one-to-one character mapping).
        Requires two maps (or a set) to ensure the mapping is bidirectional.
        Time: O(N), Space: O(1) (since the alphabet size is constant).
        """
        if len(s) != len(t): return False
        s_to_t = {} # char in s -> char in t
        t_to_s = {} # char in t -> char in s (reverse map)

        for char_s, char_t in zip(s, t):
            # Check forward mapping
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Check reverse mapping (ensuring char_t hasn't already mapped to a DIFFERENT char_s)
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True

    @staticmethod
    def t08_subarray_sum_equals_k(nums: List[int], k: int) -> int:
        """
        Template for finding the total number of continuous subarrays whose sum equals k.
        Uses a hash map to store prefix sums and their frequencies.
        Map: {prefix_sum: frequency}.
        Time: O(N), Space: O(N).
        """
        prefix_sums = {0: 1} # Stores {prefix_sum: count of times that sum has occurred}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            # We are looking for a previous sum 'P' such that:
            # current_sum - P = k  =>  P = current_sum - k
            complement = current_sum - k
            if complement in prefix_sums:
                count += prefix_sums[complement]

            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count

    @staticmethod
    def t09_find_all_duplicates_in_array(nums: List[int]) -> List[int]:
        """
        Template for finding all duplicates in an array where 1 <= a[i] <= n.
        A clever O(N) space-optimized solution uses the array itself as a hash table
        by marking indices with negative signs.
        Time: O(N), Space: O(1) (excluding result list).
        """
        duplicates = []
        for num in nums:
            # The number corresponding to the index to check
            index_to_check = abs(num) - 1
            if nums[index_to_check] < 0:
                # Already seen (marked negative), so it's a duplicate
                duplicates.append(abs(num))
            else:
                # Mark as seen by flipping the sign at that index
                nums[index_to_check] *= -1
        return duplicates

    @staticmethod
    def t10_intersection_of_two_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Template for finding the intersection of two arrays (unique elements only).
        Uses a set for O(1) lookup of elements in the first array.
        Time: O(N + M), Space: O(min(N, M)).
        """
        set1 = set(nums1)
        intersection_set = set()
        for num in nums2:
            if num in set1:
                intersection_set.add(num)
        return list(intersection_set)

    @staticmethod
    def t11_majority_element(nums: List[int]) -> int:
        """
        Template for finding the element that appears more than n/2 times.
        Boyer-Moore Voting Algorithm (O(N) time, O(1) space) is preferred, but
        the hash map solution is also standard and simple.
        Time: O(N), Space: O(N).
        """
        counts = {}
        threshold = len(nums) // 2
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > threshold:
                return num
        return -1 # Should not happen with guaranteed input

    @staticmethod
    def t12_word_pattern(pattern: str, s: str) -> bool:
        """
        Template for checking if a string 's' follows the 'pattern' (full match with one-to-one mapping).
        This is similar to t07_isomorphic_strings but with words instead of characters.
        Time: O(N + M), Space: O(N + M).
        """
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        p_to_w = {} # pattern char -> word
        w_to_p = {} # word -> pattern char

        for p_char, word in zip(pattern, words):
            # Check pattern-to-word map
            if p_char in p_to_w:
                if p_to_w[p_char] != word: return False
            # Check word-to-pattern map
            elif word in w_to_p:
                if w_to_p[word] != p_char: return False
            else:
                # Create a new, unique mapping
                p_to_w[p_char] = word
                w_to_p[word] = p_char
        return True

    @staticmethod
    def t13_ransom_note(ransom_note: str, magazine: str) -> bool:
        """
        Template for checking if a ransom note can be constructed from a magazine (character availability).
        Uses a hash map to count character frequencies in the magazine.
        Time: O(N + M), Space: O(1) (size of alphabet is constant).
        """
        magazine_counts = {}
        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1

        for char in ransom_note:
            count = magazine_counts.get(char)
            if count is None or count <= 0:
                return False
            magazine_counts[char] -= 1
        return True

    @staticmethod
    def t14_longest_substring_without_repeating_characters(s: str) -> int:
        """
        Template for finding the longest substring without repeating characters.
        Uses a hash map in a Sliding Window approach to store {char: last_seen_index}.
        Time: O(N), Space: O(min(N, |Alphabet|)).
        """
        seen_chars = {} # {char: index}
        max_len = 0
        left = 0 # Left boundary of the sliding window

        for right, char in enumerate(s):
            if char in seen_chars and seen_chars[char] >= left:
                # Repetition found: move the left boundary past the last seen index of the repeated character
                left = seen_chars[char] + 1

            # Update the last seen index of the current character
            seen_chars[char] = right
            # Update the max length (current window size is right - left + 1)
            max_len = max(max_len, right - left + 1)

        return max_len

    @staticmethod
    def t15_lru_cache_design(capacity: int, operations: List[Tuple[str, Any]]) -> List[Any]:
        """
        Template for designing an LRU Cache. Requires combining a Hash Map (for O(1) access)
        and a Doubly Linked List (for O(1) reordering by usage).
        Time: O(1) for both get and put. Space: O(Capacity).
        """
        # Inner class to simulate the LRUCache structure
        class Node:
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.prev = None
                self.next = None

        class LRUCache:
            def __init__(self, capacity: int):
                self.capacity = capacity
                self.map = {} # {key: Node}
                # Use dummy head/tail nodes to simplify edge cases
                self.head = Node(0, 0)
                self.tail = Node(0, 0)
                self.head.next = self.tail
                self.tail.prev = self.head

            def _remove_node(self, node: Node):
                node.prev.next = node.next
                node.next.prev = node.prev

            def _add_to_head(self, node: Node):
                node.next = self.head.next
                node.prev = self.head
                self.head.next.prev = node
                self.head.next = node

            def get(self, key: int) -> int:
                if key in self.map:
                    node = self.map[key]
                    self._remove_node(node)
                    self._add_to_head(node) # Move to front (Most Recently Used)
                    return node.val
                return -1

            def put(self, key: int, value: int) -> None:
                if key in self.map:
                    node = self.map[key]
                    node.val = value # Update value
                    self._remove_node(node)
                    self._add_to_head(node) # Move to front
                else:
                    new_node = Node(key, value)
                    self.map[key] = new_node
                    self._add_to_head(new_node)
                    if len(self.map) > self.capacity:
                        # Evict the Least Recently Used (node before tail)
                        lru_node = self.tail.prev
                        self._remove_node(lru_node)
                        del self.map[lru_node.key]

        # Execution logic for template
        cache = LRUCache(capacity)
        results = []
        for op, args in operations:
            if op == 'put':
                key, val = args
                cache.put(key, val)
                results.append(None)
            elif op == 'get':
                key = args
                results.append(cache.get(key))
        return results

# =============================================================================
# III. HashingMentalToolBox Class (Auxiliary Functions)
# =============================================================================

class HashingMentalToolBox:
    """
    A collection of auxiliary and utility functions for Hashing,
    useful for testing, debugging, and understanding hash behavior.
    """

    @staticmethod
    def tbx01_test_collision_rate(keys: List[Any], capacity: int = 10) -> Tuple[int, float]:
        """
        Calculates the number of collisions (number of keys that map to an occupied bucket
        after the first element) and the average chain length for a given set of keys.
        """
        hash_func: Callable[[Any], int] = lambda k: hash(k) % capacity
        bucket_counts = [0] * capacity
        collisions = 0
        
        for key in keys:
            index = hash_func(key)
            if bucket_counts[index] > 0:
                collisions += 1
            bucket_counts[index] += 1

        num_chains = sum(1 for count in bucket_counts if count > 0)
        avg_chain_length = len(keys) / num_chains if num_chains > 0 else 0
        
        return collisions, avg_chain_length

    @staticmethod
    def tbx02_generate_unique_keys(n: int) -> List[int]:
        """Generates a list of N unique integer keys."""
        import random
        return random.sample(range(1, 100000), n)

    @staticmethod
    def tbx03_generate_random_pairs(n: int) -> List[Tuple[int, int]]:
        """Generates a list of N random (key, value) integer pairs."""
        import random
        return [(random.randint(1, 1000), random.randint(1, 10000)) for _ in range(n)]

    @staticmethod
    def tbx04_check_map_equality(map1: HashMapChaining, map2: HashMapChaining) -> bool:
        """
        Checks if two custom HashMapChaining instances are logically equal (same size and contents).
        Note: This is an O(N^2) comparison for the worst case, but O(N) average.
        """
        if map1.size() != map2.size():
            return False

        for bucket in map1._buckets:
            for key, val in bucket:
                if map2.get(key) != val:
                    return False
        return True

    @staticmethod
    def tbx05_visualize_chaining(hash_map: HashMapChaining) -> None:
        """
        Prints a visualization of the hash map's buckets and chains.
        """
        print(f"--- Hash Map Visualization (Size: {hash_map.size()}, Capacity: {hash_map._capacity}) ---")
        for i, bucket in enumerate(hash_map._buckets):
            chain_str = ""
            if bucket:
                chain_str = " -> ".join([f"({k}:{v})" for k, v in bucket])
            else:
                chain_str = "Empty"
            print(f"Bucket {i:02d}: {chain_str}")
        print("-" * 50)

    @staticmethod
    def tbx06_count_word_frequency(text: str) -> dict[str, int]:
        """
        Counts the frequency of each word in a given text (standard utility).
        """
        import re
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    @staticmethod
    def tbx07_longest_contiguous_subarray_template(nums: List[int], condition_fn: Callable[[dict[int, int]], bool]) -> int:
        """
        Template for Sliding Window problems where the window condition is tracked via a hash map.
        Example conditions: max distinct elements, max count of one element, etc.
        Returns the max length of the subarray satisfying the condition.
        Time: O(N), Space: O(N).
        """
        counts = {}
        max_len = 0
        left = 0
        for right, num in enumerate(nums):
            counts[num] = counts.get(num, 0) + 1
            
            # Shrink the window until the condition is met
            while not condition_fn(counts):
                left_num = nums[left]
                counts[left_num] -= 1
                if counts[left_num] == 0:
                    del counts[left_num]
                left += 1
                
            max_len = max(max_len, right - left + 1)
        return max_len

    @staticmethod
    def tbx08_rolling_hash_rabin_karp(text: str, pattern: str, prime: int = 101) -> List[int]:
        """
        Utility for String Matching: Rabin-Karp Algorithm using a Rolling Hash.
        Finds all starting indices where 'pattern' occurs in 'text'.
        Time: O(N + M) Avg., O(N * M) Worst (due to spurious hits). Space: O(1).
        """
        N, M = len(text), len(pattern)
        if M > N: return []
        
        d = 256 # Number of characters in the alphabet
        h = pow(d, M - 1, prime) # d^(M-1) % prime
        p_hash = 0 # Hash of pattern
        t_hash = 0 # Hash of text window
        results = []

        # Calculate initial hash for pattern and first text window
        for i in range(M):
            p_hash = (d * p_hash + ord(pattern[i])) % prime
            t_hash = (d * t_hash + ord(text[i])) % prime

        # Slide the window
        for i in range(N - M + 1):
            if p_hash == t_hash:
                # Potential match: check for spurious hit
                if text[i:i + M] == pattern:
                    results.append(i)

            # Recalculate hash for the next window: Rolling Hash
            if i < N - M:
                t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + M])) % prime
                if t_hash < 0: # Ensure positive hash value
                    t_hash += prime

        return results

    @staticmethod
    def tbx09_double_hashing_index(key: K, capacity: int, i: int, h1: Callable[[K], int], h2: Callable[[K], int]) -> int:
        """
        A function to illustrate Double Hashing probe sequence (Open Addressing).
        Index = (h1(key) + i * h2(key)) % capacity
        """
        # Simplistic h1 and h2 functions for illustration
        hash_val = hash(key)
        h1_val = hash_val % capacity
        h2_val = 1 + (hash_val % (capacity - 2)) # Ensures result is non-zero and relatively prime to capacity
        
        return (h1_val + i * h2_val) % capacity

    @staticmethod
    def tbx10_calculate_load_factor(hash_map: HashMapChaining) -> float:
        """Calculates the current load factor of the hash map."""
        if hash_map._capacity == 0:
            return 0.0
        return hash_map.size() / hash_map._capacity

if __name__ == '__main__':
    # =========================================================================
    # Example Usage and Testing
    # =========================================================================

    # I. Core Implementation Test (HashMapChaining)
    hm = HashMapChaining[str, int](capacity=3) # Small capacity to force resizing/collisions
    hm.put("apple", 1)
    hm.put("banana", 2)
    hm.put("cherry", 3)
    # print(str(hm))
    # print(f"Load Factor: {HashingMentalToolBox.tbx10_calculate_load_factor(hm):.2f}")
    # HashingMentalToolBox.tbx05_visualize_chaining(hm)
    hm.put("date", 4) # This might trigger a resize if capacity was 3 and threshold 0.75
    # print(f"\nAfter resize (date=4):")
    # print(str(hm))

    # II. Interview Template Test (Longest Substring Without Repeating Characters)
    s_test = "abcabcbb"
    # max_len = HashingTemplates.t14_longest_substring_without_repeating_characters(s_test) # Expected: 3
    # print(f"\nLongest Substring for '{s_test}': {max_len}")

    # III. Mental ToolBox Test (Collision Rate)
    # keys_to_test = [1, 11, 21, 31, 2, 12] # Should mostly collide in capacity=10
    # collisions, avg_chain_len = HashingMentalToolBox.tbx01_test_collision_rate(keys_to_test, capacity=10)
    # print(f"\nCollision Test (Keys={keys_to_test}): Collisions={collisions}, Avg Chain Length={avg_chain_len:.2f}")

    # Double Hashing Probe Sequence example
    # probe_1 = HashingMentalToolBox.tbx09_double_hashing_index(10, 7, 0, None, None) # Probe 0
    # probe_2 = HashingMentalToolBox.tbx09_double_hashing_index(10, 7, 1, None, None) # Probe 1
    # print(f"Double Hashing (Key 10, Cap 7): Probe 0 Index={probe_1}, Probe 1 Index={probe_2}")

    pass