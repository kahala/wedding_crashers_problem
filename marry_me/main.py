# Reference: https://github.com/QwasarSV/eng_labs_marry_me/tree/lite
import json
import asyncio
global stress_level
from enum import IntEnum
from pydantic import BaseModel, Field
from typing import Literal
import time

# Your best friend is getting married and put you in charge of 
# coordination. Build a small event-driven simulation that receives 
# wedding incidents, routes them to the right team, 
# and tracks guest stress when events go unhandled.

class PriorityLevel(IntEnum):
     high = 2              #5 seconds
     medium = 1           #10 seconds
     low = 0              #15 seconds

PROCESSING_TIMES = {
     PriorityLevel.high: 15,
     PriorityLevel.medium: 10,
     PriorityLevel.low: 5
}

class Event(BaseModel):
      id: int = Field(..., desrciption="Unique event ID")
      event_type: str
      priority: PriorityLevel 
      description: str
      timestamp: float

# 1)Coordinator — Receives and 
# validates incoming events, then forwards them to the appropriate team.
def coordinator():
     pass
    
      #pydantic/optionals to make sure the data shape is ok...
      #try-catch


# 2)Teams — Each team has a fixed pool of workers. When an event arrives, 
# the team assigns an idle worker. 
# If no worker is available, the event waits in a queue.
    #queue of workers 
    # w0, w1, w2, w3, w4

    #Workers
# current_status: Idle | Working
# Handling an event takes 3 seconds, then the worker returns to Idle.
class Worker_Status(IntEnum):
    IDLE = 0,
    WORKING = 1


class Worker(BaseModel):
    name: str
    time_to_expire: int = 3
    status: Worker_Status = Worker_Status.IDLE

        
    def countdown(time_to_expire){
        if(time_to_expire > 3){
             stress_level += 1
        } 
    }

async def handle_event(worker)



#3) Stress Tracking — If an event is not handled before its priority deadline expires, 
#it is discarded and the global stress level increments by 1.



# Simulation
# The simulation runs for 60 seconds.
# Events are provided as a JSON array (input file), each with a timestamp indicating when it arrives.
# At the end, print:
# Total events received
# Total events handled
# Total events expired
# Final stress level (= number of expired events)


#Input:
# #[ 
# {"id": 1, "event_type": "brawl", "priority": "high", "description": "fight near the bar", "timestamp": 2.0}, 
# {"id": 2, "event_type": "bad_food", "priority": "medium", "description": "cold soup", "timestamp": 3.0}, 
# {"id": 3, "event_type": "dirty_table", "priority": "low", "description": "table 5 is a mess", "timestamp": 4.0}, 
# {"id": 4, "event_type": "brawl", "priority": "high", "description": "another fight", "timestamp": 5.0}, 
# {"id": 5, "event_type": "feeling_ill", "priority": "high", "description": "guest fainted", "timestamp": 5.5} 
# ]
async def main():
    stress_level = 0

    # 1) take in json file and parse into a list of event objects
    try: 
        with open('events.json', 'r') as file:
              raw_data = json.load(file)
    except FileNotFoundError:
        print("File 'events.json' not found.")
        return
    
    task_queue = asyncio.Queue()

    # 2) process objects in a loop of 60 seconds
    #       for(int i = 0; i < 60; i++)
    # sort them into a priority queue by priority >>> maybe set as enums

if __name__ == "__main__":
     main()
 
 
#At the end print:
Total events received
Total events handled
Total events expired
Final stress level (= number of expired events)