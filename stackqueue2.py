import sys

		
def stack():
	stack = [] #Stack create
	a = 0 
	while a < 10:
		a = a + 1	
		stack.append(a) #Stack PUSH
	print stack
	
	while stack:
		print stack 
		stack.pop() #Stack POP
	
		
def queue():
	queue = [] #Queue create
	a = 0
	while a < 10:
		a = a + 1
		queue.append(a) #Queue PUSH
	print queue
	
	while queue:
		print queue
		queue.pop(0) #Queue GET
	
	

	
stack()
queue()
sys.exit()
