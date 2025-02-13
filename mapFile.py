#File will hold map and definition variables for better modularity
allMap = [
    ["E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"P",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"P",	"P",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"W",	"W",	"W",	"D",	"W",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	"W",	"W",	"W",	"W",	"W",	"D",	"D",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"De",	" ", 	"D",	" ", 	" ", 	"Co",	"Co",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"C",	"C",	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	" ",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"B",	"B",	"TV",	"W",	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	"I3",	" ", 	"I4",	" ", 	"I5",	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	"W",	" ", 	"TV",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	"I3",	" ", 	"I4",	" ", 	"I5",	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"W",	"W",	"D",	"W",	"D",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	"I3",	" ", 	"I4",	" ", 	"I5",	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"Ba",	"D",	" ", 	" ", 	" ", 	"T",	"T",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	"I3",	" ", 	"I4",	" ", 	"I5",	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"W",	"W",	"T",	" ", 	" ", 	" ", 	" ", 	"D",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	"I3",	" ", 	"I4",	" ", 	"I5",	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	"T",	" ", 	"S",	" ", 	"R",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	"W",	"W",	"W",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E"]
]

tile_definitions = { #Tuples for character in 2D map to description
    "E": "Edge of map",
    "P": "Path",
    "W": "Wall",
    "De": "Desk",
    "CHAR": "Current Character Location",
    "B": "Bed",
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
    "C": "Cashier"
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

            row_string += padded_item  
            if colIndex < len(twoDList[rowIndex]) -1: 
                row_string += " "

        padded_map_string += row_string + "\n"  

    return padded_map_string  

paddedDefaultMap = betterPadList(allMap)

def agentMap(x, y):
    tempAllMap = allMap
    tempAllMap[x][y] = "CHAR"

    return betterPadList(tempAllMap)
