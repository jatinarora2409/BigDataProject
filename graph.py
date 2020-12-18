from matplotlib import pyplot as plt
import numpy as np
infile = open('tpcc_eval.log',"r")
tps = []
lat = []
group_epoch=1
count = 1
sum_tps = 0
sum_lat = 0
max_tps = []
min_lat = []
max_tps_value = 0
min_latency_value = 10000
output_file = open('output.txt', "w")

for line in infile:
    if '***********' in line:
            nextLine = next(infile)
            if '$$$$$$$$$$$$$$$$$$$$$$' not in nextLine:
                nextLine = nextLine.replace('[', '')
                nextLine = nextLine.replace(']', '')
                print(nextLine)
                tps_i,lat_i,_ = nextLine.split(',')

                if float(tps_i)>max_tps_value:
                    max_tps_value=float(tps_i)
                if float(lat_i)<min_latency_value:
                    min_latency_value=float(lat_i)



                sum_tps = sum_tps + float(tps_i)
                sum_lat = sum_lat + float(lat_i)
                count=count+1
                max_tps.append(max_tps_value)
                output_file.write(str(min_latency_value)+"\n")
                min_lat.append(min_latency_value)
                if(count%group_epoch==0):
                    tps.append(float(sum_tps)/group_epoch)
                    lat.append(float(sum_lat)/group_epoch)
                    sum_lat=0
                    sum_tps=0

output_file.close()
x=np.arange(0, (len(tps))*group_epoch,group_epoch)
x_max = np.arange(0,len(max_tps),1)

print(x)
print(tps)

plt.plot(x, tps)
plt.xlabel('Experiments ')
plt.ylabel('Throughput')
plt.show()
plt.plot(x, lat)
plt.xlabel('Experiments ')
plt.ylabel('Latency')
plt.show()


plt.plot(x_max, max_tps)
plt.xlabel('Steps ')
plt.ylabel('Max_Throughput')
plt.show()
plt.plot(x_max, min_lat)
plt.xlabel('Experiments ')
plt.ylabel('Min_Latency')
plt.show()

