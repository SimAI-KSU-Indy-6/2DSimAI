#Test file to get ollama python API running on local machine
from ollama import chat
from ollama import ChatResponse

descriptions = [
    'Joey, a 22-year-old college student, lives for the dream of rock stardom.  His beat-up Epiphone Les Paul is his constant companion, a conduit for the raw energy he admires in his idol, Jimmy Page.  Hes a quiet, laid-back guy until the conversation turns to music, at which point his passion ignites.  Constantly daydreaming of stadium lights and roaring crowds, Joey channels his Zeppelin-inspired ambitions into original riffs, aiming for epic compositions.  He struggles to find bandmates who share his deep appreciation for classic rock; most of his peers are into more contemporary genres.  Driven by the desire to create something legendary, something timeless, Joey seeks to resurrect rock and roll with his own music, fueled by a belief in its enduring power.'
]
time = ["12:30pm"]
location = ["In bed", "at school", "walking to class"]
prompt = [f"You are the following character: {descriptions[0]}, It is currently {time[0]} and you are currently {location[0]}, provide a single short thought as if you were the character in this situation."]


response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=[
  {
    'role': 'user',
    'content': prompt[0],
  },
])

print(response['message']['content'])

#print(prompt[0])