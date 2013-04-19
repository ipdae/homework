class LinkedList:
	def __init__(self):
		self.head = None
		self.current = None
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
		for i in self:
			if i == n:
				s += 1
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
		self.current = self.head
		return self
	def next(self):
		s = self.current
		if s == None:
			raise StopIteration
		self.current = self.current.next
		return s.data
	def nodeiter(self):
		return NodeIter(self.head)
		
class NodeIter:

	
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


class Sellable(object):
	def sell(self):
		print "{0} is sold.".format(self.get_name())

class Boonger(Sellable):
	def __init__(self):
		self.name = "Boonger"
	def xx(self):
		return 'pot'

class Inger(Sellable):
	def __init__(self):
		self.name = "Inger"
	def xx(self):
		return 'vanilla'