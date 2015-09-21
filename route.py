'''
# FORMULATION OF SEARCH PROBLEM:

1. State Space : The state graph of all the interconnected cities given in the road-segments.txt file
2. Initial State: The start city given by the user e.g. Start_city = 'Hot_Springs,_Arkansas'
3. Successor Function: From each parent city the no. of immediate cities connected in the state graph
e.g. "Y"_City,_Arkansas-->(Acorn,_Arkansas, Greenwood,_Arkansas, Hot_Springs,_Arkansas)
4. Goal State: The end_city input given by the user
5. Cost: Based on  Algorithms the cost will differ for instance. (BFS/DFS use unit costs, A* considers cost on the basis
of routing option)

# HEURISTIC used for A* -> A* search uses "Haversine" formula to calculate the distance in miles between any city to the
goal city.
The heuristic is admissible as at any given instance the cost which the function is generating to reach the goal is
lesser or equal to the actual cost of reaching the goal.
for eg. Suppose 'DeQueen,_Arkansas' is goal state & '"Y"_City,_Arkansas' is start state
Heuristic of (Acorn,_Arkansas->DeQueen,_Arkansas) = 42.55 < Actual cost from (Acorn,_Arkansas->DeQueen,_Arkansas 51)

# DESCRIPTION OF HOW DOES THE ALGORITHM WORKS?

Note: The input of all the functions is 1. source city 2. target city 3. Option (1-edges,2- Distance and 3-Time)
4. Algorithm (BFS,DFS,A*)
In  case of BFS & DFS Option given does not effect the result of the output whereas in A* the output differs as per
the input option given

--BFS:
1. The initial node (source) is pushed inside the Queue
2. If initial node is Goal node pop out append the node to the visited list and break
3. Else append it to visited list, pop out of queue and call successor function 'childNode(parent1)'
4. Add the child nodes to the queue after the existing nodes (FIFO)
5. Continue the process till goal node is reached
6. Visited list is the list of all nodes that were expanded
7. Visited list is passed to function 'calculate_parameters(visited)' which calculates the total dist and time using
another function 'childDict(node)' which stores all the details (node: key) of the each visited node
8. Results are displayed in the format [total dist, total time, visited nodes]

--DFS:
1. The initial node (source) is pushed in the Stack
2. If initial node is Goal node pop out and append the node to the visited list and break
3. Else append it to visited list and pop out and call the successor function 'childNode(parent)'
4. Add the child nodes to the stack before the existing nodes (LIFO)
5. Continue the process till goal node is reached
6. Visited list is the list of all nodes that were expanded
7. Visited list is passed to function 'calculate_parameters(visited)' which calculates the total dist and time using
another function 'childDict(node)' which stores all the details (node: key) of the each visited node
8. Results are displayed in the format [total dist, total time, visited nodes]

--A*:
1. Fringe Dictionary -> To store cost of each node, Distance Dictionary -> To store dist of any node from the start node
2. Push source node in fringe dictionary and initialize the cost as 0.0
3. If source node is the target node append it to visited list and break
4. Else push in visited list and call the function 'childastar(node, option)' which takes the option as input and
returns the child nodes dictionary with the child as key and the value depends on the option.
For instance if option = 2 (distance) then {'A':33,'B':44} etc.
5. Now, calculate the cost of each child node using the haversine function as heuristic and
pathcost = dist from start node to current child node f(n) = g(n) + h(n)
6. push all the nodes with their respective costs in fringe dictionary and pop out the node with minimum cost using
dictionary method min()
Note: If fringe dictionary contains the goal node pop out the goal node
7. Add popped out node to visited list
8. Total Distance, total time and total edges from the start node would be stored in dist variable of goal node
9. Return a list in format [dist, expanded nodes]

# RESULT OF THE PROGRAM: (Condition where: Routing option 1->Edges and Routing Algorithm 3->A*)

    Enter City 1: '"Y"_City,_Arkansas'
    Enter City 2: 'Ola,_Arkansas'
    Enter Routing Option:
    1. Press 1 for Segements
    2. Press 2 for Distance
    3. Press 3 for Time
    1
    Enter Routing Algorithm:
    1. Press 1 for BFS
    2. Press 2 for DFS
    3. Press 3 for A*
    3
    Source: "Y"_City,_Arkansas --> Target: Ola,_Arkansas
    Total no. of edges: 2
    Keeping edge as a heuristic the cities visited: ['"Y"_City,_Arkansas', 'Hot_Springs,_Arkansas', 'Ola,_Arkansas']
    Highways used are: ['US_270', 'AR_7']
    [Optimized distance],[Optimized time],[Source_City --> End_City] Details:
    [114.0, 2.778, ['"Y"_City,_Arkansas', 'Hot_Springs,_Arkansas', 'Ola,_Arkansas']]
    Do you wish to continue?
    Press  1 for Yes
    Press 2 for No
    2

#The Search Algorithm which is the best for all routing options (Edges, distances and time) --> A* Algorithm
For eg. Taking distance as an option calculate the m/c readable output from '"Y"_City,_Arkansas'-->'Ola,_Arkansas'
For BFS:
Total turns taken:  7
[341.0, 7.54, ['"Y"_City,_Arkansas', 'Acorn,_Arkansas', 'Greenwood,_Arkansas', 'Hot_Springs,_Arkansas',
'DeQueen,_Arkansas', 'Page,_Oklahoma', 'Jct_I-540_&_US_71,_Arkansas', 'Ola,_Arkansas']]
For DFS:
Total turns taken:  14
[426.0, 9.28, ['"Y"_City,_Arkansas', 'Acorn,_Arkansas', 'DeQueen,_Arkansas', 'Jct_US_59/71_&_US_70_E,_Arkansas',
'Lockesburg,_Arkansas', 'Nashville,_Arkansas', 'Prescott,_Arkansas', 'Rosston,_Arkansas', 'Waldo,_Arkansas',
'Texarkana,_Arkansas', 'New_Boston,_Texas', 'Page,_Oklahoma', 'Greenwood,_Arkansas', 'Jct_I-540_&_US_71,_Arkansas',
'Ola,_Arkansas']]
For A*:
[114.0, 2.778, ['"Y"_City,_Arkansas', 'Acorn,_Arkansas', 'Greenwood,_Arkansas', 'Ola,_Arkansas']]
-->As shown above for all the options A* gives optimal results

# A* is fastest in terms of computation
Computational costs:
1. Time Complexity:
BFS -- O(b)^d
DFS -- O(b)^m worst case
A* -- O(log h*(x))
h*(x)-- exact cost to get from x to goal
2. Space Complexity:
BFS-- O(b)^d
DFS -- O(m)
A* -- O(log h*(x))
h*(x)-- exact cost to get from x to goal

# REFERENCES:
1. Course slides and 'Artificial-Intelligence-A-Modern-Approach-3rd-Edition' for psuedo codes of BFS, DFS and A*
2. Heuristic function -- https://pypi.python.org/pypi/haversine, http://rosettacode.org/wiki/Haversine_formula#Python

# ASSUMPTIONS/PROBLEMS FACED:

1. Please enter the city names in single inverted commas while giving the inputs e.g city_1 = '"Y"_City,_Arkansas'
2. Implementing A* was a bit difficult and confusing but on referring pseudo code the concept was properly implemented
'''

