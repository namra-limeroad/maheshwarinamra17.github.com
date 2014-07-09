

import  random
#while(1):
with  open('area_data','a') as myfile:
	a = random.randint(1,5000)
	txt = "{y:" + "'" +str(random.randint(2000,2999)) + " Q"+ str(random.randint(1,4))+ "'"  + ", item1:" + str(random.randint(1000,10000))  + ", item2:" + str(random.randint(1000,10000)) + "},\n"
# 	if(a>1 and a<100):
	myfile.write(txt)
