#!/bin/bash/env Python3
# -*- coding: utf-8 -*-


import subprocess           
import multiprocessing      
import sys                  
import os                   
import errno                
import time                 
import shutil               
import datetime             

num = 24

Dir_home = os.getcwd()
Dir_result = Dir_home + "/VM/io-test1/vm-io"
sysbench_output = Dir_home + "/VM/txt"
IO_sysbench = sysbench_output + "/IO-sysbench.txt"


def sysbenchFile(file_total_size='10G', filename=Dir_result):

    totalsize = "--file-total-size=" + str(file_total_size) + "G"
    os.chdir(filename)
    devnull = open(os.devnull, "w")
    subprocess.call(["sysbench",
        "--test=fileio", "--file-test-mode=rndrw", totalsize, "prepare"], stdout=devnull)
    devnull.close()

def runFile(file_total_size='10G', directory=Dir_result, filename=IO_sysbench, cpu=1):
    totalsize = "--file-total-size=" + str(file_total_size) + "G"
    threads = "--threads=" + str(cpu)
    os.chdir(directory)
    with open(filename, "a") as output:
        subprocess.call(["sysbench", "--test=fileio", "--file-test-mode=rndrw", totalsize, threads, "run"], stdout=output)

def deleteFile(directory=Dir_result):
    #threads = "--threads=" + str(cpu)
    os.chdir(directory)
    devnull = open(os.devnull, "w")
    subprocess.call(["sysbench","--test=fileio", "cleanup"], stdout=devnull)
    devnull.close()

def appendLine(filename='', text=''):
    with open(filename, "a") as f:
        f.write(text)

def savecsv(filename='', starttime='', endtime=''):

    query = "q=SELECT \"wr_sec_per_s\", \"rd_sec_per_s\", \"tps\" FROM \"disk\" WHERE time >= '"+starttime+"' AND time <= '"+endtime+"' tz('Europe/London')"
    #print query
    with open(filename, "a") as output:
        subprocess.call(["curl", "-H" "Accept: application/csv", "-G", 'http://localhost:8086/query?pretty=true', "--data-urlencode", "db=telegraf", "--data-urlencode", query], stdout=output)

def fileoutput(filename=''):

    try:
        f = open(filename, 'r')
    except IOError:
        print("Error: File not found to output.")
    else:
        with f:
            print(f.read())
    f.close()

def main():
    n = 0
    count = 1
    num_size = 10

    # File Test
    for i in range(num):
        result = Dir_home + "/VM/io-test1/vm-io" + str(count)
        if((i%8)==0):
            sysbenchFile(num_size, result)
            print("File create !!")

        time.sleep(5)
        starttime = str(datetime.datetime.now())
        appendLine(IO_sysbench, "File Test " + str(i+1) + " Start: " + starttime + "\n")
        n += 1
        cpu = n
        print(cpu)
        runFile(num_size, result, IO_sysbench, cpu)
        endtime = str(datetime.datetime.now())
        appendLine(IO_sysbench, "File Test " + str(i+1) + " End: " + endtime + "\n")
        print ("File Test:", (i + 1), "/", num, "done")
        filenum = "/IO-thread" + str(cpu) + "-num_size"  + str(num_size)  +"G.csv"
        csv = result + filenum
        #runtime = endtime - starttime
        savecsv(csv,starttime,endtime)
        if((i+1)%8==0):
            num_size += 10
            n = 0
            deleteFile(result)
            count += 1
            print("File deleted !!")

    # print
    #deleteFile()
    fileoutput(IO_sysbench)


if __name__ == "__main__":
     main()