from collections import defaultdict
from math import radians,sin,cos,asin,sqrt


def heurist(current_city,end_city):
    lat1 = 0.0
    lat2 = 0.0
    long1 = 0.0
    long2 = 0.0
    document = open('city-gps.txt', 'r')
    line = document.readline()
    while (line):
        split = line.split(' ')
        if (split[0] == current_city):
            lat1,long1 = float(split[1]),float(split[2])
        if (split[0] == end_city):
            lat2,long2 = float(split[1]),float(split[2])
        line = document.readline()
    document.close()
    R = 6371 # Earth radius in kilometers
    dLat = radians(lat2 - lat1)
    dLon = radians(long2 - long1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    heuristic = (R * c)*0.621371
    return heuristic

# To display the child nodes information of distance, speed and Highways --> Used for calculating parameters
def childDict(parent):
    childdict = defaultdict(dict)
    document = open('road-segments.txt', 'r')
    line = document.readline()
    while (line):
        splitarray = line.split(' ')
        if splitarray[0] == parent:
            childdict[splitarray[0]][splitarray[1]] = [splitarray[2], splitarray[3], splitarray[4]]
        line = document.readline()
    document.close()
    return childdict


# To display the child nodes of any given node --> Used in BFS DFS algorithms
def childNode(parent1):
    childlist = []
    document = open('road-segments.txt', 'r')
    line = document.readline()
    while (line):
        split = line.split(' ')
        if (split[0] == parent1):
            childlist.append(split[1])
        line = document.readline()
    document.close()
    return childlist


# Used to calculate BFS/DFS Total distance, speed and highways traversed
def calculate_parameters(visited):
    speed = 0.0
    dist = 0.0
    dist1 = 0.0
    time = 0.0
    highway = []
    n = 0
    m = 1
    childinfo = defaultdict(dict)
    while m < len(visited):
        childinfo = childDict(visited[n])
        for i in childinfo:
            inner_key = childinfo[i].keys()
            for j in inner_key:
                if j in visited:
                    dspeedh = childinfo[i][j]
                    dist = dist + float(dspeedh[0])
                    if type(float(dspeedh[1])) is float:
                        speed = float(dspeedh[1])
                        dist1 = float(dspeedh[0])
                        if(speed != 0.0):
                            time += dist1/speed
                    if dspeedh[2] in dspeedh or type(float(dspeedh[1])) is str:
                        highway.append(dspeedh[2])
        n += 1
        m += 1
        time = round(time,2)
    dsh = [dist, time, highway]
    return dsh


# BFS Algorithm
def bfs(source, target,opt):
    print "Source:", source, "--> Target:", target
    queue = [source]
    visited = []
    graph = []
    dist = 0.0
    time = 0.0
    highway = []
    final_list = []
    while len(queue) > 0:
        node = queue.pop(0)
        graph = childNode(node)
        if node == target:
            visited.append(node)
            break
        elif node not in visited:
            visited = visited + [node]
        if graph is not None:
            queue = queue + graph
    dthlist = calculate_parameters(visited)
    dist = dthlist[0]
    time = dthlist[1]
    highway = dthlist[2]
    edges = len(visited) - 1
    print "The highways used to travel from ",source," to ",target,"are",highway
    if (opt==1):
        print "Total turns taken: ",edges
    if(opt==2):
        print "Total distance covered: ",dist
    if(opt==3):
        print "Time required in hours: ",time
    print "List of cities visited: ",visited
    final_list = [dist, time, visited]
    return final_list

# DFS Algorithm
def dfs(source, target,opt):
    print "Source:", source, "--> Target:", target
    stack = [source]
    visited = []
    graph = []
    dist = 0.0
    time = 0.0
    highway = []
    final_list = []
    while len(stack) > 0:
        node = stack.pop(0)
        graph = childNode(node)
        if node == target:
            visited.append(node)
            break
        elif node not in visited:
            visited = visited + [node]
        if graph is not None:
            stack = graph + stack
    dthlist = calculate_parameters(visited)
    dist = dthlist[0]
    time = dthlist[1]
    highway = dthlist[2]
    edges = len(visited) - 1
    print "The highways used to travel from ",source," to ",target,"are",highway
    if (opt==1):
        print "Total turns taken: ",edges
    if(opt==2):
        print "Total distance covered: ",dist
    if(opt==3):
        print "Time required in hours: ",time
    print "List of cities visited: ",visited
    final_list = [dist, time, visited]
    return final_list

# Used to produce child nodes for A* Algorithm in sorted order based on routing option(time/distance)
def childastar(parentnode, opt):
    node = parentnode
    childnodes = []
    parameter = []
    childinfo = defaultdict(dict)
    document = open('road-segments.txt', 'r')
    line = document.readline()
    while (line):
        splitarray = line.split(' ')
        if (splitarray[0] == parentnode and opt == 2):
            childinfo[splitarray[0]][splitarray[1]] = float(splitarray[2])
        if (splitarray[0] == parentnode and opt == 3 and float(splitarray[3]) is not str):
            speed = float(splitarray[3])
            dist = float(splitarray[2])
            time = round(dist/speed,3)
            childinfo[splitarray[0]][splitarray[1]] = time
        if (opt == 1):
            childinfo[splitarray[0]][splitarray[1]] = 1.0
        line = document.readline()
    document.close()
    for i in childinfo[node].keys():
        r = min(childinfo[node], key=childinfo[node].get)
        childnodes.append(r)
        parameter.append(childinfo[node][r])
        if (childinfo[node].keys is not None):
            del childinfo[node][r]
    p = [childnodes, parameter]
    return p

# A* Algorithm function
def astar(source, target, option):
    fringedict = defaultdict(float)
    visited = []
    fringedict = {source: 0.0}
    childnodes = []
    pathcost = 0.0
    dist = 0.0
    distancedict = defaultdict(float)
    distancedict = {source: 0.0}
    total_cost = 0.0
    while len(fringedict.keys()) > 0:
        (' specific condition when target node and other nodes have same costs')
        if target in fringedict.keys():
            node = target
        else:
            q = min(fringedict, key=fringedict.get)
            node = q
        total_cost = fringedict.pop(node)
        dist = distancedict.pop(node)
        if node == target:
            visited.append(node)
            break
        if node not in visited:
            visited.append(node)

        graph = childastar(node, option)
        childnodes = graph[0]
        m = 0
        for child in childnodes:
            pathcost = dist + graph[1][m]
            heuristic = heurist(child,target)
            cost = pathcost + heuristic
            m += 1
            fringedict[child] = cost
            distancedict[child] = pathcost
            if child == target:
                break
    final_list = [dist, visited]
    return final_list

# Main Function
if __name__ == '__main__':

    z = True
    start_city = input('\nEnter City 1: ')
    #start_city = '"Y"_City,_Arkansas'
    end_city = input('\nEnter City 2: ')
    #end_city = 'DeQueen,_Arkansas'
    while(z == True):
        option = input('\nEnter Routing Option:\n1. Press 1 for Segements\n2. Press 2 for Distance\n3. Press 3 for Time\n')
        A = [1,2,3]
        if option not in A:
            print "Invalid Option"
        algo = input('\nEnter Routing Algorithm:\n1. Press 1 for BFS\n2. Press 2 for DFS\n3. Press 3 for A*\n')
        if algo not in A:
            print "Invalid Option"
        total_speed = 0.0
        total_distance = 0.0
        total_time = 0.0
        final_output = []

        if algo == 3:
            print "Source:", start_city, "--> Target:", end_city
            edge_array = astar(start_city,end_city,1)
            total_edge = edge_array[0]
            dist_array = astar(start_city,end_city,2)
            total_distance = dist_array[0]
            time_array = astar(start_city,end_city,3)
            total_time = time_array[0]
            if option == 1:
                final_output.append(total_distance)
                final_output.append(total_time)
                final_output.append(edge_array[1])
                dthlist = calculate_parameters(edge_array[1])
                print "\nTotal no. of edges:",int(edge_array[0])
                print "\nKeeping edge as a heuristic the cities visited:", edge_array[1]
                print "\nHighways used are:",dthlist[2]
            if option == 2:
                final_output.append(total_distance)
                final_output.append(total_time)
                final_output.append(dist_array[1])
                dthlist = calculate_parameters(dist_array[1])
                print "\nTotal distance covered (miles): ",total_distance
                print "\nKeeping distance as a heuristic the cities visisted are:",dist_array[1]
                print "\nHighways used are:",dthlist[2]
            if option == 3:
                final_output.append(total_distance)
                final_output.append(total_time)
                final_output.append(time_array[1])
                dthlist = calculate_parameters(time_array[1])
                print "\nTotal time in hrs for a car that always travels at the speed limit, all the cities visited: ",total_time
                print "\nKeeping speed as a heuristic the cities visited are:",time_array[1]
                print "\nHighways used are:",dthlist[2]
            print "\n[Optimized distance],[Optimized time],[Source_City --> End_City] Details: "
            print final_output

        if algo == 1:
            print bfs(start_city,end_city,option)
        if algo == 2:
            print dfs(start_city,end_city,option)
        ans = input("\nDo you wish to continue?\nPress  1 for Yes\nPress 2 for No\n")
        if (ans == 1):
            z = True
        else:
            z = False