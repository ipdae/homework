#Stack is LIFO(Last In First Out)
#Queue is FIFO(First In First Out)
import sys
stack = [] #Stack create
queue = [] #Queue create
def main():
	num = 0
	while num != 7:
		print '1. Insert Stack'
		print '2. Delete Stack'
		print '3. Show Stack'
		print '4. Insert Queue'
		print '5. Delete Queue'
		print '6. Show Queue'
		print '7. Exit'
		
		num = int(raw_input('Choose number :'))
	
		if num == 1:
			print 'Insert Stack'
			a = raw_input('>')
			stack.append(a) #Stack PUSH
			print stack
			print '\n'
			
		elif num == 2:
			print 'Delete Stack'
			stack.pop() #Stack POP
			print stack
			print '\n'
			
		elif num == 3:
			print 'Show Stack'
			print stack
			print '\n'
			
		elif num == 4:
			print 'Insert Queue'
			a = raw_input('>')
			queue.append(a) #Queue PUT
			print queue
			print '\n'
			
		elif num == 5:
			print 'Delete Queue'
			queue.pop(0)
			print queue #Queue GET
			print '\n'
			
		elif num == 6:
			print 'Show Queue'
			print queue
			print '\n'
		
		elif num == 7:
			sys.exit()
		else:
			print 'Sorry wrong number'
			print '\n'
		
main()
