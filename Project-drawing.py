
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import itertools
import json
import pip
import jsonpath
import re
from datetime import datetime

if __name__ == '__main__':

    # # CPU Usage(Docker-VM-PM ) test

    # In[2]:

    num = 12
    test = 1
    n = 1
    num_prime = 100000
    n1 = 100000
    for i in range(num):
        df1 = pd.read_csv("MSC/Docker/cpu-test"+str(test)+"/Docker-cpu"+str(n)+"/dockerCPU.csv")
        df2 = pd.read_csv("MSC/VM/cpu-test"+str(test)+"/vm-cpu"+str(n)+"/vmCPU.csv")
        df3 = pd.read_csv("MSC/PM/cpu-test"+str(test)+"/pm-cpu"+str(n)+"/pmCPU.csv")
        x = []
        x1 = []
        x2 = []
        usage1 = (df1.loc[df1['threads'] == 1,'usage_percent']).values.tolist()
        usage2 = (df1.loc[df1['threads'] == 2,'usage_percent']).values.tolist()
        usage3 = (df1.loc[df1['threads'] == 3,'usage_percent']).values.tolist()
        usage4 = (df1.loc[df1['threads'] == 4,'usage_percent']).values.tolist()
        usage5 = (df1.loc[df1['threads'] == 5,'usage_percent']).values.tolist()
        usage6 = (df1.loc[df1['threads'] == 6,'usage_percent']).values.tolist()
        usage7 = (df1.loc[df1['threads'] == 7,'usage_percent']).values.tolist()
        usage8 = (df1.loc[df1['threads'] == 8,'usage_percent']).values.tolist()

        usage1.extend(usage2)
        usage1.extend(usage3)
        usage1.extend(usage4)
        usage1.extend(usage5)
        usage1.extend(usage6)
        usage1.extend(usage7)
        usage1.extend(usage8)
        #usage1 = list(map(float, usage1))
        #print(usage1)
        for i1 in range(0,len(usage1)):
             x.append(i1)


        usage9 = (df2.loc[df2['threads'] == 1,'cpu_usage']).values.tolist()
        usage10 = (df2.loc[df2['threads'] == 2,'cpu_usage']).values.tolist()
        usage11 = (df2.loc[df2['threads'] == 3,'cpu_usage']).values.tolist()
        usage12 = (df2.loc[df2['threads'] == 4,'cpu_usage']).values.tolist()
        usage13 = (df2.loc[df2['threads'] == 5,'cpu_usage']).values.tolist()
        usage14 = (df2.loc[df2['threads'] == 6,'cpu_usage']).values.tolist()
        usage15 = (df2.loc[df2['threads'] == 7,'cpu_usage']).values.tolist()
        usage16 = (df2.loc[df2['threads'] == 8,'cpu_usage']).values.tolist()
        usage9.extend(usage10)
        usage9.extend(usage11)
        usage9.extend(usage12)
        usage9.extend(usage13)
        usage9.extend(usage14)
        usage9.extend(usage15)
        usage9.extend(usage16)
        #print(usage9)
        for i2 in range(0,len(usage9)):
             x1.append(i2)

        usage17 = (df3.loc[df3['threads'] == 1,'cpu_usage']).values.tolist()
        usage18 = (df3.loc[df3['threads'] == 2,'cpu_usage']).values.tolist()
        usage19 = (df3.loc[df3['threads'] == 3,'cpu_usage']).values.tolist()
        usage20 = (df3.loc[df3['threads'] == 4,'cpu_usage']).values.tolist()
        usage21 = (df3.loc[df3['threads'] == 5,'cpu_usage']).values.tolist()
        usage22 = (df3.loc[df3['threads'] == 6,'cpu_usage']).values.tolist()
        usage23 = (df3.loc[df3['threads'] == 7,'cpu_usage']).values.tolist()
        usage24 = (df3.loc[df3['threads'] == 8,'cpu_usage']).values.tolist()
        usage17.extend(usage18)
        usage17.extend(usage19)
        usage17.extend(usage20)
        usage17.extend(usage21)
        usage17.extend(usage22)
        usage17.extend(usage23)
        usage17.extend(usage24)
        for i3 in range(0,len(usage17)):
             x2.append(i3)

        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.plot(x,usage1, color='b', label="Docker")
        plt.plot(x1,usage9, color='g', label="VM")
        plt.plot(x2,usage17, color='purple', label="PM")
        plt.legend(loc='upper left')
        plt.title('CPU Utilization-num_prime-'+str(num_prime))
        plt.xticks(rotation=68,fontsize=6)
        plt.xlabel("Time")
        plt.ylabel("usage(%)")

        #plt.savefig('MSC/CPU-image/CPU-usage/VM-Docker_plot'+str(i+1)+'.png')
        plt.savefig('MSC/CPU-image/CPU-usage/plot'+str(i+1)+'.png')
        plt.show()
        num_prime += n1
        n += 1
        if((i+1)%3 == 0):
            num_prime = n1
            test += 1
            n = 1
            if((i+1) == 6 or (i+1) == 9):
                n1 = 1000000
                num_prime = n1


    # # Docker-CPU test

    # In[24]:


    num = 12
    test = 1
    n = 1
    num_prime = 100000
    n1 = 100000
    for i in range(num):
        df1 = pd.read_csv("MSC/Docker/cpu-test"+str(test)+"/Docker-cpu"+str(n)+"/dockerCPU.csv")

        time1 = ((df1.loc[df1['threads'] == 1,'time']).values/1000000000).tolist()
        time2 = ((df1.loc[df1['threads'] == 2,'time']).values/1000000000).tolist()
        time3 = ((df1.loc[df1['threads'] == 3,'time']).values/1000000000).tolist()
        time4 = ((df1.loc[df1['threads'] == 4,'time']).values/1000000000).tolist()
        time5 = ((df1.loc[df1['threads'] == 5,'time']).values/1000000000).tolist()
        time6 = ((df1.loc[df1['threads'] == 6,'time']).values/1000000000).tolist()
        time7 = ((df1.loc[df1['threads'] == 7,'time']).values/1000000000).tolist()
        time8 = ((df1.loc[df1['threads'] == 8,'time']).values/1000000000).tolist()
        #print(i)

        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        for t in time1:
             a.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        #print(a)
        for t in time2:
             b.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time3:
             c.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time4:
             d.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time5:
             e.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time6:
             f.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time7:
             g.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time8:
             h.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))

        usage1 = (df1.loc[df1['threads'] == 1,'usage_percent']).values
        usage2 = (df1.loc[df1['threads'] == 2,'usage_percent']).values
        usage3 = (df1.loc[df1['threads'] == 3,'usage_percent']).values
        usage4 = (df1.loc[df1['threads'] == 4,'usage_percent']).values
        usage5 = (df1.loc[df1['threads'] == 5,'usage_percent']).values
        usage6 = (df1.loc[df1['threads'] == 6,'usage_percent']).values
        usage7 = (df1.loc[df1['threads'] == 7,'usage_percent']).values
        usage8 = (df1.loc[df1['threads'] == 8,'usage_percent']).values

        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.bar(a,usage1, color='b', label="thread1")
        plt.bar(b,usage2, color='g', label="thread2")
        plt.bar(c,usage3, color='r', label="thread3")
        plt.bar(d,usage4, color='k', label="thread4")
        plt.bar(e,usage5, color='purple', label="thread5")
        plt.bar(f,usage6, color='yellow', label="thread6")
        plt.bar(g,usage7, color='pink', label="thread7")
        plt.bar(h,usage8, color='silver', label="thread8")
        plt.legend(loc='upper left')
        plt.title('Docker-CPU usage-num_prime-'+str(num_prime))
        plt.xticks(rotation=68,fontsize=6)
        plt.xlabel("Time")
        plt.ylabel("usage")

        plt.savefig('MSC/Docker/image/plot'+str(i+1)+'.png')
        plt.show()
        num_prime += n1
        n += 1
        if((i+1)%3 == 0):
            num_prime = n1
            test += 1
            n = 1
            if((i+1) == 6 or (i+1) == 9):
                n1 = 1000000
                num_prime = n1


    # # VM-CPU test

    # In[2]:


    num = 12
    test = 1
    n = 1
    num_prime = 100000
    n1 = 100000
    for i in range(num):
        df1 = pd.read_csv("MSC/VM/cpu-test"+str(test)+"/vm-cpu"+str(n)+"/vmCPU.csv")

        time1 = ((df1.loc[df1['threads'] == 1,'time']).values/1000000000).tolist()
        time2 = ((df1.loc[df1['threads'] == 2,'time']).values/1000000000).tolist()
        time3 = ((df1.loc[df1['threads'] == 3,'time']).values/1000000000).tolist()
        time4 = ((df1.loc[df1['threads'] == 4,'time']).values/1000000000).tolist()
        time5 = ((df1.loc[df1['threads'] == 5,'time']).values/1000000000).tolist()
        time6 = ((df1.loc[df1['threads'] == 6,'time']).values/1000000000).tolist()
        time7 = ((df1.loc[df1['threads'] == 7,'time']).values/1000000000).tolist()
        time8 = ((df1.loc[df1['threads'] == 8,'time']).values/1000000000).tolist()
        #print(i)

        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        for t in time1:
             a.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        #print(a)
        for t in time2:
             b.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time3:
             c.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time4:
             d.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time5:
             e.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time6:
             f.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time7:
             g.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time8:
             h.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))

        usage1 = (df1.loc[df1['threads'] == 1,'cpu_usage']).values
        usage2 = (df1.loc[df1['threads'] == 2,'cpu_usage']).values
        usage3 = (df1.loc[df1['threads'] == 3,'cpu_usage']).values
        usage4 = (df1.loc[df1['threads'] == 4,'cpu_usage']).values
        usage5 = (df1.loc[df1['threads'] == 5,'cpu_usage']).values
        usage6 = (df1.loc[df1['threads'] == 6,'cpu_usage']).values
        usage7 = (df1.loc[df1['threads'] == 7,'cpu_usage']).values
        usage8 = (df1.loc[df1['threads'] == 8,'cpu_usage']).values

        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.bar(a,usage1, color='b', label="thread1")
        plt.bar(b,usage2, color='g', label="thread2")
        plt.bar(c,usage3, color='r', label="thread3")
        plt.bar(d,usage4, color='k', label="thread4")
        plt.bar(e,usage5, color='purple', label="thread5")
        plt.bar(f,usage6, color='yellow', label="thread6")
        plt.bar(g,usage7, color='pink', label="thread7")
        plt.bar(h,usage8, color='silver', label="thread8")
        plt.legend(loc='upper left')
        plt.title('VM-CPU usage-num_prime-'+str(num_prime))
        plt.xticks(rotation=68,fontsize=6)
        plt.xlabel("Time")
        plt.ylabel("usage")

        plt.savefig('MSC/VM/image/plot'+str(i+1)+'.png')
        plt.show()
        num_prime += n1
        n += 1
        if((i+1)%3 == 0):
            num_prime = n1
            test += 1
            n = 1
            if((i+1) == 6 or (i+1) == 9):
                n1 = 1000000
                num_prime = n1


    # # PM-CPU test

    # In[40]:


    num = 12
    test = 1
    n = 1
    num_prime = 100000
    n1 = 100000
    for i in range(num):
        df1 = pd.read_csv("MSC/PM/cpu-test"+str(test)+"/pm-cpu"+str(n)+"/pmCPU.csv")

        time1 = ((df1.loc[df1['threads'] == 1,'time']).values/1000000000).tolist()
        time2 = ((df1.loc[df1['threads'] == 2,'time']).values/1000000000).tolist()
        time3 = ((df1.loc[df1['threads'] == 3,'time']).values/1000000000).tolist()
        time4 = ((df1.loc[df1['threads'] == 4,'time']).values/1000000000).tolist()
        time5 = ((df1.loc[df1['threads'] == 5,'time']).values/1000000000).tolist()
        time6 = ((df1.loc[df1['threads'] == 6,'time']).values/1000000000).tolist()
        time7 = ((df1.loc[df1['threads'] == 7,'time']).values/1000000000).tolist()
        time8 = ((df1.loc[df1['threads'] == 8,'time']).values/1000000000).tolist()
        #print(i)

        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        for t in time1:
             a.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        #print(a)
        for t in time2:
             b.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time3:
             c.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time4:
             d.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time5:
             e.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time6:
             f.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time7:
             g.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))
        for t in time8:
             h.append(str(datetime.fromtimestamp(t).strftime("%H:%M:%S")))

        usage1 = (df1.loc[df1['threads'] == 1,'cpu_usage']).values
        usage2 = (df1.loc[df1['threads'] == 2,'cpu_usage']).values
        usage3 = (df1.loc[df1['threads'] == 3,'cpu_usage']).values
        usage4 = (df1.loc[df1['threads'] == 4,'cpu_usage']).values
        usage5 = (df1.loc[df1['threads'] == 5,'cpu_usage']).values
        usage6 = (df1.loc[df1['threads'] == 6,'cpu_usage']).values
        usage7 = (df1.loc[df1['threads'] == 7,'cpu_usage']).values
        usage8 = (df1.loc[df1['threads'] == 8,'cpu_usage']).values

        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.bar(a,usage1, color='b', label="thread1")
        plt.bar(b,usage2, color='g', label="thread2")
        plt.bar(c,usage3, color='r', label="thread3")
        plt.bar(d,usage4, color='k', label="thread4")
        plt.bar(e,usage5, color='purple', label="thread5")
        plt.bar(f,usage6, color='yellow', label="thread6")
        plt.bar(g,usage7, color='pink', label="thread7")
        plt.bar(h,usage8, color='silver', label="thread8")
        plt.legend(loc='upper left')
        plt.title('PM-CPU usage-num_prime-'+str(num_prime))
        plt.xticks(rotation=68,fontsize=6)
        plt.xlabel("Time")
        plt.ylabel("usage")

        plt.savefig('MSC/PM/image/plot'+str(i+1)+'.png')
        plt.show()
        num_prime += n1
        n += 1
        if((i+1)%3 == 0):
            num_prime = n1
            test += 1
            n = 1
            if((i+1) == 6 or (i+1) == 9):
                n1 = 1000000
                num_prime = n1


    # # CPU-thread-execution time

    # In[3]:


    num = 4
    pm_exe_time = []
    vm_exe_time = []
    c_exe_time = []
    for i in range(num):
        with open("MSC/PM/txt/Cpu-sysbench"+ str(i+1) +".txt") as f:

            lines = f.readlines()
            #pm_exe_time = []
            for line in lines:
                m2 = re.match("(    execution time )\((.*)\)\:\s*(\d*\.\d*)", line)
                m1 = re.search("execution time ", line)
                if m2:
                    #print(m2.group(3))
                    pm_exe_time.append(float(m2.group(3)))

        with open("MSC/VM/txt/Cpu-sysbench"+ str(i+1) +".txt") as f:

            lines = f.readlines()
            #vm_exe_time = []
            for line in lines:
                m2 = re.match("(    execution time )\((.*)\)\:\s*(\d*\.\d*)", line)
                m1 = re.search("execution time ", line)
                if m2:
                    #print(m2.group(3))
                    vm_exe_time.append(float(m2.group(3)))

        with open("MSC/Docker/txt/Cpu-sysbench"+ str(i+1) +".txt") as f:

            lines = f.readlines()
            #c_exe_time = []
            for line in lines:
                m2 = re.match("(    execution time )\((.*)\)\:\s*(\d*\.\d*)", line)
                m1 = re.search("execution time ", line)
                if m2:
                    #print(m2.group(3))
                    c_exe_time.append(float(m2.group(3)))
    #print(pm_exe_time[72:80])
    num = 48
    count = 0
    i = 0
    i1 = 24
    i2 = 48
    i3 = 72
    num_prime = 100000
    x = ['1','2','3','4','5','6','7','8']
    while i < 24:
        plt.plot(x,pm_exe_time[i:(i+8)], color='b', label="PM1")
        plt.plot(x,pm_exe_time[i1:(i1+8)], color='g', label="PM2")
        plt.plot(x,vm_exe_time[i:(i+8)], color='purple', label="VM1")
        plt.plot(x,vm_exe_time[i1:(i1+8)], color='yellow', label="VM2")
        plt.plot(x,c_exe_time[i:(i+8)], color='pink', label="Docker1")
        plt.plot(x,c_exe_time[i1:(i1+8)], color='silver', label="Docker2")

        i += 8
        i1 += 8
        count += 1

        plt.legend(loc='best')
        plt.title('Prime_num-'+ str(num_prime) +'-CPU_thread_avg-Execution_time')
        plt.xlabel("Thread")
        plt.ylabel("Time/s")
        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.savefig('MSC/CPU-image/execution-time/plot'+str(count)+'.png')
        plt.show()
        if((i)%8 == 0):
            num_prime += 100000

    num_prime = 1000000
    count = 3
    while i2 < 72:
        plt.plot(x,pm_exe_time[i2:(i2+8)], color='r', label="PM3")
        plt.plot(x,pm_exe_time[i3:(i3+8)], color='k', label="PM4")
        plt.plot(x,vm_exe_time[i2:(i2+8)], color='peru', label="VM3")
        plt.plot(x,vm_exe_time[i3:(i3+8)], color='orange', label="VM4")
        plt.plot(x,c_exe_time[i2:(i2+8)], color='teal', label="Docker3")
        plt.plot(x,c_exe_time[i3:(i3+8)], color='gold', label="Docker4")

        i2 += 8
        i3 += 8
        count += 1
        plt.legend(loc='best')
        plt.title('Prime_num-'+ str(num_prime) +'-CPU_thread_avg-Execution_time')
        plt.xlabel("Thread")
        plt.ylabel("Time/s")
        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.savefig('MSC/CPU-image/execution-time/plot'+str(count)+'.png')
        plt.show()
        if((i2)%8 == 0):
            num_prime += 1000000



    # # CPU- total time, speed, Latency-avg, Latency-sum

    # In[4]:


    num = 16
    n = 0
    n1 = 1
    match = ["(    total time)\:\s*(\d*\.\d*)","(    events per second)\:\s*(\d*\.\d*)","(         avg)\:\s*(\d*\.\d*)","(         sum)\:\s*(\d*\.\d*)"]
    title = ['-CPU_total_time','-CPU-speed_events-per-second','-CPU-Latency-avg','-CPU-Latency-sum']
    file_name = ['total-time','cpu-speed','Latency-avg','Latency-sum']
    ordinate = ['Time(s)','events/s','Time(ms)','Time(ms)']
    pm_data = []
    vm_data = []
    c_data = []
    for ii in range(num):
        with open("MSC/PM/txt/Cpu-sysbench"+ str(n1) +".txt") as f:

            lines = f.readlines()
            #pm_exe_time = []
            for line in lines:
                m2 = re.match(match[n], line)
                if m2:
                    #print(m2.group(3))
                    pm_data.append(float(m2.group(2)))

        with open("MSC/VM/txt/Cpu-sysbench"+ str(n1) +".txt") as f:

            lines = f.readlines()
            #vm_exe_time = []
            for line in lines:
                m2 = re.match(match[n], line)
                if m2:
                    #print(m2.group(3))
                    vm_data.append(float(m2.group(2)))

        with open("MSC/Docker/txt/Cpu-sysbench"+ str(n1) +".txt") as f:

            lines = f.readlines()
            #c_exe_time = []
            for line in lines:
                m2 = re.match(match[n], line)
                if m2:
                    #print(m2.group(3))
                    c_data.append(float(m2.group(2)))
        n1 += 1
        if((ii+1)%4 == 0):

            n1 = 1
            num = 48
            i = 0
            i1 = 24
            i2 = 48
            i3 = 72
            count = 0
            num_prime = 100000
            x = ['1','2','3','4','5','6','7','8']
            while i < 24:
                plt.plot(x,pm_data[i:(i+8)], color='b', label="PM1")
                plt.plot(x,pm_data[i1:(i1+8)], color='g', label="PM2")
                plt.plot(x,vm_data[i:(i+8)], color='purple', label="VM1")
                plt.plot(x,vm_data[i1:(i1+8)], color='yellow', label="VM2")
                plt.plot(x,c_data[i:(i+8)], color='pink', label="Docker1")
                plt.plot(x,c_data[i1:(i1+8)], color='silver', label="Docker2")

                i += 8
                i1 += 8
                count += 1

                plt.legend(loc='best')
                plt.title('Prime_num-'+ str(num_prime) +'-'+file_name[n])
                plt.xlabel("Thread")
                plt.ylabel(ordinate[n])
                plt.rcParams['figure.figsize'] = (6.0, 4.0)
                plt.rcParams['figure.dpi'] = 100
                plt.rcParams['savefig.dpi'] = 100
                plt.savefig('MSC/CPU-image/'+ file_name[n] +'/plot'+str(count)+'.png')
                plt.show()
                if((i)%8 == 0):
                    num_prime += 100000

            num_prime = 1000000
            count = 3
            while i2 < 72:
                plt.plot(x,pm_data[i2:(i2+8)], color='r', label="PM3")
                plt.plot(x,pm_data[i3:(i3+8)], color='k', label="PM4")
                plt.plot(x,vm_data[i2:(i2+8)], color='peru', label="VM3")
                plt.plot(x,vm_data[i3:(i3+8)], color='orange', label="VM4")
                plt.plot(x,c_data[i2:(i2+8)], color='teal', label="Docker3")
                plt.plot(x,c_data[i3:(i3+8)], color='gold', label="Docker4")

                i2 += 8
                i3 += 8
                count += 1

                plt.legend(loc='best')
                plt.title('Prime_num-'+ str(num_prime) +'-'+file_name[n])
                plt.xlabel("Thread")
                plt.ylabel(ordinate[n])
                plt.rcParams['figure.figsize'] = (6.0, 4.0)
                plt.rcParams['figure.dpi'] = 100
                plt.rcParams['savefig.dpi'] = 100
                plt.savefig('MSC/CPU-image/'+ file_name[n] +'/plot'+str(count)+'.png')
                plt.show()
                if((i2)%8 == 0):
                    num_prime += 1000000
            n += 1
            pm_data = []
            vm_data = []
            c_data = []



    # # AVG-CPU- total time, speed, Latency-avg, Latency-sum

    # In[7]:


    num = 16
    n = 0
    n1 = 1
    match = ["(    total time)\:\s*(\d*\.\d*)","(    events per second)\:\s*(\d*\.\d*)","(         avg)\:\s*(\d*\.\d*)","(         sum)\:\s*(\d*\.\d*)"]
    title = ['-CPU_total_time','-CPU-speed_events-per-second','-CPU-Latency-avg','-CPU-Latency-sum']
    file_name = ['total-time','cpu-speed','Latency-avg','Latency-sum']
    ordinate = ['Time(s)','events/s','Time(ms)','Time(ms)']
    pm_data = []
    vm_data = []
    c_data = []
    for ii in range(num):
        with open("MSC/PM/txt/Cpu-sysbench"+ str(n1) +".txt") as f:

            lines = f.readlines()
            #pm_exe_time = []
            for line in lines:
                m2 = re.match(match[n], line)
                if m2:
                    #print(m2.group(3))
                    pm_data.append(float(m2.group(2)))

        with open("MSC/VM/txt/Cpu-sysbench"+ str(n1) +".txt") as f:

            lines = f.readlines()
            #vm_exe_time = []
            for line in lines:
                m2 = re.match(match[n], line)
                if m2:
                    #print(m2.group(3))
                    vm_data.append(float(m2.group(2)))

        with open("MSC/Docker/txt/Cpu-sysbench"+ str(n1) +".txt") as f:

            lines = f.readlines()
            #c_exe_time = []
            for line in lines:
                m2 = re.match(match[n], line)
                if m2:
                    #print(m2.group(3))
                    c_data.append(float(m2.group(2)))
        n1 += 1
        if((ii+1)%4 == 0):

            n1 = 1
            #print(pm_exe_time[72:80])
            num = 48
            i = 0
            i2 = 0
            count = 0
            num_prime = 100000
            x = ['1','2','3','4','5','6','7','8']

            pm1 = [(pm_data[i] + pm_data[i+24])/2 for i in range(0,24)]
            vm1 = [(vm_data[i] + vm_data[i+24])/2 for i in range(0,24)]
            c1 = [(c_data[i] + c_data[i+24])/2 for i in range(0,24)]
            pm2 = [(pm_data[i] + pm_data[i+24])/2 for i in range(48,72)]
            vm2 = [(vm_data[i] + vm_data[i+24])/2 for i in range(48,72)]
            c2 = [(c_data[i] + c_data[i+24])/2 for i in range(48,72)]


            while i < 24:
                plt.plot(x,pm1[i:(i+8)], color='b', label="PM-avg")
                plt.plot(x,vm1[i:(i+8)], color='purple', label="VM-avg")
                plt.plot(x,c1[i:(i+8)], color='pink', label="Docker-avg")

                i += 8
                count += 1

                plt.legend(loc='best')
                plt.title('AVG-Prime_num-'+ str(num_prime) + title[n])
                plt.xlabel("Thread")
                plt.ylabel(ordinate[n])
                plt.rcParams['figure.figsize'] = (6.0, 4.0)
                plt.rcParams['figure.dpi'] = 100
                plt.rcParams['savefig.dpi'] = 100
                plt.savefig('MSC/CPU-image/'+ file_name[n] +'/avg-plot'+str(count)+'.png')
                plt.show()
                if((i)%8 == 0):
                    num_prime += 100000

            num_prime = 1000000
            count = 3
            while i2 < 24:
                plt.plot(x,pm2[i2:(i2+8)], color='r', label="PM-avg")
                plt.plot(x,vm2[i2:(i2+8)], color='peru', label="VM-avg")
                plt.plot(x,c2[i2:(i2+8)], color='teal', label="Docker-avg")

                i2 += 8
                count += 1

                plt.legend(loc='best')
                plt.title('AVG-Prime_num-'+ str(num_prime) + title[n])
                plt.xlabel("Thread")
                plt.ylabel(ordinate[n])
                plt.rcParams['figure.figsize'] = (6.0, 4.0)
                plt.rcParams['figure.dpi'] = 100
                plt.rcParams['savefig.dpi'] = 100
                plt.savefig('MSC/CPU-image/'+ file_name[n] +'/avg-plot'+str(count)+'.png')
                plt.show()
                if((i2)%8 == 0):
                    num_prime += 1000000
            n += 1
            pm_data = []
            vm_data = []
            c_data = []



    # # IO

    # In[5]:


    num = 3
    n = 1
    num_size = 10
    n1 = 10
    for i in range(num):
        df1 = pd.read_csv("MSC/Docker/io-test1/Docker-io"+str(n)+"/dockerio.csv")
        df2 = pd.read_csv("MSC/VM/io-test1/vm-io"+str(n)+"/vmio.csv")
        df3 = pd.read_csv("MSC/PM/io-test1/pm-io"+str(n)+"/pmio.csv")
        x = []
        x1 = []
        x2 = []
        x3 = []
        x4 = []
        x5 = []
        wkb_s1 = (df1.iloc[:,3].values/2).tolist()
        wkb_s2 = (df2.iloc[:,3].values/2).tolist()
        wkb_s3 = (df3.iloc[:,3].values).tolist()

        while 0.0 in wkb_s1:
            wkb_s1.remove(0.0)
        while 0.0 in wkb_s2:
            wkb_s2.remove(0.0)
        while 0.0 in wkb_s3:
            wkb_s3.remove(0.0)
        #print (wkb_s2)

        for i1 in range(0,len(wkb_s1)):
             x.append(i1)

        for i2 in range(0,len(wkb_s2)):
             x1.append(i2)

        for i3 in range(0,len(wkb_s3)):
             x2.append(i3)

        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.plot(x,wkb_s1, color='b', label="Docker")
        plt.plot(x1,wkb_s2, color='g', label="VM")
        plt.plot(x2,wkb_s3, color='purple', label="PM")
        plt.legend(loc='upper left')
        plt.title('IO wkB_per_s-num_size-'+str(num_size)+'G')
        plt.xticks(rotation=68,fontsize=6)
        plt.xlabel("Time")
        plt.ylabel("wkB_per_s")
        plt.savefig('MSC/IO-image/IO-wkB_per_s/plot'+str(i+1)+'.png')
        plt.show()

        num_size += 10
        n += 1
        if((i+1)%3 == 0):
            n = 1


    # In[6]:


    with open("MSC/VM/txt/IO-sysbench.txt") as f:

        lines = f.readlines()
        vm_exe_time = []
        vm_write = []
        vm_read = []
        vm_tps = []
        x = ['1','2','3','4','5','6','7','8']
        for line in lines:
            m2 = re.match("(    total time)\:\s*(\d*\.\d*)", line)
            m1 = re.match("(    writes/s)\:\s*(\d*\.\d*)", line)
            m3 = re.match("(    reads/s)\:\s*(\d*\.\d*)", line)

            if m1:
                #print(m2.group(3))
                vm_write.append(float(m1.group(2)))
            if m2:
                #print(m2.group(3))
                vm_exe_time.append(float(m2.group(2)))
            if m3:
                #print(m3.group(2))
                vm_read.append(float(m3.group(2)))

        with open("MSC/Docker/txt/IO-sysbench.txt") as f:

            lines = f.readlines()
            c_exe_time = []
            c_write = []
            c_read = []
            c_tps = []
            x = ['1','2','3','4','5','6','7','8']
            for line in lines:
                m2 = re.match("(    total time)\:\s*(\d*\.\d*)", line)
                m1 = re.match("(    writes/s)\:\s*(\d*\.\d*)", line)
                m3 = re.match("(    reads/s)\:\s*(\d*\.\d*)", line)
                if m1:
                    #print(m2.group(3))
                    c_write.append(float(m1.group(2)))
                if m2:
                    #print(m2.group(3))
                    c_exe_time.append(float(m2.group(2)))
                if m3:
                    #print(m3.group(2))
                    c_read.append(float(m3.group(2)))

        with open("MSC/PM/txt/IO-sysbench.txt") as f:

            lines = f.readlines()
            pm_exe_time = []
            pm_write = []
            pm_read = []
            pm_tps = []
            x = ['1','2','3','4','5','6','7','8']
            for line in lines:
                m2 = re.match("(    total time)\:\s*(\d*\.\d*)", line)
                m1 = re.match("(    writes/s)\:\s*(\d*\.\d*)", line)
                m3 = re.match("(    reads/s)\:\s*(\d*\.\d*)", line)
                if m1:
                    #print(m1.group(2))
                    pm_write.append(float(m1.group(2)))
                if m2:
                    #print(m2.group(3))
                    pm_exe_time.append(float(m2.group(2)))
                if m3:
                    #print(m3.group(2))
                    pm_read.append(float(m3.group(2)))

        i = 0
        count = 0
        num_size = 10
        while i < 24:

                fig = plt.figure()
                plot1 = fig.add_subplot(2,2,1)
                plot2 = fig.add_subplot(2,2,4)
                plot1.plot(x,c_read[i:(i+8)], color='b', label="Container")
                plot2.plot(x,c_write[i:(i+8)], color='b', label="Container")
                plot1.plot(x,vm_read[i:(i+8)], color='g', label="VM")
                plot2.plot(x,vm_write[i:(i+8)], color='g', label="VM")
                plot1.plot(x,pm_read[i:(i+8)], color='purple', label="PM")
                plot2.plot(x,pm_write[i:(i+8)], color='purple', label="PM")
                i += 8
                count += 1

                plot1.legend(loc='best')
                plot1.set_title('IOPS-Read_operations-num_size-'+ str(num_size)+'G')
                plot1.set_xlabel("Thread")
                plot1.set_ylabel("reads/s")

                plot2.legend(loc='best')
                plot2.set_title('IOPS-Write_operations-num_size-'+ str(num_size)+'G')
                plot2.set_xlabel("Thread")
                plot2.set_ylabel("writes/s")

                plt.rcParams['figure.figsize'] = (6.0, 4.0)
                plt.rcParams['figure.dpi'] = 100
                plt.rcParams['savefig.dpi'] = 100
                plt.savefig('MSC/IO-image/IOPS/plot'+str(count)+'.png')
                plt.show()
                if((i)%8 == 0):
                    num_size += 10


    # In[6]:


    with open("MSC/Docker/txt/IO-sysbench-num.txt") as f:

        lines = f.readlines()

        write = []
        read = []

        x = ['1','2','4','8','16','32','64','128']
        for line in lines:
            m2 = re.match("(    read, MiB/s)\:\s*(\d*\.\d*)", line)
            m1 = re.match("(    written, MiB/s)\:\s*(\d*\.\d*)", line)

            if m1:
                #print(m2.group(3))
                write.append(float(m1.group(2)))
            if m2:
                #print(m2.group(3))
                read.append(float(m2.group(2)))


        plt.plot(x,write, color='b', label="Write")

        plt.plot(x,read, color='g', label="Read")

        plt.legend(loc='best')
        plt.title('Throughput')
        plt.xlabel("File Number")
        plt.ylabel("MiB/s")
        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.savefig('MSC/IO-image/IO_num-plot.png')
        plt.show()


    # # Memory

    # In[5]:


    with open("MSC/VM/txt/vm-Memory-sysbench.txt") as f:

        lines = f.readlines()
        vm_exe_time = []
        vm_bandwidth = []
        x = ['1','2','3','4','5','6','7','8']
        for line in lines:
            m2 = re.match("(    total time)\:\s*(\d*\.\d*)", line)
            m1 = re.search("execution time ", line)
            m3 = re.match("(10240.00 MiB transferred )\((\d*)(.*)\)", line)
            if m2:
                #print(m2.group(3))
                vm_exe_time.append(float(m2.group(2)))
            if m3:
                #print(m3.group(2))
                vm_bandwidth.append(float(m3.group(2)))

        with open("MSC/Docker/txt/docker-Memory-sysbench.txt") as f:

            lines = f.readlines()
            c_exe_time = []
            c_bandwidth = []
            x = ['1','2','3','4','5','6','7','8']
            for line in lines:
                m2 = re.match("(    total time)\:\s*(\d*\.\d*)", line)
                m1 = re.search("execution time ", line)
                m3 = re.match("(10240.00 MiB transferred )\((\d*)(.*)\)", line)
                if m2:
                    #print(m2.group(3))
                    c_exe_time.append(float(m2.group(2)))
                if m3:
                    #print(m3.group(2))
                    c_bandwidth.append(float(m3.group(2)))

        with open("MSC/PM/txt/pm-Memory-sysbench.txt") as f:

            lines = f.readlines()
            pm_exe_time = []
            pm_bandwidth = []
            x = ['1','2','3','4','5','6','7','8']
            for line in lines:
                m2 = re.match("(    total time)\:\s*(\d*\.\d*)", line)
                m1 = re.search("execution time ", line)
                m3 = re.match("(10240.00 MiB transferred )\((\d*)(.*)\)", line)
                if m2:
                    #print(m2.group(3))
                    pm_exe_time.append(float(m2.group(2)))
                if m3:
                    #print(m3.group(2))
                    pm_bandwidth.append(float(m3.group(2)))




        plt.plot(x,c_bandwidth, color='b', label="Container")
        plt.plot(x,vm_bandwidth, color='g', label="VM")
        plt.plot(x,pm_bandwidth, color='purple', label="PM")


        plt.legend(loc='best')
        plt.title('Bandwidth')
        plt.xlabel("Thread")
        plt.ylabel("Bandwidth MiB/sec")
        plt.rcParams['figure.figsize'] = (6.0, 4.0)
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 100
        plt.savefig('MSC/Memory-image/Memory-plot.png')
        plt.show()

