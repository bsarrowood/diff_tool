# Created by:       Brad Arrowood
# Created on:       2023.05.30
# Last updated:     2023.05.30
# Script name:      diff_tool.py
# Version:          1.0
# Description:      script to compare 1 TXT file against another TXT then output a file with the differences

master_file = 'file_1.txt'
compare_file = 'file_2.txt'
master_list = []
compare_list = []

# read all the lines of each file into separate lists
with open(master_file, 'r') as file1:
    master_list = file1.readlines()

with open(compare_file, 'r') as file2:
    compare_list = file2.readlines()

# creating the output file
# then comparing each item in the compare list against the master list
# any device found in both triggers a print to the screen to notify
# any device from the compare file not found in the master file is appended to the output file
file3 = open('compare-Homies_not_in_AC_list.txt', 'w')
for device in compare_list:
    if device in master_list:
        print('Device from Homies OU list found in AnyConnect list')
    else:
        file3.write(device)
