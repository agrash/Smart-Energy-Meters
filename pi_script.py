import os
import binascii
import struct
import csv
import datetime
import time


meter_output = open('data.txt','r')
counter = 0
prev_answer = 0
os.system('sudo echo -ne "\\xE5\\x03\\x03\\xE8\\x00\\x0A\\x52\\x59" > /dev/ttyUSB0') # the string that need to be passed to the meter in order to obtain the readings is E5 03 03 E8 00 0A 52 59 which is a hexadecimal and the output returned by the meter is an ASCII string
while True:
	time.sleep(150) # sampling time
	os.system('sudo echo -ne "\\xE5\\x03\\x03\\xE8\\x00\\x0A\\x52\\x59" > /dev/ttyUSB0')
	content = meter_output.read()
	answer = binascii.hexlify(content).decode("ascii") # converting ASCII to hex
	print(answer)
	if len(answer) < 22:
		continue		#in order to prevent submission of the script due to erreneous output given by the meter.
	temp = answer[18]+answer[19]+answer[20]+answer[21]+answer[14]+answer[15]+answer[16]+answer[17] # the position in the hexadecimal which contains the information about the energy
	final_answer = struct.unpack('!f',temp.decode('hex'))[0]		# convert the hexadecimal form to float32 using ieee754 format
	if final_answer < 10000 or prev_answer > final_answer or final_answer > 10000000000:
		continue		# preventing erreneous outputs.
	prev_answer = final_answer
	data = [[datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),final_answer]] # storing timestamp along with the energy
	file = open('chart4.csv','a')
	writer = csv.writer(file)
	print data
	writer.writerows(data)
	file.close()
	counter += 1
	if counter == 10:		# sends the readings after 10 readings
		os.system("scp -r ~/chart4.csv baadalvm@10.17.50.24:~")
		os.system("rm -r chart4.csv")
		counter = 0
