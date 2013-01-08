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
	a = 0
	while a < 10:
		a = a + 1
		stack.append(a) #Stack PUSH
	print stack
	
	while stack:
		print stack 
		stack.pop() #Stack POP
	main()
		
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
	main()
	
def wrong():
	print 'sorry wrong number'
	main()
	
def quit():
	sys.exit()
main()
