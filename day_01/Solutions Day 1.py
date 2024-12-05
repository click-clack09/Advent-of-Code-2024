#Advent of code Day 1 puzzle 1
    #Puzzle is asking is to sort then compare distance
    #(think absolute value).
    #but is sort really necessary?
    #(sum of the differences vs. difference of the sums)
    #Initialize sum_0,sum_1 = 0,0
    #Read input file
    #split line, add left to sum_0, right to sum_1
    #return abs(sum_0 - sum_1)

import math
import os

read_file = open("input.txt",'r')

sum_0 = 0
left_list = []
right_list = []

while read_file:
    line = read_file.readline()
    if line == "":
        break
    left,right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

read_file.close()

left_list = sorted(left_list)
right_list = sorted(right_list)
    
for i in range(len(left_list)):
    sum_0 += abs(left_list[i] - right_list[i]) 

print(sum_0)

#Advent of code Day 1 puzzle 2

read_file = open("input.txt",'r')

sum_0 = 0
left_list = []
right_map = {}

while read_file:
    line = read_file.readline()
    if line == "":
        break
    left,right = line.split("   ")
    left_list.append(int(left))
    right = int(right.strip())
    if right not in right_map:
        right_map[right] = 0
    right_map[right] += 1
    
read_file.close()

for num in left_list:
    if num in right_map:
        sum_0 += num * right_map[num]

print(sum_0)
