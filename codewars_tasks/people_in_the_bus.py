def number(bus_stops):
    people_in_bus = 0
    for in_bus, out_bus in bus_stops:
        people_in_bus += in_bus - out_bus

    return people_in_bus



print(number([[10,0],[3,5],[5,8]]))