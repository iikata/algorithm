from typing import  List

def insetionSort(numbers:List[int]) -> List[int]:
	l =len(numbers)
	for i in range(1,l):
		temp =numbers[i]
		j=i -1
		while j >=0 and numbers[j]>temp:
			numbers[j+1] =numbers[j]
			j -= 1
		numbers[j+1] =temp
		
	return numbers
	
if __name__ =='__main__':
	import random
	nums = [random.randint(1,9999) for _ in range(100)]
	
	print(insetionSort(nums))
