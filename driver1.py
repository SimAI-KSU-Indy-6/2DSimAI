
from AgentClass import Agent, Thought, Memory
import mapFile
import datetime

agents = []
startTime = datetime.datetime(2024, 10, 27, 10, 0, 0)
increment15m = datetime.timedelta(minutes=15)
increment6h = datetime.timedelta(hours=6)

dateString = startTime.strftime('%A, %B %d, %Y')
timeString = startTime.strftime('%I:%M %p')

#Make Agent instance  
agents.append(Agent( #Name, Desc, Location
        "Joey",
        "Joey, a 22-year-old college student, lives for the dream of rock stardom.  His beat-up Epiphone Les Paul is his constant companion, a conduit for the raw energy he admires in his idol, Jimmy Page.  Hes a quiet, laid-back guy until the conversation turns to music, at which point his passion ignites.  Constantly daydreaming of stadium lights and roaring crowds, Joey channels his Zeppelin-inspired ambitions into original riffs, aiming for epic compositions.  He struggles to find bandmates who share his deep appreciation for classic rock; most of his peers are into more contemporary genres.  Driven by the desire to create something legendary, something timeless, Joey seeks to resurrect rock and roll with his own music, fueled by a belief in its enduring power.",
        (6,5)
    )
)
for agent in agents:
    for i in range(6):
        #mapFile already loaded
        agent.update_map_info(mapFile.allMap, mapFile.tile_definitions)
        agent.generateThoughtResponse(dateString, timeString, startTime)

        print(agent.getHighestMemories())
        print(str(agent.thoughts))
        #TODO Fix string outs and feed back into future prompting.

        agent.generateMemory()
