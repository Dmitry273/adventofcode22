from collections import defaultdict
from queue import PriorityQueue

valves = {}
rates = {}
pressures = defaultdict(lambda: float('inf'))
pressures[('AA', 0, ())] = 0
routes = PriorityQueue()
routes.put((0, 'AA', (), 0))

for line in open('Day16/d16.txt', 'r'):
    valve = line[6:8]
    rate = int(line[line.find('=')+1:line.find(';')])
    leads_to = {i:1 for i in line[:-1].replace(',', '').split()[9:]}
    rates.update({valve:rate})
    valves.update({valve:leads_to})

for valve in frozenset(valves):
    if len(valves[valve]) == 2 and rates[valve] == 0:
        head, tail = *valves[valve],
        l = valves[valve][head] + valves[valve][tail]
        valves[head].pop(valve)
        valves[tail].pop(valve)
        valves[head].update({tail:l})
        valves[tail].update({head:l})
        valves.pop(valve)

total = 30
while not routes.empty():
    pressure_est, curr, opened, time = routes.get()

    if time >= total: continue
    if pressure_est > pressures[(curr, time, opened)]: continue

    for step in valves[curr]:
        new_time = time+valves[curr][step]
        if pressure_est >= pressures[(step, new_time, opened)]: continue
        else: pressures[(step, new_time, opened)] = pressure_est
        routes.put((pressure_est, step, opened, new_time))
    
    if rates[curr] and curr not in opened:
        new_opened = tuple(list(opened)+[curr])
        new_pressure = pressure_est-(total-time-1)*rates[curr]
        if new_pressure >= pressures[(curr, time+1, new_opened)]: continue
        else: pressures[(curr, time+1, new_opened)] = new_pressure
        routes.put((new_pressure, curr, new_opened, time+1))

print(min(pressures.values()))
