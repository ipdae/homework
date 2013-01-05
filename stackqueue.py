#Stack is LIFO(Last In First Out)
#Queue is FIFO(First In First Out)
import sys

stack = [] #Stack create
queue = [] #Queue create

def main():
	print '1. Insert Stack'
	print '2. Delete Stack'
	print '3. Show Stack'
	print '4. Insert Queue'
	print '5. Delete Queue'
	print '6. Show Queue'

	num = int(raw_input('choose number :'))
	
	if num == 1:
		insert_stack()
	elif num == 2:
		delete_stack()
	elif num == 3:
		show_stack()
	elif num == 4:
		insert_queue()
	elif num == 5:
		delete_queue()
	elif num == 6:
		show_queue()
	else:
		wrong()
		
def insert_stack():
	print 'Insert Stack'
	a = raw_input('>')
	stack.append(a) #Stack PUSH
	print stack
	main()
	
def delete_stack():
	stack.pop() #Stack POP
	print stack
	main()
	
def show_stack():
	print 'Show Stack'
	print stack
	main()
	
def insert_queue():
	print 'Insert Queue'
	a = raw_input('>')
	queue.append(a) #Queue PUT
	print queue
	main()
	
def delete_queue():
	queue.pop(0) #Queue GET
	print queue
	main()

def show_queue():
	print 'Show Queue'
	print Queue
	main()
	
def wrong():
	print 'sorry wrong number'
	main()
	
main()