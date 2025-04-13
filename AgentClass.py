import json
from openai import OpenAI
import os
from dotenv import load_dotenv
import mapFile

load_dotenv()
gemini_key = os.environ["GEMINI_KEY"]

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

class Agent:
    next_id = 0  # Class-level variable to store the next ID

    def __init__(self, name="N/A", description="N/A", location=(1, 1)):
        self.id = Agent.next_id  # Assign the current ID to the agent
        self.name = name
        self.description = description
        self.location = location
        self.currentMapLocation = "N/A"
        self.currentMapTile = ""
        self.thoughts = []
        self.memories = []

        Agent.next_id += 1      # Increment the next ID for the next agent

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
    
    def getHighestMemoriesString(self):

        memoryContext = self.getHighestMemories()

        memoryString = "No Recent Memories."

        if(len(self.thoughts) > 4):
            if(len(memoryContext) != 0):
                memoryString = ""
                for memory in memoryContext:
                    memoryString += str(memory) + "\n"

        return memoryString

    
    def prepPrompt(self, mapString, definitionString, agents):

        mapContext = "You are navigating a grid-based map. The top-left corner is (0, 0). Each blank tile in the map is represented by exactly four literal spaces (from left to right). X increases to the right, and Y increases downwards. Use the following map and map key to get context for your environment the 'CHAR' is your current position ( "+ str(self.location[0]) +"," + str(self.location[1]) + "): \n" + mapString + "\nKey: " + definitionString

        memoryString = self.getHighestMemoriesString()
                

        memoryPrompt = " Use the following list of memories for context of past events, IMPORTANT:: ensure your actions not repetitive based on time from previous memories unless absolutely necessary ::. "

        jsonFormatInstruct = """ Provide your response in JSON format, like this example:

        ```json
        {
        "response_type": "thought",
        "thought": "...",
        "action_description": "...",
        "target_location": "...",
        "target_location_description": "...",
        "target_coordinates": [row, column]
        }
        """

        agentsInTheArea = []

        for agent in agents:
            currentX = self.location[0]
            currentY = self.location[1]
            if(agent.name != self.name):
                if agent.location[0] >= currentX - 3 and agent.location[0] <= currentX + 3:
                    if agent.location[1] >= currentX - 3 and agent.location[1] <= currentY + 3:
                        agentsInTheArea.append(agent.name)

        jsonFormatInstructConverse = """ Alternatively, If you want to initiate a conversation, Provide your response in JSON format, like this example:

        ```json
        {
        "response_type": "converse",
        "agent": "...",
        "initial_message": "...",
        "target_coordinates": [row, column]
        }
        """
        prompt = memoryPrompt + memoryString + mapContext + "\nProvide a single short thought as if you were the character in this situation and detail the next movement of the character based on the map and current position." + jsonFormatInstruct


        if len(agentsInTheArea) > 0:
            surroundingAgents = "The following agents are close enough to start a conversation: " + str(agentsInTheArea)
            prompt += surroundingAgents + jsonFormatInstructConverse
            
        print(prompt)
        return prompt
    
    def getRolePrompt(self, fullDateString):
        role = f"You are the following character: {self.description}, It is currently {fullDateString} and you are currently on {self.currentMapLocation}" # Made role a single string
        return role
    
    def appendThought(self, thoughtString, dateTimeObj, agents):
        startJsonIndex = thoughtString.find("{")
        endJsonIndex = thoughtString.find("}")+1        
        jsonObj = json.loads(thoughtString[startJsonIndex:endJsonIndex+1])
        print(str(jsonObj))

        if(jsonObj["response_type"] == "converse"):
            targetAgent = ""
            for agent in agents:
                if agent.name == jsonObj["agent"]:
                    targetAgent = agent
            conversationObj = Conversation(self, jsonObj, dateTimeObj, targetAgent)

        elif(jsonObj["response_type"] == "thought"):
            currThought = Thought(dateTimeObj, thoughtString, self.location)
            self.thoughts.append(currThought)
            self.location = currThought.endLoc
        else:
            print("invalid response")

    def prepMemoryPrompt(self, index=-1):
        return f"{Memory.memorySummarizePrompt} \n {str(self.thoughts[index])} {Memory.memoryScorePrompt} {Memory.memoryJsonPrompt}"
    
    def appendMemory(self, thoughtObject, rawMemory):
        currMemory = Memory(thoughtObject, rawMemory)
        self.memories.append(currMemory)

    def getHighestMemories(self):
        memoriesNum = len(self.memories)
        if memoriesNum == 0:
            return []
        elif memoriesNum <= 5:
            return self.memories
        else:
            #Sort memories by total score, return top 5
            sortedMemories = sorted(self.memories, key=lambda x: x.totalScore, reverse=True)
            return sortedMemories[:5]

    def generateThoughtResponse(self, dateString, timeString, dateTimeObj, agents):
        currentAgentMap = mapFile.agentMap(self.location[0], self.location[1], agents)
        agentContentPrompt = self.prepPrompt(currentAgentMap, mapFile.tileDefToString, agents)
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "system", "content": self.getRolePrompt(dateString + " " + timeString)}, # Corrected to use single string role
                {"role": "user", "content": agentContentPrompt}
            ]
        )
        self.appendThought(response.choices[0].message.content,dateTimeObj, agents)
        return response.choices[0].message.content
    
    def generateMemory(self, index = -1):
        if(len(self.thoughts) == 0):
            print("Not thoughts for agent" + self.name)
            return
        prompt = self.prepMemoryPrompt(index)
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "system", "content": "You are the following character, respond accordingly: " + self.description}, # Corrected to use single string role
                {"role": "user", "content": prompt}
            ]
        )
        rawMemory = (response.choices[0].message.content)
        self.appendMemory(self.thoughts[index], rawMemory)

        return response.choices[0].message.content
    
    def updateMemoryRecency(self):
        if(len(self.memories) >= 1):
            for memory in self.memories:
                memory.reduceRecencyScore()

