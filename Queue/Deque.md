A **Double-Ended Queue** (also known as a **Deque**) is a more generalized form of a queue data structure. Unlike a normal queue, which follows a strict **FIFO (First In, First Out)** principle, a deque allows insertion and deletion of elements from both **ends**—the front and the rear.

### Key Characteristics of Deque:

1. **Insertion/Deletion from Both Ends:**

   - Elements can be added or removed from either the **front** or the **rear** of the deque.
2. **Flexible Operations:**

   - This flexibility allows a deque to function both as a **queue** (FIFO) and as a **stack** (LIFO - Last In, First Out).
3. **Two Types of Deques:**

   - **Input-Restricted Deque:** Insertion is restricted to one end (say rear), but deletion can be done from both ends.
   - **Output-Restricted Deque:** Deletion is restricted to one end (say front), but insertion can be done from both ends.

### Operations on Deque:

A deque supports the following operations on both the front and rear:

1. **Insertion at Front (`insertFront`)**: Adds an element at the front of the deque.
2. **Insertion at Rear (`insertRear`)**: Adds an element at the rear of the deque.
3. **Deletion from Front (`deleteFront`)**: Removes an element from the front of the deque.
4. **Deletion from Rear (`deleteRear`)**: Removes an element from the rear of the deque.
5. **Get Front (`getFront`)**: Returns the front element without removing it.
6. **Get Rear (`getRear`)**: Returns the rear element without removing it.
7. **IsEmpty**: Checks if the deque is empty.
8. **IsFull**: Checks if the deque is full (applicable for deques with fixed sizes).

### Visual Representation:

```
Initially:                    After Insertions:                   After Deletions:
[ _, _, _, _, _ ]              [ _, 10, 20, 30, _ ]                [ _, _, 20, 30, _ ]
   ↑    ↑                           ↑      ↑                           ↑     ↑
 Front Rear                     Front   Rear                       Front   Rear
```

### Variants:

1. **Input-Restricted Deque:**

   - Insertion is allowed at only one end (say rear), but deletion can occur from both ends.
2. **Output-Restricted Deque:**

   - Deletion is allowed from only one end (say front), but insertion can occur at both ends.

### Implementing a Deque:

Deques can be implemented using arrays or linked lists. Here’s a brief look at both:

1. **Array Implementation**:

   - A fixed-size array is used with two pointers (`front` and `rear`) to track the ends of the deque.
   - The pointers wrap around when they reach the array boundaries, just like in a circular queue.
   - This implementation requires care to handle underflow (deletion from an empty deque) and overflow (insertion into a full deque) conditions.
2. **Linked List Implementation**:

   - A doubly linked list can efficiently implement a deque since it allows constant-time insertions and deletions from both ends.
   - No need for wrapping around pointers like in the array-based implementation.

### Time Complexity of Operations:

- **Insertion/Deletion** at both ends is typically done in **O(1)** time in most implementations (using circular arrays or doubly linked lists).

### Applications of Deque:

- **Palindrome Checking:** A deque can be used to check if a word is a palindrome by comparing characters from both ends.
- **Sliding Window Problems:** Deques are useful in solving problems where a sliding window is used, such as finding the maximum or minimum in a range of array elements.
- **Job Scheduling:** Deques are often used in scheduling tasks where both priority jobs (inserted at the front) and normal jobs (inserted at the rear) are handled.
- **Undo/Redo Operations in Text Editors:** Deques can be used to keep track of undo and redo operations by adding new changes at one end and removing them from the other.

### Advantages of Deque:

1. **Versatility:** The ability to insert and delete from both ends makes deques more versatile than stacks and queues.
2. **Efficient Sliding Window Algorithms:** In some algorithms, deques provide a clean and efficient way to process a set of elements in a fixed window size.
3. **Optimal Performance:** Operations at both ends are performed in constant time, making it efficient for a wide range of use cases.

### Disadvantages:

1. **Fixed Size in Array Implementation:** In array-based deques, resizing is an issue if the deque reaches its maximum capacity.
2. **Memory Overhead in Linked List:** In linked-list-based deques, extra memory is required to store pointers for the next and previous nodes.

### Example Use Case: Sliding Window Maximum Problem

Given an array `arr[]` and a window size `k`, find the maximum of all subarrays of size `k`. The deque can store indexes of array elements, and it helps in sliding the window efficiently to get the maximum in constant time.

For instance, for the array `[1, 3, -1, -3, 5, 3, 6, 7]` with `k = 3`, using a deque allows finding the maximum of each window (i.e., `[3, 3, 5, 5, 6, 7]`) in O(n) time.

### Conclusion:

A **deque** is a highly flexible and efficient data structure with a wide range of applications. Its ability to perform operations at both ends makes it suitable for tasks where both queue and stack functionalities are required simultaneously.



### Operations in a Deque (Double-Ended Queue)

To fully understand the deque operations, let’s explore the basic operations with detailed steps and required conditions for each operation.

### 1. **Insertion at Front (`insertFront`)**

Inserts an element at the front of the deque.

#### Algorithm:

1. **Check if the deque is full**:
   - If the deque is full (i.e., `(front == 0 && rear == size - 1)` or `(front == rear + 1)`), the insertion cannot be performed.
2. **If the deque is empty**:
   - Set both `front` and `rear` to `0` (initializing the deque).
3. **If `front` is at the first position of the array** (i.e., `front == 0`):
   - Set `front = size - 1` (wrap around to the last index).
4. **Otherwise**, decrement the `front` pointer by 1.
5. **Insert** the new element at `front`.

#### Conditions:

