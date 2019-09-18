import time
from time import sleep


start_time = time.clock()
print("Start Time :" , round(start_time))
sleep(2)
end_time = time.clock()
print("End Time :", round(end_time))
exec_time = end_time-start_time
print ("Execution Time:", round(exec_time))

sleep(2)
mytime = round(time.clock())
print (("SecondTc Execution Time :", round(mytime + exec_time) ))

