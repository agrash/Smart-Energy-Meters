start1-start4 are the scripts that need to be run in the raspberry pi
pi_script is called by the script4
baadal_script is called in the baadal sever
mysite is the complete web framework of baadal

The name of the scripts may differ from what has been used inside the server as well as pi, so if you want you may delete the existing scripts and then execute them in their respective places and the architecture would work

The names of the variables used in mysite templates may also differ from that used in the baadal’s templates. So, I suggest putting the entire mysite in place of the existing mysite in the baadal sever.

Names used in the raspberry pi:
New name	Name inside the pi
start1.sh 	panda.sh
start2.sh	start1.sh
start3.sh	start2.sh
start4.sh	start3.sh
pi_script.py	test2.py

Names used in baadal:
New name		Name inside baadal
baadal_script.py	untitled.py

The pi’s are named from 1-7 and their respective ifconfig that goes to baadal after rebooting is ip<number_of_pi>