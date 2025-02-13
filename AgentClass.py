class Agent:
    next_id = 0  # Class-level variable to store the next ID
    name = "N/A"
    description = "N/A"
    location = (1,1)
    currentMapLocation = "N/A" #Translating current Map tile to description for prompting
    currentMapTile = ""
    thoughts = []

    def __init__(self, name="N/A", description="N/A", location=(1, 1)):
        self.id = Agent.next_id  # Assign the current ID to the agent
        Agent.next_id += 1      # Increment the next ID for the next agent
        self.name = name
        self.description = description
        self.location = location
        self.currentMapLocation = "N/A"
        self.currentMapTile = ""
        self.thoughts = []

    def update_map_info(self, game_map, tile_definitions): #Update the 2D map to place Character Info
        row, col = self.location 
        
        # Handle potential out-of-bounds errors:
        if 0 <= row < len(game_map) and 0 <= col < len(game_map[row]):
            self.currentMapTile = game_map[row][col]  # Get the tile character

            if self.currentMapTile == "" or self.currentMapTile == " ":
                self.currentMapTile == "_"
                
            tile_type = self.currentMapTile # Get the tile type for look up
            if tile_type in tile_definitions:
                self.currentMapLocation = tile_definitions[tile_type] #Get description from tile definitions
            else:
                self.currentMapLocation = "Empty Spot"
        else:
            self.currentMapTile = "Off Map"
            self.currentMapLocation = "Off Map"
            print(f"Warning: Agent {self.name} is off the map!") #Print message for debugging.

    def __str__(self):  # The __str__ method is used for string representation
        return (
            f"Agent ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Location: {self.location}\n"
            f"Current Map Location: {self.currentMapLocation}\n"
            f"Current Map Tile: {self.currentMapTile}\n"
            f"Thoughts: {self.thoughts}\n"
        )
    
    def prepPrompt(self, mapString, definitionString):
        mapContext = "Use the following map and map key to get context for your environment the 'CHAR' is your current position: \n" + mapString + "\nKey: " + definitionString

        jsonFormatInstruct = """ Provide your response in JSON format, like this example:

        ```json
        {
        "thought": "...",
        "action_description": "...",
        "target_location": "...",
        "target_location_description": "...",
        "target_coordinates": [row, column]
        }
        """

        prompt = mapContext + "\nProvide a single short thought as if you were the character in this situation and detail the next movement of the character based on the map and current position." + jsonFormatInstruct
        return prompt
    
    def getRolePrompt(self, fullDateString):
        role = f"You are the following character: {self.description}, It is currently {fullDateString} and you are currently on {self.currentMapLocation}" # Made role a single string
        return role

class Thought:
    thoughtText = "N/A"
    action = "N/A"
    locationDesc = "N/A"
    day = 20231221 #example integer for day
    time = 1430 #military time example for 2:30PM

class Memory:
    memoryDesc = ""
    location = ""
    day = 20231221 #example integer for day
    time = 1430 #military time example for 2:30PM
    sentimentScore = 2.5 #double between 0-10 - measures if memory is emotional
    recencyScore = 10 #same as above; automatically decay when recalling
    frequencyScore = 8 #same ^ trying to measure if the memory is reoccuring
    importanceScore = 3.2 #measure of memory is viewed as important to the agent.
