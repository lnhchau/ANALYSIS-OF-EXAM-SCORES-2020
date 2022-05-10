with open("data_cleaning.txt", "r", encoding = "utf-8") as  file:
	data = file.read().split("\n")
header = data[0]
students = data[1:]

students.pop()
total_student = int(len(students))

header = header.split(",")
subject = header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

for student in students:
	for j in range(len(not_take_exam)):
		if student[j+5] == "-1":
			not_take_exam[j] += 1

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(not_take_exam)):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)

print(header)
print(not_take_exam_percentage)
print(not_take_exam)

# PLOT BARCHART
import matplotlib.pyplot as plt
import numpy
import pandas as pd

fig, ax = plt.subplots()
y_pos = numpy.arange(len(subject))

plt.bar(y_pos, not_take_exam_percentage)
plt.xticks(y_pos, subject)

ax.set_ylim(0,100)

plt.xlabel('SUBJECTS')
plt.ylabel('PERCENTAGE')
plt.title('Số học sinh bỏ thi hoặc không đăng ký năm 2020')

rects = ax.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom")

plt.show()
