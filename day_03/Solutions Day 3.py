import re
import os

#Advent of code Day 3 puzzle 1

def part_one(data):
    total = 0
    for operation in re.findall(r"mul\(\d{1,3},\d{1,3}\)", data):
        operands = operation[4:-1].split(',')
        total += int(operands[0])*int(operands[1])
    return total

#Advent of code Day 3 puzzle 2
    
def part_two(data):
    total = 0
    calc = True
    while len(data) > 0:
        if calc:
            temp = re.search(r"don\'t\(\)",data)
            if temp:
                scan_line = data[:temp.start()]
                data = data[temp.end():]
                calc = False
            else:
                scan_line = data
                data = ''

            for operation in re.findall(r"mul\(\d{1,3},\d{1,3}\)",scan_line):
                operands = operation[4:-1].split(',')
                total += int(operands[0])*int(operands[1])
        else:
            temp = re.search(r"do\(\)",data)
            if temp:
                data = data[temp.end():]
                calc = True
            else:
                data = ''
    return total

#Execute
read_file = open("input.txt",'r')
data = read_file.read()
print(part_one(data))
print(part_two(data))
read_file.close()
    
