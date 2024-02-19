# Array & Hashing Takeaways

### 1. List vs. Dictionary
In Python, dictionary is faster than list. The average time complexity of a dictionary key lookup is O(1) since it is implemented as a hashtable, while that of a list is O(n) as it needs to iterate through all elements until the goal element. To avoid Time Limit Exceeded error, List should generally be avoided.

#### Reference
- 217-contains-duplicate

### 2. List vs. Tuple
While  tuples are immutable objects (static array), lists are mutable (dynamic array). This means that tuples cannot be changed whereas the lists can be modified. Tuples are more memory efficient than the lists.