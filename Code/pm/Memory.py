#!/bin/bash/env Python3
# -*- coding: utf-8 -*-

import subprocess          
import multiprocessing      
import sys                  
import os                   
import errno                
import time                 
import datetime             


num = 8

threads = 1

Dir_home = os.getcwd()
Dir_result = Dir_home + "/PM/txt"
Memory_sysbench = Dir_result + "/Memory-sysbench.txt"

# Benchmark

def sysbenchMemory(mem_block_size='1K', mem_total_size='10G', filename=Memory_sysbench, cpu=1):

    blocksize = "--memory-block-size=" + mem_block_size
    totalsize = "--memory-total-size=" + mem_total_size
    threads = "--threads=" + str(cpu)
    with open(filename, "a") as output:
        subprocess.call(["sysbench", "--test=memory", blocksize, totalsize, threads, "run"], stdout=output)

def appendLine(filename='', text=''):
    with open(filename, "a") as f:
        f.write(text)

def fileoutput(filename=''):

    try:
        f = open(filename, 'r')
    except IOError:
        print("Error: File not found")
    else:
        with f:
            print(f.read())
    f.close()

def main():

    # Memory Test
    for i in range(num):
        print("Memory Test:", (i + 1), "/", num, "start")
        appendLine(Memory_sysbench, "Memory Test " + str(i+1) + " Start: " + str(datetime.datetime.now()) + "\n")
        sysbenchMemory('1K', '10G', Memory_sysbench, i+1)
        print("Memory Test:", (i + 1), "/", num, "done")
        appendLine(Memory_sysbench, "Memory Test " + str(i+1) + " End: " + str(datetime.datetime.now()) + "\n")
    
    # print

    fileoutput(Memory_sysbench)


if __name__ == "__main__":
     main()
