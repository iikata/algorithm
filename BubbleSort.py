from typing import List

def bubbleSort(numbers: List[int]) -> List[int]:
	lenNumbers = len(numbers)
	for i in range(lenNumbers):
		for j in range(lenNumbers - 1 - i):
			if numbers[j] > numbers[j+1]:
				numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
	return numbers


if __name__ == '__main__':
	import random
	nums = [random.randint(0,1000)for i in range(10)]
	print(bubbleSort(nums))

