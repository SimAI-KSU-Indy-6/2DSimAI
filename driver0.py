from openai import OpenAI
import os
from dotenv import load_dotenv
from AgentClass import Agent, Thought, Memory
import mapFile
import datetime
import requests  #Added to send thoughts to Flask API

# Flask API URL for storing thoughts
API_URL = "http://127.0.0.1:5000/add_thought"  # Change to public IP if remote

agents = []

load_dotenv()
gemini_key = os.environ["GEMINI_KEY"]

startTime = datetime.datetime(2024, 10, 27, 10, 0, 0)
increment15m = datetime.timedelta(minutes=15)
increment6h = datetime.timedelta(hours=6)

dateString = startTime.strftime('%A, %B %d, %Y')
timeString = startTime.strftime('%I:%M %p')

print(dateString + "\n" + timeString)

# Make Agent Instance
agents.append(Agent(
    "Joey",
    "Joey, a 22-year-old college student, lives for the dream of rock stardom. His beat-up Epiphone Les Paul is his constant companion, a conduit for the raw energy he admires in his idol, Jimmy Page...",
    (6,5)
))

prompts = []

for agent in agents:
    agent.update_map_info(mapFile.allMap, mapFile.tile_definitions)
    currentAgentMap = mapFile.agentMap(agent.location[0], agent.location[1])
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
            {"role": "system", "content": agents[0].getRolePrompt(dateString + " " + timeString)},
            {"role": "user", "content": prompts[0]}
        ]
    )

    generated_thought = response.choices[0].message.content
    print("Gemini Response:--------------------")
    print(generated_thought)

    # Store Thought in Agent
    agents[0].appendThought(generated_thought, startTime)
    thought_object = agents[0].thoughts[0]

    print(thought_object)

    # Convert Thought to API Format
    thought_data = {
        "date": startTime.strftime("%Y-%m-%d"),
        "time": startTime.strftime("%H:%M:%S"),
        "start_location": "(6,5)",  # Adjust as needed
        "thought": generated_thought,
        "action_description": "Joey reflects on his musical journey.",
        "target_location": "(5,3)",  # Adjust as needed
        "target_location_description": "Living Room",
        "target_coordinates": "(5,3)"  # Same as target location
    }

    # Send Thought to Flask API
    response = requests.post(API_URL, json=thought_data)

    if response.status_code == 200:
        print("Thought stored successfully!")
    else:
        print("Failed to store thought:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")  #Handle any exceptions
