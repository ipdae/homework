import sys

		
def stack():
	stack = [] #Stack create
	a = 0 
	print 'Stack PUSH'
	while a < 10:
		a = a + 1	
		stack.append(a) #Stack PUSH
	print stack
	
	print 'Stack POP'
	while stack:
		print stack 
		stack.pop() #Stack POP
	
		
def queue():
	queue = [] #Queue create
	a = 0
	print 'Queue PUT'
	while a < 10:
		a = a + 1
		queue.append(a) #Queue PUT
	print queue
	
	print 'Queue GET'
	while queue:
		print queue
		queue.pop(0) #Queue GET
	
	

	
stack()
queue()
sys.exit()
