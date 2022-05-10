
with open("data_cleaning.txt", "r", encoding = "utf-8") as file:
	datas = file.read().split("\n")

header = datas[0].split(",")
subjects = header[5:]

students = datas[1:]
students.pop()
for i in range(len(students)):
	students[i] = students[i].split(",")

age_students = ["17","18","19","20","21","22","23","24","25","26",">26"]
aver_students = [0,0,0,0,0,0,0,0,0,0,0]
num_students = [0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	age = 2020 - int(s[4])
	if age > 26:
		age = 27
	num_students[age - 17] += 1

	count = 0
	total_grade = 0
	for j in range(5, len(s)):
		if j in [7,8]:
			continue
		if s[j] != "-1":
			count += 1
			total_grade += float(s[j])

	aver_students[age-17] += total_grade/count

for i in range(len(age_students)):
	aver_students[i] = round(aver_students[i]/num_students[i], 2)


import matplotlib.pyplot as plt
import numpy
import pandas 

fig, ax = plt.subplots()
width = .8
plt.xlabel('Tuổi')
plt.title('Điểm trung bình theo độ tuổi')

# Tạo danh sách pandas các charts muốn vẽ
danh_sach = pandas.DataFrame({
 'normal' : num_students,
 'bad_rate' : aver_students})

	# 1. Draw barchart
danh_sach['normal'].plot(kind='bar', width = width)
plt.ylabel('Số học sinh')
plt.ylim(0,70000)

	# 2. Draw linechart
danh_sach['bad_rate'].plot(secondary_y=True, color='red', marker='o')
ax.tick_params(axis='y', colors='blue')
plt.ylabel('Điểm trung bình')
plt.ylim(0,10)

	# 3. Draw Ox axis
ax2 = plt.gca() 
plt.xlim([-width, len(danh_sach['normal'])])
ax2.set_xticklabels(("17","18","19","20","21","22","23","24","25","26",">26"))

# Make some labels on bars
rects = ax.patches
labels = num_students
for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width()/2, height+0.01, label, ha="center", va="bottom")

plt.show()

