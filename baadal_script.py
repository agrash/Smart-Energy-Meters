import os
import time

# the script reads the data from the csv from various pi's if they have arrived and then append the data in their respective location

while True:
	time.sleep(1500)

	try:
		file = open("chart.csv",'r')
		lines = file.readlines()
		lines = lines[:-1]	# to remove the empty cell at the last of the csv
		chart = open("./mysite/static/Block4/chart.csv",'a')
		for line in lines:
			chart.write(line)
		file.close()
		os.system("rm -r chart.csv")
	except IOError as e:
		print "file not found"

	try:
		file = open("chart7.csv",'r')
		lines = file.readlines()
		lines = lines[:-1]	
		chart = open("./mysite/static/Udaigiri/chart.csv",'a')
		for line in lines:
			chart.write(line)
		file.close()
		os.system("rm -r chart7.csv")
	except IOError as e:
		print "file not found7"

	try:
		file = open("chart4.csv",'r')
		lines = file.readlines()
		lines = lines[:-1]
		chart = open("./mysite/static/Girnar/chart.csv",'a')
		for line in lines:
			chart.write(line)
		file.close()
		os.system("rm -r chart4.csv")
	except IOError as e:
		print "file not found4"

	try:
		file = open("chart1.csv",'r')
		lines = file.readlines()
		lines = lines[:-1]
		chart = open("./mysite/static/Synergy/chart.csv",'a')
		for line in lines:
			chart.write(line)
		file.close()
		os.system("rm -r chart4.csv")
	except IOError as e:
		print "file not found4"

	try:
		file = open("chart5.csv",'r')
		lines = file.readlines()
		lines = lines[:-1]
		chart = open("./mysite/static/Block6/chart.csv",'a')
		for line in lines:
			chart.write(line)
		file.close()
		os.system("rm -r chart5.csv")
	except IOError as e:
		print "file not found5"

	try:
		file = open("chart6.csv",'r')
		lines = file.readlines()
		lines = lines[:-1]
		chart = open("./mysite/static/SIT/chart.csv",'a')
		for line in lines:
			chart.write(line)
		file.close()
		os.system("rm -r chart6.csv")
	except IOError as e:
		print "file not found6"

