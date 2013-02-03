class Node:
	def __init__(self,data,prev=None,next=None):
		self.data = data
		self.prev = prev
		self.next = next
class LinkedList:
	def __init__(self):
		self.head = None
		self.current = None
		self.tail = None
	def print_list(self):
		current = self.head
		while current:
			print current.data
			current = current.next
	def __len__(self):
		s = 0 
		for i in self:
			s += 1
		return s
	def __repr__(self):
		current = self.head
		if self.head == None:
			return str(None)
		else:
			s = str(current.data)
			while current.next != None:
				current = current.next 
				s = s + str(' ') + str(current.data)
			return s
	def __getitem__(self, key):
		s = 0
		for i in self:
			if s == key:
				return i
			else:
				s += 1
	def __setitem__(self, key, value):
		s = 0
		for i in self.nodeiter():
			if s == key:
				i.data = value
				return 
			else:
				s += 1
	def __delitem__(self, key): #used nodeiter()
		s = 0
		for i in self.nodeiter():
			if s == key:
				self.head = self.head.next
				return
			elif s + 1 == key:
				a = self.head
				b = self.head.next
				a.next = b.next
				b.prev = a
				return
			else:
				s += 1 
	def range_list(self,n):
		s = 0
		for i in self:
			if i == n:
				s += 1
		return s
	def append_first(self,s): #add self.tail, self.prev
		n = Node(s)
		if self.head == None:
			self.head = n
			self.tail = n
		else:
			n.next = self.head
			self.tail = self.head
			self.head.prev = n
			self.head = n		
	def append_last(self,s): #add self.tail, self.prev
		n = Node(s)
		if self.head == None:
			self.head = n	
			self.tail = n	
		else:
			current = self.tail
			self.tail.next = n
			n.prev = current
			self.tail = n
	def pop_first(self): #add self.tail, self.prev
		n = self.head
		self.head = self.head.next
		return n.data
	def pop_last(self): #add self.tail, self.prev
		n = self.tail
		self.tail = self.tail.prev
		if self.tail == None:
			self.head = None
			return n.data
		else:
			self.tail.next = None
			return n.data
	def __contains__(self, item):
		for i in self:
			if i == item:
				return True
		return False
	def __reversed__(self):
		s = LinkedList()
		for i in self:
			s.append_first(i)
		return s
	def __iter__(self):
		return DataIter(self.head)
	def nodeiter(self):
		return Iter(self.head)
class Iter(object):
	def __init__(self,head):
		self.current = head
	def __iter__(self):
		return self
	def next(self):
		s = self.current
		if s == None:
			raise StopIteration
		self.current = self.current.next
		return s
class DataIter(Iter):
	def next(self):
		return super(DataIter,self).next().data		
