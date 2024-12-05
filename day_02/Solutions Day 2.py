#Advent of code Day 2 puzzle 1
    #Read line
    #Line may contain variable elements per line
    #split(' ')
    #All levels increasing or decreasing
    #adjacent levels must have difference between 1 and 3 (inclusive)
    #Can mark level as safe only if those conditions are met
    #return safe count
    #for each in line: between 1 and 3 or -1 and -3 (once first is checked,
    #all others must be neg or pos)

import os

def _is_safe(levels):
    if int(levels[0]) == int(levels[1]):
        return False
    if int(levels[0]) < int(levels[1]):
        direction = 1
    else:    
        direction = -1
        
    for i in range(1,len(levels)):
        distance = (int(levels[i]) - int(levels[i-1]))*direction
        if (distance < 1 or distance > 3):
            return False

    return True

read_file = open("input.txt",'r')

count = 0

while read_file:
    line = read_file.readline()
    if line == "":
        break
    levels = line.strip().split(" ")
    if _is_safe(levels):
        count += 1
    
read_file.close()

print(count)

#Advent of code Day 2 puzzle 2
#If there is a bad level, attempt to remove elements

def _is_safe_dampen(levels):
    if int(levels[0]) < int(levels[1]):
        direction = 1
    else:    
        direction = -1
        
    for i in range(1,len(levels)):
        distance = (int(levels[i]) - int(levels[i-1]))*direction
        if (distance < 1 or distance > 3):
            for j in range(0,len(levels)):
                if _is_safe(levels[:j]+levels[j+1:]):
                    return True
            return False

    return True

read_file = open("input.txt",'r')

count = 0

while read_file:
    line = read_file.readline()
    if line == "":
        break
    levels = line.split(" ")
    levels[-1] = levels[-1].strip()
    if _is_safe_dampen(levels):
        count += 1
    
read_file.close()

print(count)
