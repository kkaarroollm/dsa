### Sorting Algorithms – Study Notes

#### 📌 General idea of Sorting:

Sorting algorithms rearrange elements into ascending (or descending) order. Efficiency and optimal use depend on the input size and structure.

---

### 1️⃣ Selection Sort

* **How it works:**

  * Repeatedly find the smallest (or largest) element from the unsorted part and put it at the beginning.

* **Complexity:**

  * Best, Average, Worst-case: **O(n²)**

* **Performance:**

  * Input doesn't significantly affect performance; always quadratic.
  * Good for small arrays; poor performance on large datasets.

* **Linked Lists:**

  * Inefficient (frequent traversal needed).

* **Stability:**

  * Not stable (can change order of identical elements).

---

### 2️⃣ Insertion Sort

* **How it works:**

  * Builds sorted array incrementally, inserting each element into its correct position.

* **Complexity:**

  * Best-case: **O(n)** (already sorted)
  * Average/Worst-case: **O(n²)**

* **Performance:**

  * Excellent for nearly-sorted or small datasets.
  * Slow for large, randomly ordered datasets.

* **Linked Lists:**

  * Efficient (constant insertion time).

* **Stability:**

  * Stable (preserves order of identical elements).

---

### 3️⃣ Merge Sort

* **How it works:**

  * Divide and conquer: split list into halves, recursively sort, then merge sorted halves.

* **Complexity:**

  * Best, Average, Worst-case: **O(n log n)**

* **Merge Function:**

  * Key part: efficiently combines sorted sequences.

* **Performance:**

  * Consistently efficient for all inputs.

* **Linked Lists:**

  * Very efficient (ideal for lists due to easy merging).

* **Stability:**

  * Stable (order of identical elements preserved).

---

### 4️⃣ Quicksort

* **How it works:**

  * Select pivot, partition array around pivot, recursively sort partitions.

* **Complexity:**

  * Best/Average-case: **O(n log n)**
  * Worst-case: **O(n²)** (poor pivot choice)

* **Partition Function:**

  * Critical step: rearranging around the pivot.

* **Performance:**

  * Fastest for typical random data.
  * Slowest for sorted or reverse-sorted data (bad pivot choices).

* **Linked Lists:**

  * Inefficient due to partitioning.

* **Stability:**

  * Not stable (partitioning can rearrange identical elements).

---

### 5️⃣ Counting Sort

* **How it works:**

  * Counts occurrences of each value; calculates positions based on cumulative count.

* **Complexity:**

  * Best, Average, Worst-case: **O(n + k)**, k - range of input values

* **Performance:**

  * Optimal when range (k) isn't significantly greater than n.

* **Linked Lists:**

  * Generally impractical due to the counting step.

* **Stability:**

  * Stable if implemented carefully (counts positionally).

---

### 6️⃣ Radix Sort

* **How it works:**

  * Sorts numbers digit-by-digit, from least significant to most significant.

* **Complexity:**

  * Best, Average, Worst-case: \**O(d*(n + k))\*\*, d - number of digits, k - digit range

* **Performance:**

  * Excellent for sorting integers, strings, fixed-length data.

* **Linked Lists:**

  * Can be implemented effectively with linked lists.

* **Stability:**

  * Stable (preserves order across digit-based sorting).

---

### 📌 Algorithm Comparison:

| Algorithm      | Avg. Complexity | Best Data                 | Worst Data            | Stability | Linked List Efficiency |
| -------------- | --------------- | ------------------------- | --------------------- | --------- | ---------------------- |
| Selection Sort | O(n²)           | Small arrays              | Large arrays          | ❌         | Poor                   |
| Insertion Sort | O(n²)           | Nearly sorted             | Reverse/random        | ✅         | Good                   |
| Merge Sort     | O(n log n)      | General-purpose sorting   | Always efficient      | ✅         | Excellent              |
| Quicksort      | O(n log n)      | Random data               | Sorted/reverse sorted | ❌         | Poor                   |
| Counting Sort  | O(n + k)        | Small range of values     | Large range           | ✅         | Poor                   |
| Radix Sort     | O(d\*(n + k))   | Fixed-length numeric data | Large range of digits | ✅         | Good                   |

---

### 📌 Stability:

