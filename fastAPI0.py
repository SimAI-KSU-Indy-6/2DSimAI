from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Tuple, Optional
import datetime
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from AgentClass import Agent
import mapFile

load_dotenv()
gemini_key = os.environ["GEMINI_KEY"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class Location(BaseModel):
    row: int
    col: int

class AgentData(BaseModel):
    id: int 
    name: str
    description: str
    location: Location

class ThoughtResponse(BaseModel):
    thoughtId: int 
    response_type: str
    thought: Optional[str] = None
    action_description: Optional[str] = None
    target_location: Optional[str] = None
    target_location_description: Optional[str] = None
    target_coordinates: Optional[List[int]] = None
    agent: Optional[str] = None
    initial_message: Optional[str] = None

class MemoryData(BaseModel):
    memoryId: int 
    memoryDesc: str
    location: str
    sentimentScore: float
    frequencyScore: float
    importanceScore: float

class ConversationData(BaseModel):
    conversationId: int 
    agent: str
    initial_message: str
    target_coordinates: List[int]

agents = []
currTime = datetime.datetime(2024, 10, 27, 10, 0, 0)
increment15m = datetime.timedelta(minutes=15)
increment6h = datetime.timedelta(hours=6)

def getDateString(startTime):
    return startTime.strftime('%A, %B %d, %Y')

def getTimeString(startTime):
    return startTime.strftime('%I:%M %p')

# Initialize Agents
agents.append(Agent( #Name, Desc, Location
        "Joey",
        "Joey, a 22-year-old college student, lives for the dream of rock stardom.  His beat-up Epiphone Les Paul is his constant companion, a conduit for the raw energy he admires in his idol, Jimmy Page.  Hes a quiet, laid-back guy until the conversation turns to music, at which point his passion ignites.  Constantly daydreaming of stadium lights and roaring crowds, Joey channels his Zeppelin-inspired ambitions into original riffs, aiming for epic compositions.  He struggles to find bandmates who share his deep appreciation for classic rock; most of his peers are into more contemporary genres.  Driven by the desire to create something legendary, something timeless, Joey seeks to resurrect rock and roll with his own music, fueled by a belief in its enduring power.",
        (6,5)
    )
)
agents.append(Agent(
    "Amy",
    "Amy, a 35-year-old freelance graphic designer, finds beauty in the details. Her cluttered but meticulously organized workspace is a testament to her creative process, filled with sketches, Pantone swatches, and half-finished projects. She's a thoughtful listener, always observing and absorbing the nuances of her surroundings. Amy has a sharp eye for color and composition, and a knack for translating abstract ideas into visually compelling designs. She's passionate about sustainability and incorporates eco-friendly practices into her work whenever possible. Though sometimes prone to overthinking, Amy's dedication to her craft and her clients is unwavering. She dreams of one day opening her own design studio, a space where creativity and community can flourish. She loves exploring local art galleries and cafes, finding inspiration in the everyday moments and the stories they hold.",
    (4,8)
))

@app.post("/step_simulation/")
async def step_simulation():
    global currTime, agents
    currTime += increment15m
    for agent in agents:
        agent.updateMemoryRecency()
        agent.update_map_info(mapFile.allMap, mapFile.tile_definitions)
        agent.generateThoughtResponse(getDateString(currTime), getTimeString(currTime), currTime, agents)
        agent.generateMemory()

    return {"message": "Simulation step completed", "time": currTime.isoformat()}

@app.get("/agents/")
async def get_agents():
    return [{"id": agent.id, "name": agent.name, "location": agent.location, "currentMapLocation": agent.currentMapLocation} for agent in agents]

@app.get("/agents/{agent_id}/thoughts/")
async def get_agent_thoughts(agent_id: int):
    agent = next((agent for agent in agents if agent.id == agent_id), None)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return [{"thoughtId": thought.thoughtId, "thoughtText": thought.thoughtText} for thought in agent.thoughts]

@app.get("/agents/{agent_id}/memories/")
async def get_agent_memories(agent_id: int):
    agent = next((agent for agent in agents if agent.id == agent_id), None)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return [{"memoryId": memory.memoryId, "memoryDesc": memory.memoryDesc} for memory in agent.memories]

@app.get("/all_thoughts/")
async def get_all_thoughts():
    all_thoughts = []
    for agent in agents:
        for thought in agent.thoughts:
            all_thoughts.append({
                "agent_id": agent.id,
                "agent_name": agent.name,
                "thoughtId": thought.thoughtId,
                "thoughtText": thought.thoughtText
            })
    return all_thoughts

@app.get("/all_memories/")
async def get_all_memories():
    all_memories = []
    for agent in agents:
        for memory in agent.memories:
            all_memories.append({
                "agent_id": agent.id,
                "agent_name": agent.name,
                "memoryId": memory.memoryId,
                "memoryDesc": memory.memoryDesc
            })
    return all_memories

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)