# 134	Gas Station

# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).

# You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.


# Example 1:

# Input:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# Output: 3

# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.


# Example 2:

# Input:
# gas  = [2,3,4]
# cost = [3,4,3]

# Output: -1
def gasstation(gas,cost):
    totalgas=0
    totalcost=0
    balance=0
    start=0
    
    for i in range(0,len(gas)):
        totalgas += gas[i]
        totalcost += cost[i]
    for i in range(0, len(gas)):
        balance += gas[i] - cost[i]
        if balance < 0:
            start = i + 1
        balance = 0
    if totalcost <= totalgas:
        return start
    return -1

# # gas  = [1,2,3,4,5]
# # cost = [3,4,3,1,2]

gas  = [2,3,4]
cost = [3,4,3]
print(gasstation(gas,cost))


# def gas_station(gas,cost):
#     totalgas=0
#     totalcost=0
#     starting_station=0

#     if len(gas) != len(cost):
#         return -1

#     for i in range(0,len(gas)):
#         totalgas += gas[i]
#         totalcost += cost[i] 
#     if totalgas < totalcost:
#         return -1
    
#     for i in range(0,len(gas)):
#         while gas[starting_station] <= cost[starting_station]:
#             starting_station = starting_station + 1
#         return starting_station


# # gas  = [1,2,3,4,5]
# # cost = [3,4,3,1,2]

# gas  = [2,3,4]
# cost = [3,4,3]
# print(gas_station(gas,cost))

