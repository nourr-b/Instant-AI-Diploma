#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(stack.pop())  
print(stack.pop())  


print(stack.is_empty())  


print(stack.pop())  
print(stack.pop())  


# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linked_list = LinkedList()


linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(15)

# Inserting elements at the end
linked_list.insert_at_end(20)
linked_list.insert_at_end(25)


linked_list.print_list() 


linked_list.remove(10)


linked_list.print_list()  


# In[3]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

        
doubly_linked_list = DoublyLinkedList()


doubly_linked_list.insert_at_beginning(5)
doubly_linked_list.insert_at_beginning(10)
doubly_linked_list.insert_at_beginning(15)


doubly_linked_list.insert_at_end(20)
doubly_linked_list.insert_at_end(25)


doubly_linked_list.print_list()  

doubly_linked_list.remove(10)

doubly_linked_list.print_list()  


# In[4]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            last_node = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = last_node
            last_node.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            last_node = self.head.prev
            new_node.prev = last_node
            last_node.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def remove(self, data):
        if self.head is None:
            return

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:
                    self.head = None
                else:
                    prev_node = current.prev
                    next_node = current.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    if current == self.head:
                        self.head = next_node
                return

            current = current.next
            if current == self.head:
                break

    def print_list(self):
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

circular_doubly_linked_list = CircularDoublyLinkedList()

circular_doubly_linked_list.insert_at_beginning(5)
circular_doubly_linked_list.insert_at_beginning(10)
circular_doubly_linked_list.insert_at_beginning(15)

circular_doubly_linked_list.insert_at_end(20)
circular_doubly_linked_list.insert_at_end(25)


circular_doubly_linked_list.print_list()  

circular_doubly_linked_list.remove(10)

circular_doubly_linked_list.print_list()  


# In[5]:


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print(queue.dequeue())  
print(queue.dequeue())  

print(queue.is_empty())  

print(queue.dequeue()) 
print(queue.dequeue())  


# In[6]:


import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[2]
        else:
            print("Priority queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

priority_queue = PriorityQueue()

priority_queue.enqueue(5, 2)
priority_queue.enqueue(10, 1)
priority_queue.enqueue(15, 3)

print(priority_queue.dequeue())  
print(priority_queue.dequeue())  

print(priority_queue.is_empty())  

print(priority_queue.dequeue())  
print(priority_queue.dequeue())  


# In[7]:


class Map:
    def __init__(self):
        self.map = {}

    def add(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key)

    def contains(self, key):
        return key in self.map

    def remove(self, key):
        if self.contains(key):
            del self.map[key]

    def size(self):
        return len(self.map)

    def keys(self):
        return self.map.keys()

    def values(self):
        return self.map.values()

map = Map()

map.add("one", 1)
map.add("two", 2)
map.add("three", 3)

print(map.get("two")) 

print(map.contains("four"))  


map.remove("two")

print(map.size())  

print(list(map.keys())) 
print(list(map.values()))  


# In[8]:


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def has_path(self, u, v):
        visited = set()
        return self._has_path_recursive(u, v, visited)

    def _has_path_recursive(self, u, v, visited):
        visited.add(u)

        if u == v:
            return True

        for neighbor in self.graph[u]:
            if neighbor not in visited:
                if self._has_path_recursive(neighbor, v, visited):
                    return True

        return False

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)

print("DFS traversal:")
graph.dfs(1) 


print("\nBFS traversal:")
graph.bfs(1)  

print("\nHas path between 1 and 5:", graph.has_path(1, 5))  
print("Has path between 2 and 3:", graph.has_path(2, 3)) 


# In[9]:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.value, end=" ")

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

tree = BinaryTree()

tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)

print("Inorder traversal:")
tree.inorder_traversal()  

print("\nPreorder traversal:")
tree.preorder_traversal() 

print("\nPostorder traversal:")
tree.postorder_traversal() 

value = 5
result = tree.search(value)
if result is not None:
    print(f"\nFound {value} in the tree")
else:
    print(f"\n{value} not found in the tree")


# In[10]:


class Set:
    def __init__(self):
        self.set = []

    def add(self, element):
        if element not in self.set:
            self.set.append(element)

    def remove(self, element):
        if element in self.set:
            self.set.remove(element)

    def contains(self, element):
        return element in self.set

    def union(self, other_set):
        union_set = Set()

        for element in self.set:
            union_set.add(element)

        for element in other_set.set:
            union_set.add(element)

        return union_set

    def intersection(self, other_set):
        intersection_set = Set()

        for element in self.set:
            if other_set.contains(element):
                intersection_set.add(element)

        return intersection_set

    def difference(self, other_set):
        difference_set = Set()

        for element in self.set:
            if not other_set.contains(element):
                difference_set.add(element)

        return difference_set

    def size(self):
        return len(self.set)

    def elements(self):
        return self.set

set1 = Set()

set1.add(1)
set1.add(2)
set1.add(3)

set2 = Set()
set2.add(2)
set2.add(3)
set2.add(4)

set1.remove(1)

print(set1.contains(2))  
print(set1.contains(4)) 

print("Union:", set1.union(set2).elements()) 
print("Intersection:", set1.intersection(set2).elements()) 
print("Difference:", set1.difference(set2).elements())  

print("Size of set1:", set1.size())  


# In[ ]:




