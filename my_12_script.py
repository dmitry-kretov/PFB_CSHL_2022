#!usr/bin/env python3
numbers = [101,2,15,22,95,33,2,27,72,15,52]
numbers_odd = []
numbers_even = []
sorted_numbers = sorted(numbers)
print(sorted_numbers)
for number in numbers:
	if number % 2 ==0:
		numbers_even.append(number)
	else:
		numbers_odd.append(number)
print("Sum of even numbers:",sum(numbers_even))
print("Sum of odds:", sum(numbers_odd))
