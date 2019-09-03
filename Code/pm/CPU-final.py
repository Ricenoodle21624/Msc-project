#!/bin/bash/env Python3
# -*- coding: utf-8 -*-

import subprocess           
import multiprocessing      
import sys                 
import os                   
import errno               
import time                 
import datetime             

# number of tests
num = 24

thread = 1

Dir_home = os.getcwd()
Dir_result = Dir_home + "/PM/cpu-test1/pm-cpu"
sysbench_output = Dir_home + "/PM/txt"
CPU_sysbench = sysbench_output + "/Cpu-sysbench.txt"
#csv = Dir_result + "/CPU.csv"
# 

def sysbenchCPU(prime=30000000, filename=CPU_sysbench, cpu=1):
    prime = "--cpu-max-prime=" + str(prime)
    threads = "--num-threads=" + str(cpu)
    with open(filename, "a") as output:
        subprocess.call(["sysbench", "--test=cpu", prime, threads, "run"], stdout=output)

def appendLine(filename='', text=''):
    with open(filename, "a") as f:
        f.write(text)

def savecsv(filename='', starttime='', endtime=''):
    query = "q=SELECT \"cpu_usage\" FROM \"procstat\" WHERE \"exe\"='sysbench' AND time >= '"+starttime+"' AND time <= '"+endtime+"' tz('Europe/London')"
    print(query)
    with open(filename, "a") as output:
        subprocess.call(["curl", "-H" "Accept: application/csv", "-G", 'http://localhost:8086/query?pretty=true', "--data-urlencode", "db=telegraf", "--data-urlencode", query], stdout=output)


def filesoutput(filename=''):

    try:
        f = open(filename, 'r')
    except IOError:
        print("Error: File not found.")
    else:
        with f:
            print(f.read())
    f.close()

def main():
    
	n = 0
	count = 1
	num_prime = 100000
	for i in range(num):
         print("CPU Test:", (i + 1), "/", num, "start")
         #starttime = int(datetime.datetime.now().strftime("%M"))
         starttime = str(datetime.datetime.now())
         appendLine(CPU_sysbench, "CPU Test " + str(i+1) + " Start: " + starttime + "\n")
         n += 1
         cpu = n
         sysbenchCPU(num_prime, CPU_sysbench, cpu)
         #endtime = int(datetime.datetime.now().strftime("%M"))
         endtime = str(datetime.datetime.now())
         print("CPU Test:", (i + 1), "/", num, "done")
         appendLine(CPU_sysbench, "CPU Test " + str(i+1) + " End: " + endtime + "\n")
         filenum = "/CPU-thread" + str(cpu) +"-num_prime-" + str(num_prime) +".csv"
         Dir_result = Dir_home + "/PM/cpu-test1/pm-cpu" + str(count)
         csv = Dir_result + filenum
         #runtime = endtime - starttime
         savecsv(csv,starttime,endtime)
         if((i+1)%8 == 0):
            num_prime += 100000
            n = 0
            count += 1
            filesoutput(CPU_sysbench)

if __name__ == "__main__":
     main()
