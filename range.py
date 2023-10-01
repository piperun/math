import random, math, statistics, timeit
import numpy as np

def calculate():
	students = 11
	average = 18.3
	i = 0
	qoutient = 0
	grades = []


	while i != average:
		for x in range(0,students + 1):
			grades.append(round(random.uniform(10, 20), 1))
			i += grades[x]

			if x == students:
				qoutient = i/students
				rounded = round(qoutient, 1)
				if rounded == average:
					print(*grades, sep='\n')
					print("Median: %s" % statistics.median(grades))
					exit()

				else:
					i = 0
					del rounded
					del qoutient
					del x
					del grades[:]

calculate()