class Thought:
    nextThoughtId = 0

    def __init__(self, dateTimeObj, thoughtString="N/A", sLoc = (1,1)):
        self.thoughtId = Thought.nextThoughtId  
        Thought.nextThoughtId += 1
        self.dayInt = int(dateTimeObj.strftime("%Y%m%d"))
        self.timeInt = int(dateTimeObj.strftime("%H%M"))
        self.startLoc = sLoc

        startJsonIndex = thoughtString.find("{")
        endJsonIndex = thoughtString.find("}")+1
        #print(f"JSON String:\n{thoughtString}")
        #print(f"JSON String Formatted:\n{thoughtString[startJsonIndex:endJsonIndex+1]}")
        
        jsonObj = json.loads(thoughtString[startJsonIndex:endJsonIndex+1])
        self.thoughtText = jsonObj["thought"]
        self.action = jsonObj["action_description"]
        self.location = jsonObj["target_location"]
        self.locationDesc = jsonObj["target_location_description"]
        self.endLoc = tuple(reversed(tuple(jsonObj["target_coordinates"])))

    def __str__(self):
        return (
            f"Thought ID: {self.thoughtId}\n"
            f"Date: {self.dayInt}\n"
            f"Time: {self.timeInt}\n"
            f"Start Location: {self.startLoc}\n"
            f"Thought: {self.thoughtText}\n"
            f"Action: {self.action}\n"
            f"Location: {self.location}\n"
            f"Location Description: {self.locationDesc}\n"
            f"End Location: {self.endLoc}\n"
        )






        

