# Basic Linked List

class Node:
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		return self.data

# node3 = Node("Node3", None)
# node2 = Node("Node2", node3)
# node1 = Node("Node1", node2)

# print(node1.next_node)                                    # Node2
# print(node3.next_node)                                    # None

class LinkedList:
	def __init__(self):
		self.head = None
		self.last_node = None

	def __str__(self):                                    # Print LinkedList mapping 
		node = self.head
		s = f"{node.data}"
		while node.next_node:
			s += f" -> {node.next_node.data}"
			node = node.next_node
		s += " -> None"
		return s

	def insert_at_start(self, data):
		new_data = Node(data, self.head)                  # Insert new node
		self.head = new_data                              # Set head to newly inserted node
		if self.last_node is None:                        # Check if last_node is empty
			self.last_node = new_data                     # Set last node. Only done for the first time when LL is initialized

	def insert_at_end(self, data):
		if self.head is None:                             # Check if LinkedList is empty
			self.insert_at_start(data)                    # If empty insert @ start
		else:
			self.last_node.next_node = Node(data, None)   # Update Last nodes next node with new node
			self.last_node = self.last_node.next_node     # Update last_node to newly inserted node

	def delete_node(self, data):
		if self.head is None:
			return "LinkedList is Empty"
		
		node = self.head
		prev_node = None
		while node:
			if node.data == data:                          
				if prev_node:                              # If node has previous node
					prev_node.next_node = node.next_node   # Then set previous nodes next node to current nodes next node
				else:                                      # If Node is first in LL
					self.head = node.next_node             # Set LL head to next node
				return "Deleted"
			prev_node = node
			node = node.next_node
			



ll = LinkedList()
ll.insert_at_start("Node1")
ll.insert_at_start("Node2")
ll.insert_at_end("END")
ll.insert_at_end("END 00")
print(ll)                                                  # Node2 -> Node1 -> END -> END 00 -> None
print(ll.delete_node("Node1"))                             # Deleted
print(ll)                                                  # Node2 -> END -> END 00 -> None