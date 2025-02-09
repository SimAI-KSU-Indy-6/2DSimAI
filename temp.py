# Test file to get ollama python API running on local machine
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

allMap = [
    ["E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E",	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	"P",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"P",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"P",	"P",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"W",	"W",	"W",	"D",	"W",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	"W",	"W",	"W",	"W",	"W",	"D",	"D",	"W",	"W",	"W",	"W",	"W",	"W",	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"De",	" ", 	"D",	" ", 	" ", 	"Co",	"Co",	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"C",	"C",	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
    ["E",	" ", 	" ", 	" ", 	"W",	"CHAR",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"W",	" ", 	"I1",	" ", 	"I2",	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	" ", 	"I6",	" ", 	"W",	" ", 	" ", 	" ", 	" ", 	"E"],
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

tile_definitions = {
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

#print(str(tile_definitions))
tileDefToString = ''.join(f"{k} - {v} | " for k, v in tile_definitions.items())


def padList(twoDList):
    for rowIndex in range(len(twoDList)):
        for colIndex in range(len(twoDList[rowIndex])):
            item = twoDList[rowIndex][colIndex]
            padding = 4 - len(item)  # Calculate needed padding. 4 is the target length
            if padding > 0:
                twoDList[rowIndex][colIndex] = item + " " * padding  # Efficient padding
            elif padding < 0:
                twoDList[rowIndex][colIndex] = item[:4] # Truncate if longer than 4.  Corrected truncation length


descriptions = [
    'Joey, a 22-year-old college student, lives for the dream of rock stardom.  His beat-up Epiphone Les Paul is his constant companion, a conduit for the raw energy he admires in his idol, Jimmy Page.  Hes a quiet, laid-back guy until the conversation turns to music, at which point his passion ignites.  Constantly daydreaming of stadium lights and roaring crowds, Joey channels his Zeppelin-inspired ambitions into original riffs, aiming for epic compositions.  He struggles to find bandmates who share his deep appreciation for classic rock; most of his peers are into more contemporary genres.  Driven by the desire to create something legendary, something timeless, Joey seeks to resurrect rock and roll with his own music, fueled by a belief in its enduring power.'
]
time = ["12:30pm"]
location = ["In bed"]  # Removed extra options for simplicity in the prompt
role = f"You are the following character: {descriptions[0]}, It is currently {time[0]} and you are currently {location[0]}" # Made role a single string

padList(allMap)

mapContext = "Use the following map and map key to get context for your environment: \n" + '\n'.join(map(''.join, allMap)) + "\nKey: " + tileDefToString

jsonFormatInstruct = """Provide your response in JSON format, like this example:

```json
{
  "thought": "...",
  "action_description": "...",
  "target_location": "...",
  "target_coordinates": [row, column]
}
"""

prompt = mapContext + "\nProvide a single short thought as if you were the character in this situation and detail the next movement of the character based on the map and current position." + jsonFormatInstruct

gemini_key = os.environ["GEMINI_KEY"]

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


  # Pad the map *before* printing or using it in the prompt

#print('\n'.join(map(''.join, allMap))) # Print padded map.

try:
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role": "system", "content": role}, # Corrected to use single string role
            {"role": "user", "content": prompt}
        ]
    )

    print("Initial Role:\n", role)
    print("\nInitial Prompt:\n", prompt)

    print("\nGemini Response:\n", response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}") # Handle and print any exceptions