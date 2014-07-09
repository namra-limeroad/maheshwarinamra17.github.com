

import  random, threading

#while(1):
with  open('bar_data','a') as myfile:
	a = random.randint(1,5000)
	txt = "{y:" + str(random.randint(2000,2999))  + ", a:" + str(random.randint(1,100))  + ", b:" + str(random.randint(1,100)) + "},\n"
#	if(a>10 and a<100):
	myfile.write(txt)
