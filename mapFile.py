#File will hold map and definition variables for better modularity
allMap = [["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "I", "I", "I", "I", "I", "I", "I", "O", "I", "I", "I", "I", "I", "I", "I", "I", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "I", "I", "R", "I", "I", "I", "I", "O", "I", "I", "I", "I", "I", "I", "I", "I", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "I", "I", "I", "I", "I", "I", "I", "O", "I", "I", "I", "I", "I", "I", "I", "I", "O", "O", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "O", "O", "O", "O", "I", "I", "I", "I", "Ba", "I", "I", "O", "I", "I", "I", "I", "I", "I", "I", "I", "O", "O", "I1", "C", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "BE", "BE", "BE", "P", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "P", "P", "I1", "I", "I2", "I", "I3", "I", "I4", "I", "I5", "I", "I6", "I", "I7", "I", "I8", "I", "E"],
["E", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "E"],
["E", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "E"],
["E", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "E"],
["E", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "E"],
["E", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "E"],
["E", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "E"],
["E", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "R", "R", "R", "R", "P", "P", "P", "P", "P", "P", "E"],
["E", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "R", "R", "R", "R", "P", "P", "P", "P", "P", "P", "E"],
["E", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "Y", "GH", "GH", "GH", "GH", "Y", "O", "O", "Y", "G", "G", "G", "G", "Y", "O", "O", "O", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "Y", "GH", "GH", "GH", "GH", "Y", "O", "O", "Y", "G", "G", "G", "G", "Y", "O", "O", "O", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "Y", "GH", "GH", "GH", "GH", "Y", "O", "O", "Y", "G", "G", "G", "G", "Y", "O", "O", "O", "Y", "Y", "Y", "Y", "SW", "Y", "SW", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "Y", "GH", "GH", "GH", "GH", "Y", "O", "O", "Y", "G", "G", "G", "G", "Y", "O", "O", "O", "I", "I", "I", "I", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "Y", "GH", "GH", "GH", "GH", "Y", "O", "O", "Y", "Y", "Y", "Y", "Y", "Y", "O", "O", "I", "I", "I", "I", "I", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "B", "I", "T", "I", "I", "I", "O", "O", "I", "I", "I", "I", "B", "I", "O", "O", "I", "I", "I", "I", "I", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "S", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "S", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "I", "B", "I", "I", "I", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "F", "I", "O", "O", "I", "I", "S", "T", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "I", "I", "Y", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "T", "I", "I", "O", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "I", "I", "O", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "Co", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "I", "I", "I", "I", "I", "I", "O", "O", "O", "O", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "P", "P", "R", "R", "R", "R", "P", "P", "O", "O", "O", "O", "E"],
["E", "I", "I", "I", "I", "I", "I", "P", "P", "I", "I", "I", "I", "I", "I", "P", "P", "I", "I", "I", "I", "I", "I", "I", "I", "P", "P", "P", "P", "R", "R", "R", "R", "P", "P", "P", "P", "O", "O", "E"],
["E", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "R", "R", "R", "R", "P", "P", "P", "P", "P", "P", "E"],
["E", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "R", "R", "R", "R", "P", "P", "P", "P", "P", "P", "E"],
["E", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "E"],
["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],

]   

tile_definitions = { #Tuples for character in 2D map to description
    "E": "Edge of map",
    "P": "Path",
    # "W": "Wall",
    "De": "Desk",
    "CHAR": "Current Character Location",
    "B": "Bed",
    "BE": "Bench",
    "Ba": "Bathroom",
    "T": "Table",
    "S": "Stove",
    "R": "Refrigerator",
    "Co": "Couch",
    "I1": "Aisle 1",
    "I2": "Aisle 2",
    "I3": "Aisle 3",
    "I4": "Aisle 4",
    "I5": "Aisle 5",
    "I6": "Aisle 6",
    "I7": "Aisle 7",
    "I8": "Aisle 8",
    "C": "Cashier",
    "G": "Garden",
    "SW": "Swing set",
    "I": "Interior"
}

tileDefToString = ''.join(f"{k} - {v} | " for k, v in tile_definitions.items()) #toString for tile Definitions

def betterPadList(twoDList):
    padded_map_string = ""  

    for rowIndex in range(len(twoDList)):
        row_string = ""  
        for colIndex in range(len(twoDList[rowIndex])):
            item = twoDList[rowIndex][colIndex]
            padding = 4 - len(item)  
            if padding > 0:
                padded_item = item + " " * padding  
            elif padding < 0:
                padded_item = item[:4]  
            else:
                padded_item = item 

            #row_string += "[" + padded_item + "],"    #Provided decent results.
            row_string += "'" + padded_item + "',"
            if colIndex < len(twoDList[rowIndex]) -1: 
                row_string += " "

        padded_map_string += row_string + "\n"  

    return padded_map_string  

paddedDefaultMap = betterPadList(allMap)

def agentMap(x, y, agents):
    tempAllMap = [row[:] for row in allMap]
    tempAllMap[x][y] = "CHAR"

    for agent in agents:
        agentX = agent.location[0]
        agentY = agent.location[1]

        tempAllMap[agentX][agentY] = agent.name
    return betterPadList(tempAllMap)
