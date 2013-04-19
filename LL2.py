class LinkedList:
	def __init__(self):
		self.head = None
		self.n = -1
	def print_list(self):
		current = self.head
		while current:
			print current.data
			current = current.next
	def len_list(self):
		current = self.head
		s = 0
		while current:
			s += 1
			current = current.next
		return s
	def __repr__(self):
		current = self.head
		if self.head == None:
			return str(None)
		else:
			while current:
				s = str(current.data)
				while current.next != None:
					current = current.next 
					s = s + str(' ') + str(current.data)
				return str(s)
	def __getitem__(self, key):
		s = 0
		current = self.head
		while current:
			if key == s:
				return current.data
			else:
				s += 1
				current = current.next
	def __setitem__(self, key, value):
		s = 0
		current = self.head
		while current:
			if key == s:
				current.data = value
				return value
			else:
				s += 1
				current = current.next
	def __delitem__(self, key):
		s = 0
		current = self.head
		while current:
			if key == s:
				self.head = self.head.next
				break
			elif key == s + 1:
				first = current
				second = current.next
				first.next = second.next
				second = None
				break
			else:
				s += 1
				current = current.next
	def range_list(self,n):
		s = 0
		current = self.head
		while current:
			if current.data == n:
				s += 1
			current = current.next
		return s
	def append_first(self,s):
		n = Node(s)
		if self.head == None:
			self.head = n
		else:
			n.next = self.head
			self.head = n		
	def append_last(self,s):
		n = Node(s)
		if self.head == None:
			self.head = n		
		else:
			current = self.head
			while current:
				if current.next == None:
					current.next = n
					break
				else:
					current = current.next
	def pop_first(self):
		n = self.head
		self.head = self.head.next
		return n.data
	def pop_last(self):
		current = self.head
		while current:
			if current.next == None:
				n = self.head
				self.head = None
				return n.data
			elif current.next.next == None:
				n = current.next
				current.next = None
				return n.data
			else:
				current = current.next
	def __contains__(self, item):
		current = self.head
		while current:
			if current.data != item:
				current = current.next
				if current == None:
					return False
			elif current.data == item:
				return True
	def __reversed__(self):
		current = self.head
		s = LinkedList()
		while current:
			s.append_first(current.data)
			current = current.next
		return s
	def __iter__(self):
		while self.n < self.len_list() - 1:
			self.n += 1
			yield self[self.n]
		
