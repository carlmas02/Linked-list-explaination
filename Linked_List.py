class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None


	#traversal
	def print_list(self):
		item = self.head
		while item is not None:
			print(item.data)
			item = item.next

	#add nodes to linkedlist
	def node_at_beginning(self,data):
		new_node = Node(data)
		new_node.next = self.head 
		self.head = new_node
		
	def node_at_end(self,data):
		new_node = Node(data)
		last = self.head
		while last.next is not None:
			last = last.next
		last.next = new_node

	def node_in_middle(self,data,x):
		new_node = Node(data)
		new = self.head
		while new.next is not None:
			if new.data == x:
				break
			new = new.next
		new_node.next = new.next
		new.next = new_node

	#delete nodes in linkedlist
	def delete_node_at_beginning(self):
		self.head = self.head.next

	def delete_last_node(self):
		last = self.head
		while last.next.next is not None:
			last = last.next
		last.next = None

	#length of linkedlist
	def length_list(self):
		num = 0
		count = self.head
		while count is not None:
			count = count.next
			num+=1
		print(num)

	#search item in linkedlist
	def search_item(self,item):
		n = 0
		word = self.head
		while word.next is not None:
			if word.data == item:
				print(f"item found at {n} index.")
				break
			else :
				n+=1
				word = word.next
		print("item not found")

	#nth node from end of linkedlist
	'''Given a Linked List and a number n, write a function that returns the value
		at the n’th node from the end of the Linked List.
		For example, if the input is below list and n = 3, then output is “B”'''
	def n_node_from_end(self,position):
		len_list = 1
		start = self.head
		while start.next is not None:
			len_list+=1 
			start = start.next

		pos = len_list - position
		start = self.head
		for i in range(pos):
			start = start.next
		print(f'item is {start.data}')

	#check if a linked list palindrome
	def palindrome(self):
		start = self.head
		string = ''
		while start is not None:
			print(start.data)
			string += start.data
			start = start.next
		#print(string)
		if string == string[::-1]:
			print("String is palindrome")
		else :
			print("String is not palindrome")

	#remove duplicates from sorted linkedlist
	def remove_duplicates(self):
		start = self.head
		while start.next is not None:
			if start.data == start.next.data:
				start.next = start.next.next
			else :
				start = start.next

	#move last elemnt to front
	def last_to_front(self):
		temp = self.head
		while temp.next.next is not None: #so we will stop traversing at second last node
			temp = temp.next
		temp.next.next = self.head   #point last node to head , so last node ends up becoming first node
		self.head = temp.next		 #make value of last node as head
		temp.next = None             #point second-last node to None, which ends the linked list at second last node 
		

	#reverse a linkedlist
	def reverse_list(self):
		current = self.head
		prev = None
		while current is not None:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node
		self.head = prev

		

	def odd_even_list(self):
		'''count = self.head
		num = 0
		while count is not None:
			num += 1
			count = count.next
		if num % 2 == 0:
			print("Even")
		else :
			print("Odd")'''
		while (self.head != None and self.head.next != None):
			self.head = self.head.next.next
		if(self.head == None):
			return 0
		return 1
		#0 is even 1 is odd

	#swap the elements of linked list pairwise 
	def pair_wise_swap(self):
		temp = self.head

		while (temp != None and temp.next != None):
			#if value is same no need to swap
			if temp.data == temp.next.data:
				temp = temp.next.next # point to next to next node
			else :
				temp.data,temp.next.data = temp.next.data,temp.data
				temp = temp.next.next


	#modify the linked list such that all even numbers appear
	#before all the odd numbers in the modified linked list.
	#keep order same
	def even_odd_nodes(self):
		start = self.head
		while start is not None:
			if start.data % 2 != 0 :
				start.next = self.head
				prev.next = start.next




		
#output
FE = Linkedlist()



FE.node_at_beginning(3)
FE.node_at_beginning(5)
FE.node_at_beginning(4)
FE.node_at_beginning(2)
FE.node_at_end(100)
FE.print_list()




#FE.reverse_ll()

print("")

#FE.length_list()

#FE.search_item("Gifford")

#FE.n_node_from_end(3)

#FE.palindrome()

#FE.remove_duplicates()

#FE.last_to_front()

#FE.reverse_list()

#print(FE.odd_even_list())


#FE.delete_last_node()

#FE.pair_wise_swap()

FE.even_odd_nodes()

FE.print_list()