class Memory:
    memorySummarizePrompt = "Being brief, Summarize your provided thought in the first past tense along with a location."
    memoryScorePrompt = """
    Provide sentimentScore, frequencyScore, and importanceScore for the given thought.

    sentimentScore (0-10): Emotional Intensity

    High (7-10): Strong emotions (joy, excitement, love, fear, anger, sadness). Major life events, passionate moments, traumatic experiences. Example: "I won the lottery!"
    Medium (4-6): Moderate emotional involvement. Everyday events (pleasant conversation, frustrating commute). Example: "I had lunch with a friend."
    Low (0-3): Largely factual or unemotional. Routine actions (brushing teeth, noting the weather). Example: "The meeting is at 2 PM."
    frequencyScore (0-10): Recall Frequency

    High (7-10): Frequently recalled memories. Recurring problems, cherished childhood memories.
    Medium (4-6): Occasionally recalled memories.
    Low (0-3): Rarely recalled memories. This score can increase with each recall, up to a maximum.
    importanceScore (0-10): Personal Importance

    High (7-10): Significant impact on life, identity, or goals. Graduating college, getting married, major accomplishments.
    Medium (4-6): Relevant but not life-changing.
    Low (0-3): Trivial or insignificant.
    """
    memoryJsonPrompt = """
        Provide your response in JSON format, like this example:

        {
        "memoryDesc": "...",
        "location": "...",
        "sentimentScore": 2.5,
        "frequencyScore": 8,
        "importanceScore": 3.2
        }

    """

    def __init__(self, thoughtObject, memoryString="N/A"):
        self.memoryId = thoughtObject.thoughtId
        self.dayInt = thoughtObject.dayInt
        self.timeInt = thoughtObject.timeInt
        startJsonIndex = memoryString.find("{")
        endJsonIndex = memoryString.find("}")+1
        #print(f"JSON String:\n{memoryString}")
        #print(f"JSON String Formatted:\n{memoryString[startJsonIndex:endJsonIndex+1]}")
        
        jsonObj = json.loads(memoryString[startJsonIndex:endJsonIndex+1])
        self.memoryDesc = jsonObj["memoryDesc"]
        self.location = jsonObj["location"]
        self.sentimentScore = jsonObj["sentimentScore"]
        self.frequencyScore = jsonObj["frequencyScore"]
        self.importanceScore = jsonObj["importanceScore"]
        self.recencyScore = 10.0
        self.totalScore = self.getTotalMemoryScore()

    def __str__(self):
        return (
            f"Memory ID: {self.memoryId}\n"
            f"Memory Date: {self.dayInt}\n"
            f"Time: {self.timeInt}\n"
            f"Start Location: {self.location}\n"
            f"Memory Desc: {self.memoryDesc}\n"
            f"Sentiment Score: {self.sentimentScore}\n"
            f"Frequency Score: {self.frequencyScore}\n"
            f"Importance Score: {self.importanceScore}\n"
            f"Overall Memory Score: {self.totalScore}\n"
        )
    
    def reduceRecencyScore(self): #Meant to be ran every 15 minutes
        if self.recencyScore > 1.1:
            self.recencyScore -= .007
            self.totalScore = self.getTotalMemoryScore()
    
    def getTotalMemoryScore(self):
        return self.sentimentScore * self.frequencyScore * self.importanceScore * self.recencyScore
    

class Conversation:
    nextConvId = 0
    def __init__(self, startAgent, jsonObj, dateTimeObj, targetAgent):
        self.ConversationId = Conversation.nextConvId
        self.startAgentId = startAgent.id
        self.startAgentName = startAgent.name
        self.targetAgentId = targetAgent.id
        self.targetAgentName = targetAgent.name
        self.startAgentObj = startAgent
        self.targetAgentObj = targetAgent
        self.dateTimeObj = dateTimeObj
        self.initMessage = jsonObj["initial_message"]
        self.targetCoordinate = jsonObj["target_coordinates"]
        self.rawConversation = self.generateConversation()
        
        Conversation.nextConvId += 1

    def generateConversation(self):
        role = "You are facilitating conversation between two agents. " + self.startAgentName + " and " + self.targetAgentName + ". The first message from " + self.startAgentName + " is : " + self.initMessage
        instruct = "Generate a conversation between the two agents using the following descriptions and top memories."
        startAgentDesc = self.startAgentObj.description + " Top Memories: " + self.startAgentObj.getHighestMemoriesString()
        targetAgentDesc = self.targetAgentObj.description + " Top Memories: " + self.targetAgentObj.getHighestMemoriesString()
        outputGuidance = "output the conversation in the following JSON format" + """
        {
        "turns": [
            {
            "speaker": "Agent1", 
            "text": "Initial statement or question to start the conversation.",
            "emotion": "neutral or appropriate emotion"
            },
            {
            "speaker": "Agent2",
            "text": "Response to the initial statement or question.",
            "emotion": "neutral or appropriate emotion"
            },
            {
            "speaker": "Agent1",
            "text": "Further response or a new statement/question.",
            "emotion": "neutral or appropriate emotion"
            }
            // ... more turns
        ]
        }    
        """
        contentOutput = instruct + startAgentDesc + targetAgentDesc + outputGuidance
        


        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "system", "content": role}, # Corrected to use single string role
                {"role": "user", "content": contentOutput}
            ]
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content