with open("data_cleaning.txt", "r", encoding = "utf-8") as file:
	datas = file.read().split("\n")
header = datas[0].split(",")
subjects = header[5:]
total_subjects = len(subjects) - 2

students = datas[1:]
students.pop()
total_students = len(students)
for i in range(total_students):
	students[i] = students[i].split(",")

num_of_take_exam = [0,0,0,0,0,0,0,0,0,0]
aver_students = [0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	total_grade = 0
	for i in range(5, len(s)):
		if i in [7,8]:
			continue
		if s[i] != "-1":
			count += 1
			total_grade += float(s[i])

	num_of_take_exam[count] += 1
	aver_students[count] += total_grade/count

for i in range(len(aver_students)):
	if num_of_take_exam[i] != 0:
		aver_students[i] = round(aver_students[i]/num_of_take_exam[i], 2)

print(aver_students)

import matplotlib.pyplot as plt
import numpy

fig, ax = plt.subplots()

x = numpy.arange(len(aver_students))
y = numpy.arange(len(aver_students))
num = ["0","1","2","3","4","5","6","7","8","9"]

plt.bar(y, aver_students)
plt.xticks(x, y)

# Set limit to vertical axis, đặt limit cho trục dọc (max = 100)
ax.set_ylim(0,10)

# label and title ~ nhãn, tiêu đề trục Ox, Oy
plt.xlabel('Số môn thi')
plt.ylabel('Điểm trung bình')
plt.title('Điểm trung bình theo số môn thi')

# Make some labels: student's number on top of each bar
rects = ax.patches
labels = aver_students
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.001, label, ha="center", va="bottom")

# show the plot - hiện lên biểu đồ
plt.show()