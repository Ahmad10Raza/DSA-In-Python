
# Algorithm:

# 1. Create a class CircularQueue with the following methods:
#    a. __init__(size): Initializes the class with a given size
#    b. enqueue(data): Adds an element to the circular queue
#    c. dequeue(): Removes and returns an element from the circular queue
#    d. display(): Displays the elements of the circular queue

# Enueue operation:
# 1. Check if the circular queue is full by checking if (rear + 1) % size == front
# 2. If the queue is full, print "Queue is Full"
# 3. If the queue is empty, set front and rear to 0 and add the element at the rear
# 4. If the queue is not full, increment the rear and add the element at the rear

# Dequeue operation:
# 1. Check if the circular queue is empty by checking if front == -1
# 2. If the queue is empty, print "Queue is Empty"
# 3. If there is only one element in the queue, set front and rear to -1 and return the element
# 4. If the queue is not empty, return the element at the front and increment the front


class CircularQueue():

	# constructor
	def __init__(self, size): # initializing the class
		self.size = size
		
		# initializing queue with none
		self.queue = [None for i in range(size)] 
		self.front = self.rear = -1

	def enqueue(self, data):
		
		# condition if queue is full
		if ((self.rear + 1) % self.size == self.front): 
			print(" Queue is Full\n")
			
		# condition for empty queue
		elif (self.front == -1): 
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			
			# next position of rear
			self.rear = (self.rear + 1) % self.size 
			self.queue[self.rear] = data
			
	def dequeue(self):
		if (self.front == -1): # condition for empty queue
			print ("Queue is Empty\n")
			
		# condition for only one element
		elif (self.front == self.rear): 
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
	
		# condition for empty queue
		if(self.front == -1): 
			print ("Queue is Empty")

		elif (self.rear >= self.front):
			print("Elements in the circular queue are:", 
											end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Elements in Circular Queue are:", 
										end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		if ((self.rear + 1) % self.size == self.front):
			print("Queue is Full")

# Driver Code
ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()

# This code is contributed by AshwinGoel 