* **Stable algorithms:** Insertion, Merge, Counting (carefully implemented), Radix
* **Not Stable:** Selection, Quicksort

**Why stability matters:**

* Important when sorting by multiple criteria (e.g., first by name, then by age).

---

### 📌 Mathematical Lower Limit for Sorting by Comparisons:

* No comparison-based sorting algorithm can do better than **O(n log n)** in the worst-case.
* Derived using decision-tree argument: sorting n elements requires log(n!) comparisons ≈ **n log n**.


---

Sorting Algorithms Comprehensive Notes

1. Algorithm Overviews:
	•	Selection Sort:
	•	Complexity: O(n²) always
	•	Idea: Select smallest/largest element and move to correct position.
	•	Stability: Unstable (swaps non-adjacent elements)
	•	Suitable for small data sets, not efficient on large ones.
	•	Performs poorly on large lists; consistent but slow.
	•	Insertion Sort:
	•	Complexity: O(n²) average/worst; O(n) best-case (sorted list)
	•	Idea: Insert element into the correct sorted position.
	•	Stability: Stable (only moves elements to right)
	•	Efficient on small or nearly sorted data sets.
	•	Good performance with linked lists (easy insertion).
	•	Merge Sort:
	•	Complexity: O(n log n) always
	•	Idea: Divide, recursively sort, merge sorted halves.
	•	Stability: Stable (maintains order during merging)
	•	Suitable for large data sets.
	•	Excellent with linked lists (no random access needed).
	•	QuickSort:
	•	Complexity: Average O(n log n), Worst-case O(n²)
	•	Idea: Partition around pivot; recursively sort partitions.
	•	Stability: Unstable (partition swaps elements unpredictably)
	•	Efficient for large, random data; poor with already sorted or reverse-sorted data.
	•	Poor performance with linked lists (partitioning difficult).
	•	Counting Sort:
	•	Complexity: O(n + k) (k = range of input)
	•	Idea: Count occurrences; cumulative sums; reorder accordingly.
	•	Stability: Stable (preserves original relative order)
	•	Efficient when data range (k) is not significantly larger than input size (n).
	•	Only integers or discrete values; ineffective if range is large.
	•	Radix Sort:
	•	Complexity: O(nk) (k = number of digits/characters in max element)
	•	Idea: Sort elements digit by digit from least significant to most significant.
	•	Stability: Stable (maintains original relative order)
	•	Efficient with fixed-length numbers/strings.
	•	Best for data with uniform length.

⸻

2. Pairwise Comparison:
	•	Selection vs. Insertion:
	•	Insertion better with nearly sorted/small data; selection always quadratic.
	•	Selection vs. Merge:
	•	Merge better for larger datasets (O(n log n)); selection slower.
	•	Selection vs. QuickSort:
	•	QuickSort usually faster, except worst-case; selection always slow.
	•	Insertion vs. Merge:
	•	Merge for large datasets; insertion quicker for small or nearly sorted data.
	•	Insertion vs. QuickSort:
	•	QuickSort faster on average; insertion better for nearly sorted/small.
	•	Merge vs. QuickSort:
	•	Merge guarantees O(n log n); QuickSort often faster practically but O(n²) worst-case.
	•	Counting vs. Radix:
	•	Counting ideal for small range; Radix handles larger numeric ranges better.
	•	Counting/Radix vs. Comparison-based:
	•	Counting/Radix faster for integers within limited ranges, otherwise impractical.

⸻

3. Stability:
	•	Stable Algorithms:
	•	Insertion Sort, Merge Sort, Counting Sort, Radix Sort
	•	Unstable Algorithms:
	•	Selection Sort, QuickSort

Stability is important when sorting records based on multiple criteria.

⸻

4. Linked List Performance:
	•	Good: Insertion Sort, Merge Sort (excellent for linked lists)
	•	Poor: QuickSort, Selection Sort, Counting and Radix (require random access)

⸻

5. Mathematical Lower Limit for Comparison-Based Sorting:
	•	Theoretical limit: O(n log n)
	•	Proven by decision-tree model for comparison-based sorting algorithms
	•	Algorithms like Merge Sort or Heap Sort meet this bound.
	•	Non-comparison-based sorts (Counting, Radix) can surpass this limit.
