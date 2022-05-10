# Dùng python để chạy lệnh trên terminal
		subprocess.run('curl -F "SoBaoDanh=02004318" diemthi.hcm.edu.vn/Home/Show', shell=True)

# Cách lấy thông tin kết quả các sbd vào python: 
import subprocess
with open('rawdata.txt', 'w') as file:
	for sbd in range(2000001,2074719): # range(start,end)
		result = subprocess.check_output('curl -F "sobaodanh=0' + str(sbd) + '" diemthi.hcm.edu.vn/Home/Show')
		file.write(str(result) + "\n")