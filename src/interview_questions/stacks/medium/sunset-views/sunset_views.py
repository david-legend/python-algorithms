# Solution 1
# O(n) time | O(n) space 
def sunsetViews(buildings, direction):
    potentialBuildings = []

    # start iterating from 0 if direction is 'EAST'
    # OR start iterating from the back of the array if direction is 'WEST'
    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    # increment by 1 or decrease by 1 based on direction
    step = 1 if direction == "EAST" else -1

    idx = startIdx
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        # if current building is equal to or greater than any building we have come accross
        # remove that building from the stack
        while len(potentialBuildings) > 0 and buildings[potentialBuildings[-1]] <= buildingHeight:
            potentialBuildings.pop()

        potentialBuildings.append(idx)

        # increment/decrease index based on direction
        idx += step

    # reverse final array if direction is 'WEST'
    if direction == "WEST":
        return potentialBuildings[::-1]

    return potentialBuildings

# Solution 2
# O(n) time | O(n) space - where n is the length of the input array
def sunsetViews2(buildings, direction):
    buildingsWithSunsetViews = []
    
    # start iterating from 0 if direction is 'EAST'
    # OR start iterating from the back of the array if direction is 'WEST'
    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    # increment by 1 or decrease by 1 based on direction
    step = 1 if direction == "WEST" else -1

    idx = startIdx
    # track the current Maximum height
    runningMaxHeight = 0

    while idx >= 0 and idx < len(buildings):
        # current building
        buildingHeight = buildings[idx]

        # if current height of building is greater than a previous building
        # Append that building to buildingsWithSunsetViews[] 
        if buildingHeight > runningMaxHeight:
            buildingsWithSunsetViews.append(idx)

        # compare current height of building to previous max height
        # assign new runningMaxHeight if it is taller than the previous 
        runningMaxHeight = max(runningMaxHeight, buildingHeight)

        # increment/decrease index based on direction
        idx += step

    # reverse final array if direction is 'EAST'
    if direction == "EAST":
        return buildingsWithSunsetViews[::-1]

    return buildingsWithSunsetViews


test1 = {
  "buildings": [3, 5, 4, 4, 3, 1, 3, 2],
  "direction": "EAST"
}
test2 = {
  "buildings": [3, 5, 4, 4, 3, 1, 3, 2],
  "direction": "WEST"
}
test3 = {
  "buildings": [20, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8],
  "direction": "EAST"
}
test4 = {
  "buildings": [],
  "direction": "WEST"
}


print("Running Solution 1\n")

print("Test 1: ", sunsetViews(test1["buildings"], test1["direction"]))  # [1, 3, 6, 7]
print("Test 2: ", sunsetViews(test2["buildings"], test2["direction"]))  # [0, 1]
print("Test 3: ", sunsetViews(test3["buildings"], test3["direction"]))  # [0, 13, 14]
print("Test 4: ", sunsetViews(test4["buildings"], test4["direction"]))  # []

print("\n\nRunning Solution 2\n")

print("Test 1: ", sunsetViews2(test1["buildings"], test1["direction"]))  # [1, 3, 6, 7]
print("Test 2: ", sunsetViews2(test2["buildings"], test2["direction"]))  # [0, 1]
print("Test 3: ", sunsetViews2(test3["buildings"], test3["direction"]))  # [0, 13, 14]
print("Test 4: ", sunsetViews2(test4["buildings"], test4["direction"]))  # []
