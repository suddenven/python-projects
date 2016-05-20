#Insertion Sort Algorithm

#swapping algorithm
def swap(array,first,second):
	temp = array[first]
	array[first] = array [second]
	array[second] = temp

#For every element in the array, 
#check if the subsequent value is lower than its current value or not. 
#If it is lower, it will swap with the current value, and then swap until it reaches a suitable position. 

def InsertionSort(array):
	for i in range(0,len(array)):
		current = i
		while (i > 0 and array[i] < array[i-1]):
			swap(array,i,i-1)
			i = i-1
			
#test out with sample data
a = [31,34,75,1,5,6]
print a
InsertionSort(a)
print a

wait = raw_input('end of program, press enter to exit')
