# Reference: https://github.com/QwasarSV/eng_labs_marry_me/tree/lite
import json
import asyncio
global stress_level
from enum import IntEnum
from pydantic import BaseModel, Field
from typing import Literal, List
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

    def __init(self, id, event_type, priority, description, timestamp):
        self.id = id
        self.event_type = event_type
        self.priority = priority
        self.description = description
        self.timestamp = timestamp
      
    async def process_event:
    pass
    
           


# 2)Teams — Each team has a fixed pool of workers. When an event arrives, 
# the team assigns an idle worker. 
# If no worker is available, the event waits in a queue.
    #queue of workers 
    # w0, w1, w2

    #Workers
# current_status: Idle | Working
# Handling an event takes 3 seconds, then the worker returns to Idle.
class Worker_Status(IntEnum):
    IDLE = 0,
    WORKING = 1


# Event Handling takes 3 seconds
class Worker(BaseModel):
    name: str
    status: Worker_Status = Worker_Status.IDLE

    def __init__(self, name: str):
         self.name = name


async def validate_event(raw_item):
     return raw_item
    

# 1)Coordinator — Receives and 
# validates incoming events, then forwards them to the appropriate team.
async def coordinator(event : Event):
     pass
    
      #pydantic/optionals to make sure the data shape is ok...
      #try-catch


#decide which worker to send the event
async def handle_event(event):
    pass 



#3) Stress Tracking — If an event is not handled before its priority deadline expires, 
#it is discarded and the global stress level increments by 1.

def print_results():
    pass
# Total events received
# Total events handled
# Total events expired
# Final stress level (= number of expired events)


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

    task_queue = asyncio.Queue()
    
    all_worker_tasks = []
    
    # 1) take in json file and parse into a list of event objects
    try: 
        with open('events.json', 'r') as file:
              raw_data = json.load(file)
    except FileNotFoundError:
        print("File 'events.json' not found.")
        return

         # 2) Create 3 teams of 2 workers
    #Define Teams
    team_names = ["Security", "Catering", "Waiters"]
    workers : List[Worker] = [] 

    # 2 workers per team
    for name in team_names:
        for i in range(1, 3): 
            w = Worker(worker_id=i, team_name = name)
            # create task >>> 
            #asyncio.create_task(w.work(queue)) ???
            workers.append(w)

    # 3) Validate information and add to task queue
    for item in raw_data: 
        try:
            clean_item = validate_event(item)          
            ###put into queue
            await task_queue.put(Event(**clean_item)) 
        except ValueError as e:
             print(f"Skipping bad data: {e}")

    # 4) In each group need to have worker 1, worker 2 and a queue for
    # the incoming events. It seems that it would be most efficient
    # to simulate everything using a clock going up by 0.1. 

    # Once an event goes into the queue >>> immediately calculate how
    # long it will take until it ends

    # OR COULD ACTUALLY JUST PRE-SORT ALL THE EVENTS INTO 3 QUEUES 
    # and then could feed them in the 2-worker teams

    # Could have 3 queues for Sercurity, Catering and Waiters
    # and then calculate those individually... then don't need to update
    # each 0.1 







    print_results()

if __name__ == "__main__":
     main()

