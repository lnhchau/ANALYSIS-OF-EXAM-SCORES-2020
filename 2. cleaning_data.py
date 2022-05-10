import csv

file = open("raw_data.txt", "r", encoding = "utf-8")
datas = file.read().split("\n")

with open("data_cleaning.txt", "w", encoding = "utf-8", newline = "") as csv_file:
	header = ["sbd", "tên", "dd", "mm", "yyyy", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
	writer = csv.writer(csv_file) 
	writer = writer.writerow(header) 

sbd = 2000000

for data in datas:
	sbd += 1
	sbd_str = "0" + str(sbd)
	data = data.split("\\n")
	begin = 0
	end = 0
	for i in range(len(data)):
		data[i] = data[i].replace("\\r", "") 
		data[i] = data[i].replace("\\t", "")

		tags = [] 
		for j in range(len(data[i])):
			if data[i][j] == "<":
				begin = j
			if data[i][j] == ">":
				end = j
				tags.append(data[i][begin : end+1])
		for tag in tags:
			data[i] = data[i].replace(tag, "")

		
	unempty_data = []
	for i in range(len(data)):
		data[i] = data[i].strip()
		if data[i] != "":
			unempty_data.append(data[i])
	data = unempty_data

	if(len(data) < 10):
		continue
	else: 
		data = [data[7], data[8], data[9]]

		with open("unicode (1).txt", "r", encoding = "utf-8") as file:
			utf8_to_unicode = file.read().split("\n")
			
		utf8_codes = []
		unicode_chars = []
		for line in utf8_to_unicode:
			line = line.split(" ")
			unicode_chars.append(line[0])
			utf8_codes.append(line[1])

		for i in range(len(data)):
			for j in range(len(utf8_to_unicode)):
				data[i] = data[i].replace(utf8_codes[j], unicode_chars[j])
			
		for i in range(len(data)):
			for j in range(len(data[i])):
				if data[i][j : j+2] == "&#" and data[i][j+2:j+5].isdigit() == True:
					data[i] = data[i][:j] + chr(int(data[i][j+2:j+5])) + data[i][j+6:]
				if data[i][j : j+2] == "&#" and data[i][j+2:j+5].isdigit() == False:
					data[i] = data[i][:j] + chr(int(data[i][j+2:j+4])) + data[i][j+5:]
			
		data[0] = data[0].lower()
		name = data[0].title()
			
		data[1] = data[1].lower()
		dob = data[1].split("/")
		dd = dob[0]
		mm = dob[1]
		yyyy = dob[2]
			
		data[2] = data[2].lower()
		data[2] = data[2].replace(":", "")
		data[2] = data[2].replace("khxh ", "khxh   ")
		data[2] = data[2].replace("khtn ", "khtn   ")
		data[2] = data[2].replace(" 10", "  10")
		scores = data[2].split("   ")
		
		data = [sbd_str, name, str(dd), str(mm), str(yyyy)]

		for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]:
			if subject in scores:
				data.append(str(float(scores[scores.index(subject)+1])))
			else: data.append("-1")
		
		with open("data_cleaning.txt", "a", encoding = "utf-8", newline = "") as csv_file:
			writer = csv.writer(csv_file)
			writer = writer.writerow(data)
