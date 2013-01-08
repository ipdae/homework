import sys

def main():
	print '1. Stack'
	print '2. Queue'
	print '3. Quit'
	
	num = int(raw_input('choose number :'))

	if num == 1:
		stack()
	elif num == 2:
		queue()
	elif num == 3:
		quit()
	else:
		wrong()
		
def stack():
	stack = [] #Stack create
	stack.append(1) #Stack PUSH
	stack.append(2)
	stack.append(3)
	stack.append(4)
	print stack
	
	while stack:
		print stack 
		stack.pop() #Stack POP
	main()
		
def queue():
	queue = [] #Queue create
	queue.append(1) #Queue PUSH
	queue.append(2)
	queue.append(3)
	queue.append(4)
	print queue
	
	while queue:
		print queue
		queue.pop(0) #Queue GET
	main()
	
def wrong():
	print 'sorry wrong number'
	main()
	
def quit():
	sys.exit()
main()