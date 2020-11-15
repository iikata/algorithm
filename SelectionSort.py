from typing import List

def selectionSort(numbers: List[int]) -> List[int]:
	lenNumber = len(numbers)
	for i in range(lenNumber):
		minIdx = i
		for j in range(i+1, lenNumber):
			if numbers[minIdx] > numbers[j]:
				minIdx = j
				
		numbers[i],numbers[minIdx] = numbers[minIdx],numbers[i]
	return numbers
	
if __name__ == '__main__':
	import random
	nums = [random.randint(0,9999) for _ in range(999)]
	print(selectionSort(nums))
				
				
