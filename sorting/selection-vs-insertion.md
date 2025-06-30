### selection sort

> for each interation compares elements in unsorted part trying to find a min element


$$
S(n) = (n - 1) + (n - 2) + \ldots + 1 = \sum_{i=1}^{n-1} i
$$

$$
S(n) = \frac{(n - 1) \cdot n}{2}
$$

$$
\Rightarrow S(n) \in \Theta(n^2)
$$

### time complexity 
- worst: $\Theta(n^2)$
- best: $\Theta(n^2)$ ← *always does the same number of comparisons regardless of input order*


---
### insertion sort

> at each step, compares the current element with the sorted part and inserts it in the right place by shifting larger elements

$$
S(n) = 1 + 2 + \ldots + (n - 1) = \sum_{i=1}^{n-1} i
$$

$$
S(n) = \frac{(n - 1) \cdot n}{2}
$$

$$
\Rightarrow S(n) \in \Theta(n^2)
$$

### time complexity 
- worst: $\Theta(n^2)$ ← *eg. reverse-sorted input*
- best: $\Theta(n)$ ← *already sorted input; only one comparison per element*

