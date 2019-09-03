#!/bin/bash/env Python3
# -*- coding: utf-8 -*-

import subprocess          
import multiprocessing      
import sys                  
import os                   
import errno                
import time                 
import datetime             

test = 3
num = 4
image = 6
environment = ['Docker','VM','PM']
cpu_image = ['CPU-usage', 'Latency-sum', 'Latency-avg', 'cpu-speed', 'total-time', 'execution-time']
def main():
    
    os.makedirs('test/CPU-image')
    os.makedirs('test/IO-image/IOPS')
    os.makedirs('test/IO-image/IO-wkB_per_s')
    os.makedirs('test/Memory-image')
    for n in range(test):
        os.makedirs('test/'+environment[n]+'/image')
        os.makedirs('test/'+environment[n]+'/txt')
        os.makedirs('test/'+environment[n]+'/io-test1')  

    for i in range(num):
        os.makedirs('test/Docker/cpu-test'+str(i+1))
        os.makedirs('test/VM/cpu-test'+str(i+1))
        os.makedirs('test/PM/cpu-test'+str(i+1))

    for j in range(image):
       os.makedirs('test/CPU-image/'+str(cpu_image[j]))

if __name__ == "__main__":
    
     main()
