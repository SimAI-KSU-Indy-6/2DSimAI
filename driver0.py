from openai import OpenAI
import os
from dotenv import load_dotenv
from AgentClass import Agent, Thought, Memory
import mapFile
import datetime

agents = []

load_dotenv()
gemini_key = os.environ["GEMINI_KEY"]

startTime = datetime.datetime(2024, 10, 27, 10, 0, 0)
#Operating hours of simulation will be 6AM - 12PM (increment by 15min and once by 6 hours)
increment15m = datetime.timedelta(minutes=15)
increment6h = datetime.timedelta(hours=6)

dateString = startTime.strftime('%A, %B %d, %Y')
timeString = startTime.strftime('%I:%M %p')

print(dateString + "\n" + timeString)

#Make Agent instance  
agents.append(Agent( #Name, Desc, Location
        "Joey",
        "Joey, a 22-year-old college student, lives for the dream of rock stardom.  His beat-up Epiphone Les Paul is his constant companion, a conduit for the raw energy he admires in his idol, Jimmy Page.  Hes a quiet, laid-back guy until the conversation turns to music, at which point his passion ignites.  Constantly daydreaming of stadium lights and roaring crowds, Joey channels his Zeppelin-inspired ambitions into original riffs, aiming for epic compositions.  He struggles to find bandmates who share his deep appreciation for classic rock; most of his peers are into more contemporary genres.  Driven by the desire to create something legendary, something timeless, Joey seeks to resurrect rock and roll with his own music, fueled by a belief in its enduring power.",
        (6,5)
    )
)

prompts = []

for agent in agents:
    agent.update_map_info(mapFile.allMap, mapFile.tile_definitions)

    currentAgentMap = mapFile.agentMap(agent.location[0], agent.location[1]) #split x and y coordinates of location variable
    print("\nAGENT INFO::-------------------------")
    print(agent)
    
    prompts.append(agent.prepPrompt(currentAgentMap, mapFile.tileDefToString))

print("PROMPT:------------------------")
print(prompts[0])

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

try:
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role": "system", "content": agents[0].getRolePrompt(dateString + " " + timeString)}, # Corrected to use single string role
            {"role": "user", "content": prompts[0]}
        ]
    )
    print("Gemini Response:--------------------")
    print(response.choices[0].message.content)

    agents[0].appendThought(response.choices[0].message.content, startTime)

    memoryPrompt = []
    memoryPrompt.append(agents[0].prepMemoryPrompt())

    print(agents[0].thoughts[0])

    print(memoryPrompt)

    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role": "system", "content": "You are the following character, respond accordingly: " + agents[0].description}, # Corrected to use single string role
            {"role": "user", "content": memoryPrompt[-1]}
        ]
    )

    currentRawMemory = response.choices[0].message.content
    agents[0].appendMemory(agents[0].thoughts[-1], currentRawMemory)

    print("MEMORY Object ----------------------------------")

    print(agents[0].memories[-1])

    


except Exception as e:
    print(f"An error occurred: {e}") # Handle and print any exceptions