#!/bin/bash/env Python3
# -*- coding: utf-8 -*-

   
import sys                  
import os                   
                
                
test = 3
num = 4

def main():

    os.makedirs('VM/txt')
    os.makedirs('VM/io-test1')  
    for i in range(test):
        os.makedirs('VM/io-test1/vm-io'+str(i+1))

    for i in range(num):
        os.makedirs('VM/cpu-test'+str(i+1))
        for i1 in range(test):
            os.makedirs('VM/cpu-test'+str(i+1)+'/vm-cpu'+str(i1+1))


if __name__ == "__main__":
     main()
