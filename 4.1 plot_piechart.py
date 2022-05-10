with open("data_cleaning.txt", "r", encoding = "utf-8") as file:
	datas = file.read().split("\n")

header = datas[0].split(",")
subjects = header[5:]
total_subjects = len(subjects) - 2 # khtn, khxh

students = datas[1:]
students.pop()
total_students = len(students)

for i in range(total_students):
	students[i] = students[i].split(",")

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0]

for s in students:
	total_exams = 0
	for i in range(5, len(s)):
		if i in [7,8]: 
			continue
		if s[i] != "-1":
			total_exams += 1
	num_of_exam_taken[total_exams] += 1

print(num_of_exam_taken)

import matplotlib.pyplot as plt
import numpy 
mylabels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sizes = num_of_exam_taken
num = numpy.array(num_of_exam_taken)

explode = (0,0.1,0,0,0,0,0.5,0,0,0)

fig, ax = plt.subplots()
plt.legend(title = "SỐ MÔN HS THI")
ax.pie(sizes, explode = explode, labels = mylabels, autopct='%1.1f%%', startangle=90) 

plt.show()