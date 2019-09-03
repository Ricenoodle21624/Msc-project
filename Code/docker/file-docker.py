#!/bin/bash/env Python3
# -*- coding: utf-8 -*-

   
import sys                  
import os                   
                
                
test = 3
num = 4

def main():

    os.makedirs('Docker/txt')
    os.makedirs('Docker/io-test1')  
    for i in range(test):
        os.makedirs('Docker/io-test1/Docker-io'+str(i+1))

    for i in range(num):
        os.makedirs('Docker/cpu-test'+str(i+1))
        for i1 in range(test):
            os.makedirs('Docker/cpu-test'+str(i+1)+'/Docker-cpu'+str(i1+1))


if __name__ == "__main__":
     main()
