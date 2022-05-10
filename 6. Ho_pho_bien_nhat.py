with open("data_cleaning.txt", "r", encoding="utf-8") as file:
	datas = file.read().split("\n")

students = datas[1:]
students.pop()
for i in range(len(students)):
	students[i] = students[i].split(",")

header = datas[0].split(",")
subjects = header[5:]

name = []
name_count = []

for s in students:
	s_name = s[1].split(" ")
	lastname = s_name[0]
	if lastname not in name:
		name.append(lastname)
		name_count.append(1)
	else:
		name_count[name.index(lastname)] += 1

counted_num = []
sorted_name = []

for i in range(len(name)):
	max_num = 0
	for j in range(len(name)):
		if name_count[j] > max_num:
			max_num = name_count[j]
	counted_num.append(max_num)
	sorted_name.append(name[name_count.index(max_num)])

	if max_num in name_count: 
		name.remove(name[name_count.index(max_num)])
		name_count.remove(max_num)

print(counted_num)
print(sorted_name)

import matplotlib.pyplot as plt
import numpy

fig, ax = plt.subplots()

num = 20
x = numpy.arange(20)
y = numpy.arange(20)

plt.bar(y, counted_num[0:num])
plt.xticks(x, sorted_name[0:num])
ax.set_ylim(0,25000)

plt.xlabel("Họ")
plt.ylabel("Số học sinh")
plt.title(str(num) + " họ phổ biến nhất trong kỳ thi")

rects = ax.patches
labels = counted_num
for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x()+rect.get_width()/2, height+0.1, label, ha="center", va="bottom")

plt.show()
