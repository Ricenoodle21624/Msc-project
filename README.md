# Msc-project

1.Program introduction  
  1.1 Run the file.py file on VM (Virtual Machine), Docker, and VM respectively to generate folders to collect data.  
  1.2 After configuring the environment of telegraf, Inflluxdb, sysbench and python on VM, Docker and PM (Physical Machine), run the scripts to generate workloads (CPU, IO, Memory).  
  1.3 We need to copy the data to the PM which collected in the VM and Docker, so we should copy the 'VM' and 'Docker' folders to the MSC folder.  
  1.4 Run project-data_cleanning to do data cleaning job and organize the data. According to the requirements of the experiment, set the number of tests, the number of prime numbers and other parameters, then run the project-drawing.py for drawing plots.  
  1.5 The data cleaning has been completed in this experiment, and it is no need to run the project-data_cleanning file, which means we can use the collected data directly. The MSC folder contains all the data for this experiment, including the image and the output of the sysbench test.  
