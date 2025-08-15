# Data Structure
- Every program or software relies on data, we dont want this data to be scattered around the memory, we want it neatly placed in memory and to be easily accessible.
- We use Data Structures for this, Data structures are the in memory representation of data.

> Arrays
- Collection of items stored consecutively in memory
- All items in an array have same type
- Fixed size
why mixed arrays are allowed in JS?
- Because when you try to add a new element to an array of 3 elements if the consecutive space is not available, it'll look for a space in memory where it has 4 consecutive blocks put the array there and clear the current space where it present in memory
Operations & Complexity
- Accessing element at index : O(1)
- Inserting at Index : O(n)
- Deleting from index : O(n)
- Updating at Index : O(1)
- Traversing the array : O(n)

> Linked Lists
- Linear collection of elements where each element points to the next element in memory
- Each element is called a Node.
- First element is called HEAD of the list
- Last element is called TAIL of the list

>> Singly Linked List
Node -> Data and next node pointer

Operations & Complexity
- Inserting an element at the start : O(1)
HEAD
  n1 -> n2 -> n3 -> null
- Create a new node
- Point the new node to the head
- Change the head as the new node

- Inserting an element at the end : O(1)
HEAD         TAIL
  n1 -> n2 -> n3 -> null
- Create a new node
- Point the tail node to the new node
- Change the new node as TAIL

- Inserting an element at middle : O(1)
HEAD         TAIL
  n1 -> n2 -> n3 -> null
- Create a new node
- Point the new node to the element before which we are gonna insert it
- Make the previous element point to this node

- Deleting an element at the start : O(1)
HEAD
  n1 -> n2 -> n3 -> null
- Point the head to the next node of the current head

- Deleting an element at the end : O(1)
HEAD         TAIL
  n1 -> n2 -> n3 -> null
- Change TAIL as the second last node and point it to NULL

- Deleting an element at middle : O(1)
HEAD         TAIL
  n1 -> n2 -> n3 -> null
  n1   n2 -> n3 -> null
   |------|
- Point the deleting nodes previous node to its next node

- Traversing a Linked List : O(n)

- Accessing an element : O(n)

>> Doubly Linked List
- Node -> Prev-Data-Next

>> Circular Linked List
- TAILs next points to the HEAD

>> Doubly Circular Linked List
- Node -> Prev<-Data->Next
- HEADs prev points to the TAIL
- TAILs next points to the HEAD


> Stack
- Linear collections of items where items are inserted and removed in a particular order
- FILO/LIFO i.e. First in Last out

Stack.isEmpty() - True if the Stack is empty
Stack.push(n) - Push the element to the stack
Stack.pop() - Removes the top element from the stack and returns it
Stack.peek() - peeks the top element of the stack and returns it
Stack.size() - return the length of the stack

Used for use cases such as
- Undo/Redo operation
- for Back Tracking like program to solve a maze


> Queue
- Linear collections of items where items are inserted and removed in a particular order
- FIFO i.e. First In First Out

queue.isEmpty() - return true if the queue is empty
queue.enqueue() - adds an item to the queue
queue.dequeue() - remove the item at first and returns it from the queue
queue.peek() - returns the first element of the queue
queue.size() - returns the size of the queue

> Hash Table
- Map, Dictionary, Hash Map, Associative array - different names of the hash table data structure
- Used for key-value lookup
fruits  price
mango -> 10
kiwi  -> 15
orange-> 8

Complexity of all the operations in hash table - O(1)
pricelist = {}
pricelist['mango'] = 10
pricelist['kiwi'] = 15
pricelist['orange'] = 8
pricelist['mango'] #returns 10
delete pricelist['kiwi']

BTS of Hash Table

Key(Against which we      Hash Function(Takes the input and gives     Values(The value we need 
 store the values)    ->    back the hash code/index in array)    ->  to store against a key)
                                                                      we will have a array of values

- The hash function should always return the same output for the same input
- Handle Hash Table collisions, i.e. there are possibilities that the hash function could return the same output for different inputs
  -> Separate Chaining(added image)
  -> Open Addressing

> Tree
- All the above discussed were Linear Data Structure
- Tree is a Hierarchical Data Structure
- Used to represent Hierarchical Data like Organizational Hierarchy, Directory structure, Databse Indexes, Compiler design, etc.


> Heap
- A tree based data structure in which the value of a parent node is ordered in a certain way with respect to its child nodes
- It can either be a min-heap or a max-heap
conditions:
- should be a complete binary tree
- Either a Min-heap(parent node <= child nodes) or a max-heap(parent node >= child nodes)
use cases of heap
- Whenever you need a min or max value quickly
- Priority queues
- Heap sort
- Dijkstra's algorithm
