from AgentClass import Agent, Thought, Memory
import mapFile
import datetime

agents = []
currTime = datetime.datetime(2024, 10, 27, 10, 0, 0)
increment15m = datetime.timedelta(minutes=15)
increment6h = datetime.timedelta(hours=6)

#dateString = startTime.strftime('%A, %B %d, %Y')
#timeString = startTime.strftime('%I:%M %p')

def getDateString(startTime): return startTime.strftime('%A, %B %d, %Y')
def getTimeString(startTime): return startTime.strftime('%I:%M %p')

#Make Agent instance  
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

for i in range(8):
    currTime += increment15m
    for agent in agents:
        agent.updateMemoryRecency()
        #mapFile already loaded
        agent.update_map_info(mapFile.allMap, mapFile.tile_definitions)
        agent.generateThoughtResponse(getDateString(currTime), getTimeString(currTime), currTime, agents)

        currMemories = agent.getHighestMemories()

        print("MEMORIES ---------------------")
        for memory in currMemories:
            print(str(memory) + "\n")

        print("THOUGHTS ---------------------")
        for thought in agent.thoughts:
            print(str(thought) + "\n")

        #TODO Add memories to both agents after a conversation takes place.

        agent.generateMemory()
