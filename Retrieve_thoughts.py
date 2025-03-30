#This module is meant to be imported and used anywhere in the project to access and process agent thoughts from database
#To import this module type at top -> from retrieve_thoughts import get_recent_thoughts, parse_thought, get_thought_by_id

# ** Current Functions: **
# get_recent_thoughts() → Fetches a list of the most recent thoughts from the Flask API.
# parse_thought(row) → Takes a single database row and returns the structured thought as a dictionary.
# filter_thoughts_by_location(location) → Filters and returns all thoughts from a given start_location (e.g., "(6,5)")
# get_thought_by_id(thought_id) → Returns a specific thought row by its ID.

# Running this python file will call get_recent_thoughts() as an example

import requests
import re
import json

def get_recent_thoughts():
    try:
        response = requests.get("https://flask-app-api-bthdc4bzbgcfbbfp.centralus-01.azurewebsites.net/thoughts")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching thoughts: {e}")
        return []

def parse_thought(row):
    raw_thought = row.get('thought', '')
    clean_thought = re.sub(r"^```(?:json)?|```$", "", raw_thought.strip(), flags=re.IGNORECASE | re.MULTILINE).strip()
    try:
        return json.loads(clean_thought)
    except json.JSONDecodeError:
        return {}

def filter_thoughts_by_location(location):
    return [row for row in get_recent_thoughts() if row.get('start_location') == location]

def get_thought_by_id(thought_id):
    thoughts = get_recent_thoughts()
    for row in thoughts:
        if str(row.get('thoughtId')) == str(thought_id):
            return row
    return None

if __name__ == "__main__":
    recent_thoughts = get_recent_thoughts()

    for idx, row in enumerate(recent_thoughts, start=1):
        thought_data = parse_thought(row)

        print(f"\n--- Thought #{idx} ---")
        print(f"Date: {row.get('date')}")
        print(f"Time: {row.get('time')}")
        print(f"Start Location: {row.get('start_location')}")
        print(f"Thought: {thought_data.get('thought', 'N/A')}")
        print(f"Action Description: {thought_data.get('action_description', 'N/A')}")
        print(f"Target Location: {thought_data.get('target_location', 'N/A')}")
        print(f"Target Location Description: {thought_data.get('target_location_description', 'N/A')}")
        print(f"End Location: {thought_data.get('target_coordinates', 'N/A')}")


