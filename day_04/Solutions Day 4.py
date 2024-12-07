import os

class node:
    def __init__(self,coords,value):
        self.coords = coords
        self.value = value
        self.neighbors = set()
        self.neighbor_values = set()

def add_neighbor(nodeA,nodeB,graph):
    graph[nodeA.coords].neighbors.add(nodeB)
    nodeA.neighbor_values.add(nodeB.value)
    graph[nodeB.coords].neighbors.add(nodeA)
    nodeB.neighbor_values.add(nodeA.value)

def insert_node(coords,graph,data):
    if coords not in graph:
        graph[coords] = node(coords,data[coords[0]][coords[1]])

def initialize_node(i,j,graph,data,node):
    insert_node((i,j),graph,data)
    add_neighbor(node,graph[(i,j)],graph)
                
def create_graph(data,m,n):
    graph = {}
    insert_node((0,0),graph,data)
    for i in range(m):
        for j in range(n):
            current_node = graph[(i,j)]
            if i < m - 1:
                # vertical
                initialize_node(i+1,j,graph,data,current_node)
                #y = x diagonal
                if j != 0:
                    initialize_node(i+1,j-1,graph,data,current_node)
                #y = -x diagonal
                if j != m - 1:
                    initialize_node(i+1,j+1,graph,data,current_node)
            if j < n - 1:
                # horizontal
                initialize_node(i,j+1,graph,data,current_node)
    return graph

def determine_direction(nodeA,nodeB):
    return (nodeB.coords[0]-nodeA.coords[0],
            nodeB.coords[1]-nodeA.coords[1])

def search(node,graph,word,direction,count):
    if len(word) == 0:
        return 1
    if word[0] in node.neighbor_values:
        for neighbor in node.neighbors:
            if neighbor.value == word[0]:
                if direction == (0,0):
                    count += search(neighbor,graph,word[1:],\
                            determine_direction(node,neighbor),0)
                elif direction == determine_direction(node,neighbor):
                    count += search(neighbor,graph,word[1:],direction,0)
    return count

def complex_search(node,graph,word,start_index):
    count = 0
    x_count = 0
    direction_dict = {(-1,-1):'NW',\
                      (-1,1):'NE',\
                      (1,-1):'SW',\
                      (1,1):'SE'}
    if word[start_index-1] in node.neighbor_values:
        for neighbor in node.neighbors:
            direction = determine_direction(node,neighbor)
            if direction in direction_dict.keys() and\
            neighbor.value == word[start_index-1] and\
            check_inverse(graph,node.coords,direction,word[start_index+1]):
                x_count += 1
    if x_count > 1:
        count = 1
    return count
    
def get_candidates(graph,character,exclude_rows,exclude_columns):
    candidates = []
    verify = True
    if len(exclude_rows) == 0 and len(exclude_columns) == 0:
        verify = False
    
    for node in graph.values():
        if node.value == character:
            if verify and exclude(node.coords,exclude_rows,exclude_columns):
                continue
            candidates.append(node.coords)
    return candidates

def exclude(coords,rows,cols):
    for row in rows:
        if coords[0] == row:
            return True
    for col in cols:
        if coords[1] == col:
            return True
    return False

def check_inverse(graph,coords,direction,target):
    if graph[get_inverse(coords,direction,target)].value == target:
        return True
    return False

def get_inverse(coords,direction,target):
    return direction[0] * -1+coords[0],direction[1] * -1+coords[1]

#Advent of code Day 4 puzzle 1
def part_one(data,word):
    count = 0
    m = len(data)
    n = len(data[0])
    graph = create_graph(data,m,n)
    candidates = get_candidates(graph,word[0],[],[])
    for node in candidates:
        count += search(graph[node],graph,word[1:],(0,0),0)
    return count


#Advent of code Day 4 puzzle 2
def part_two(data,word,start_index):
    count = 0
    m = len(data)
    n = len(data[0])
    #make graph
    graph = create_graph(data,m,n)
    #find candidates (only in i = 1:m-1, j = 1:n-1)
    candidates = get_candidates(graph,word[start_index],[0,m-1],[0,n-1])
    for node in candidates:
        count += complex_search(graph[node],graph,word,start_index)
    return count
    
read_file = open("input.txt",'r')
data = []
while read_file:
    line = read_file.readline()
    if line == "":
        break
    data.append(list(line.strip())) 

print(part_one(data,'XMAS'))
print(part_two(data,'MAS',1))
read_file.close()
    
