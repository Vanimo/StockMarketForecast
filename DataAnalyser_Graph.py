'''
Created on 10 May 2013

@author: Floris
'''
import IO
from time import strptime
import matplotlib.pyplot as plt

twitterFile = open("data/scrapeTest2.txt")
my_dict = dict()
for tweet in IO.readData_by_line(twitterFile):
    parts = tweet.strip().split('\t')
    time = strptime(parts[1][5:-6], "%d %B %Y %H:%M:%S")
    """02 May 2013 19:14:07
    time.struct_time(tm_year=2013, tm_mon=5, tm_mday=2, tm_hour=19, tm_min=14, tm_sec=7, tm_wday=3, tm_yday=122, tm_isdst=-1)
    """
    tag = str(time[0]) + "-" + str(time[1]) + "-" + str(time[2]) + "_" + str(time[3])
    if (tag in my_dict):
        my_dict[tag] += 1
    else:
        my_dict[tag] = 1
twitterFile.close()

keylist = my_dict.keys()
keylist.sort()
#initialize list
N_points = len(keylist) #per uur 
points_of_graph=[0]*N_points
i = 0

for key in keylist:
    points_of_graph[i] = my_dict[key]
    i += 1
plt.plot(range(N_points) ,points_of_graph)
plt.ylabel('Tweet volume')
plt.xlabel('Hour')
plt.show()
