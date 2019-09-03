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
import math

num = 8

Dir_home = os.getcwd()
Dir_result = Dir_home + "/test/PM/io-test1"
sysbench_output = Dir_home + "/test/PM/txt"
IO_sysbench = sysbench_output + "/IO-sysbench-num.txt"

# --- 

def sysbenchFile(file_total_size='10G', fn=1, filename=IO_sysbench):

    totalsize = "--file-total-size=" + str(file_total_size) + "G"
    filenum = "--file-num=" + str(fn)
    os.chdir(Dir_result)
    devnull = open(os.devnull, "w")
    subprocess.call(["sysbench",
        "fileio", "--file-test-mode=rndrw", totalsize, filenum, "prepare"], stdout=devnull)
    devnull.close()

def runFile(file_total_size='10G', fn=1, filename=IO_sysbench, cpu=1):
    totalsize = "--file-total-size=" + str(file_total_size) + "G"
    filenum = "--file-num=" + str(fn)
    threads = "--threads=" + str(cpu)
    os.chdir(Dir_result)
    with open(filename, "a") as output:
        subprocess.call(["sysbench", "fileio", "--file-test-mode=rndrw", totalsize, filenum, threads, "run"], stdout=output)

def deleteFile():
    #threads = "--threads=" + str(cpu)
    devnull = open(os.devnull, "w")
    subprocess.call(["sysbench", "fileio", "cleanup"], stdout=devnull)
    devnull.close()
    os.chdir(Dir_result)

def appendLine(filename='', text=''):
    with open(filename, "a") as f:
        f.write(text)

def savecsv(filename='', starttime='', endtime=''):

    query = "q=SELECT \"wr_sec_per_s\", \"rd_sec_per_s\", \"tps\" FROM \"disk\" WHERE time >= '"+starttime+"' AND time <= '"+endtime+"'"
    #print query
    with open(filename, "a") as output:
        subprocess.call(["curl", "-H" "Accept: application/csv", "-G", 'http://localhost:8086/query?pretty=true', "--data-urlencode", "db=telegraf", "--data-urlencode", query], stdout=output)

def fileSysout(filename=''):

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
    num_size = 2
    file_num = 1
    #sysbenchFile(num_size, file_num, IO_sysbench)
    #print("File done.")
    #time.sleep(10)
    # File Test
    for i in range(num):
        #if((i%5)==0):
        file_num = pow(2,i)
        sysbenchFile(num_size, file_num, IO_sysbench)
        print("File create !!")

        #time.sleep(5)
        starttime = str(datetime.datetime.now())
        appendLine(IO_sysbench, "File Test " + str(i+1) + " Start: " + starttime + "\n")
        #n += 1
        #cpu = n
        print(file_num)
        print(num_size)
        runFile(num_size, file_num, IO_sysbench, 1)
        endtime = str(datetime.datetime.now())
        appendLine(IO_sysbench, "File Test " + str(i+1) + " End: " + endtime + "\n")
        print ("File Test:", (i + 1), "/", num, "done")
        
        #filenum = "/IO-thread" + str(cpu) + "-num_size"  + str(num_size)  +"G.csv"
        #csv = Dir_result + filenum
        #runtime = endtime - starttime
        #savecsv(csv,starttime,endtime)
        #deleteFile()
        #if((i+1)%5==0):
            #num_size += 100
            #n = 0
        deleteFile()
        print("File deleted !!")

    # print
    #deleteFile()
    fileSysout(IO_sysbench)


if __name__ == "__main__":
     main()
