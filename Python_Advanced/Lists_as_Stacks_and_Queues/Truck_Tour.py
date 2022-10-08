from collections import deque

pumps_counts = int(input())

stops_list = deque()
for _ in range(pumps_counts):
    stop_info = [int(i) for i in input().split()]
    stops_list.append(stop_info)


for pump_start_index in range(pumps_counts):
    fuel = 0
    stops = 0
    for petrol, distance in stops_list:
        fuel += petrol
        if fuel < distance:
            stops = 1
            break
        else:
            fuel += - distance
            stops += 1
    if stops == pumps_counts:
        print(pump_start_index)
        break
    else:
        stops_list.append(stops_list.popleft())


