#!/bin/bash/env Python3
# -*- coding: utf-8 -*-


import sys                  
import os                   
import errno                


test = 3
num = 4
image = 6
environment = ['Docker','VM','PM']
cpu_image = ['CPU-usage', 'Latency-sum', 'Latency-avg', 'cpu-speed', 'total-time', 'execution-time']
def main():
    
    os.makedirs('MSC/CPU-image')
    os.makedirs('MSC/IO-image/IOPS')
    os.makedirs('MSC/IO-image/IO-wkB_per_s')
    os.makedirs('MSC/Memory-image')
    for n in range(test):
        os.makedirs('MSC/'+environment[n]+'/image')
        os.makedirs('MSC/'+environment[n]+'/txt')
        os.makedirs('MSC/'+environment[n]+'/io-test1')

    for i in range(num):
        os.makedirs('MSC/Docker/cpu-test'+str(i+1))
        os.makedirs('MSC/VM/cpu-test'+str(i+1))
        os.makedirs('MSC/PM/cpu-test'+str(i+1))

    for j in range(image):
       os.makedirs('MSC/CPU-image/'+str(cpu_image[j]))

if __name__ == "__main__":
     main()
