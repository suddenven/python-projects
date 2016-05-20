#Binary Search Algorithm

#First the algorithm cut the array in half
#if the guess is lower than the answer, max is reassigned to average -1
#if the guess is higher than the answer, min is reassigned to average +1
#Repeat until the answer is found, or return -1 when there isnt such a thing in the array

def BinSearch(array,finding):
	minimum = 0
	maximum = len(array)
	
	while(True):
	
		average = (minimum + maximum /2)
		
		if (array[average] == finding):
			print "Found %d at index %d." %(finding,average)
			break
			
		elif (maximum <= minimum):
			print "There is no such element in the array!"
			break
		
		elif (array[average] > finding):
			maximum = average - 1
		elif (array[average] < finding):
			minimum = average + 1
			
a = [1,2,7,9,11,13,15,17,48,56,67,78,89,91,94,92]

BinSearch(a,9)

wait = raw_input('end of program, press enter to exit')