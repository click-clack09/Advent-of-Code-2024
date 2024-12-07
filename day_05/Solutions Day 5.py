import os
import re

def check_update(rules,update):
    previous = {update[0]}
    for entry in update[1:]:
        if entry not in rules:
            previous.add(entry)
            continue
        elif rules[entry].intersection(previous) != set():
            return 0            
        previous.add(entry)

    return int(update[len(update)//2])

def correct_update(rules,update):
    if len(update) == 1 or check_update(rules,update) != 0:
        return 0
    pointer = 1
    error_stack = []
    previous = {update[0]}
    
    while pointer < len(update):
        entry = update[pointer]
        if entry not in rules:
            previous.add(entry)
            pointer += 1
            continue
        while rules[entry].intersection(previous) != set():
            #move pointer back one index, recheck
            pointer -= 1
            previous.remove(update[pointer])
            update[pointer],update[pointer+1] = update[pointer+1], update[pointer]
        pointer += 1
        previous.add(entry)
    return int(update[len(update)//2])

#Advent of code Day 5 puzzle 1
def part_one(rules, updates):
    count = 0
    for update in updates:
        count+= check_update(rules,update)
    return count

#Advent of code Day 5 puzzle 2
def part_two(rules,updates):
    count = 0
    for update in updates:
        count += correct_update(rules,update)
    return count

rules = {}
updates = []

read_file = open("input.txt",'r')
while read_file:
    line = read_file.readline()
    if line == '':
        break
    if line == '\n':
        continue
    line = line.strip()
    if re.match(r"\d+\|\d+",line):
        key,value = line.split("|")
        if key not in rules:
            rules[key] = set()
        rules[key].add(value)
    else:
        updates.append(line.split(","))
read_file.close()
        
print(part_one(rules, updates))
print(part_two(rules, updates))
    