- **IsFull:** `(front == 0 && rear == size - 1)` or `(front == rear + 1)`
- **IsEmpty:** `front == -1`

#### Pseudocode:

```pseudo
insertFront(deque, element):
    if (deque is full):
        return "Overflow"
  
    if (deque is empty):
        front = 0
        rear = 0
    else if (front == 0):
        front = size - 1
    else:
        front = front - 1
      
    deque[front] = element
```

---

### 2. **Insertion at Rear (`insertRear`)**

Inserts an element at the rear of the deque.

#### Algorithm:

1. **Check if the deque is full**:
   - If the deque is full (i.e., `(front == 0 && rear == size - 1)` or `(front == rear + 1)`), the insertion cannot be performed.
2. **If the deque is empty**:
   - Set both `front` and `rear` to `0` (initializing the deque).
3. **If `rear` is at the last position of the array** (i.e., `rear == size - 1`):
   - Set `rear = 0` (wrap around to the first index).
4. **Otherwise**, increment the `rear` pointer by 1.
5. **Insert** the new element at `rear`.

#### Conditions:

- **IsFull:** `(front == 0 && rear == size - 1)` or `(front == rear + 1)`
- **IsEmpty:** `front == -1`

#### Pseudocode:

```pseudo
insertRear(deque, element):
    if (deque is full):
        return "Overflow"
  
    if (deque is empty):
        front = 0
        rear = 0
    else if (rear == size - 1):
        rear = 0
    else:
        rear = rear + 1
      
    deque[rear] = element
```

---

### 3. **Deletion from Front (`deleteFront`)**

Removes an element from the front of the deque.

#### Algorithm:

1. **Check if the deque is empty**:
   - If the deque is empty (`front == -1`), the deletion cannot be performed.
2. **If there is only one element left** (`front == rear`):
   - Set both `front` and `rear` to `-1` (deque becomes empty).
3. **If `front` is at the last position of the array** (i.e., `front == size - 1`):
   - Set `front = 0` (wrap around to the first index).
4. **Otherwise**, increment the `front` pointer by 1.

#### Conditions:

- **IsEmpty:** `front == -1`

#### Pseudocode:

```pseudo
deleteFront(deque):
    if (deque is empty):
        return "Underflow"
  
    removedElement = deque[front]
  
    if (front == rear):
        front = -1
        rear = -1
    else if (front == size - 1):
        front = 0
    else:
        front = front + 1
  
    return removedElement
```

---

### 4. **Deletion from Rear (`deleteRear`)**

Removes an element from the rear of the deque.

#### Algorithm:

1. **Check if the deque is empty**:
   - If the deque is empty (`front == -1`), the deletion cannot be performed.
2. **If there is only one element left** (`front == rear`):
   - Set both `front` and `rear` to `-1` (deque becomes empty).
3. **If `rear` is at the first position of the array** (i.e., `rear == 0`):
   - Set `rear = size - 1` (wrap around to the last index).
4. **Otherwise**, decrement the `rear` pointer by 1.

#### Conditions:

- **IsEmpty:** `front == -1`

#### Pseudocode:

```pseudo
deleteRear(deque):
    if (deque is empty):
        return "Underflow"
  
    removedElement = deque[rear]
  
    if (front == rear):
        front = -1
        rear = -1
    else if (rear == 0):
        rear = size - 1
    else:
        rear = rear - 1
  
    return removedElement
```

---

### 5. **Get Front (`getFront`)**

Retrieves the element at the front without removing it.

#### Algorithm:

1. **Check if the deque is empty**:
   - If the deque is empty (`front == -1`), return an error or appropriate message.
2. **Return the element** at the `front` index.

#### Conditions:

- **IsEmpty:** `front == -1`

#### Pseudocode:

```pseudo
getFront(deque):
    if (deque is empty):
        return "Deque is empty"
  
    return deque[front]
```

---

### 6. **Get Rear (`getRear`)**

Retrieves the element at the rear without removing it.

#### Algorithm:

1. **Check if the deque is empty**:
   - If the deque is empty (`front == -1`), return an error or appropriate message.
2. **Return the element** at the `rear` index.

#### Conditions:

- **IsEmpty:** `front == -1`

#### Pseudocode:

```pseudo
getRear(deque):
    if (deque is empty):
        return "Deque is empty"
  
    return deque[rear]
```

---

### 7. **Is Full (`isFull`)**

Checks if the deque is full.

#### Algorithm:

1. The deque is full if:
   - The `front` is at `0` and the `rear` is at `size - 1` (i.e., `front == 0 && rear == size - 1`).
   - Or, the `front` is one position ahead of the `rear` (i.e., `front == rear + 1`).

#### Pseudocode:

```pseudo
isFull(deque):
    return (front == 0 && rear == size - 1) or (front == rear + 1)
```

---

### 8. **Is Empty (`isEmpty`)**

Checks if the deque is empty.

#### Algorithm:

1. The deque is empty if:
   - Both `front` and `rear` are set to `-1`.

#### Pseudocode:

```pseudo
isEmpty(deque):
    return (front == -1)
```

---

### Summary Table:

| Operation   | Front Operation                                                 | Rear Operation |
| ----------- | --------------------------------------------------------------- | -------------- |
| Insert      | `insertFront`                                                 | `insertRear` |
| Delete      | `deleteFront`                                                 | `deleteRear` |
| Get/Peek    | `getFront`                                                    | `getRear`    |
| Check Full  | `(front == 0 && rear == size - 1)` or `(front == rear + 1)` |                |
| Check Empty | `(front == -1)`                                               |                |

This set of operations and algorithms forms the basis for implementing a **double-ended queue (deque)**, providing versatility and efficient manipulation at both ends.
