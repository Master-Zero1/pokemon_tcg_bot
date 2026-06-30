import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cg.game import battle_start, battle_select, battle_finish
from cg.api import to_observation_class
from main import agent, my_deck
import random

def random_agent(obs_dict):
    obs = to_observation_class(obs_dict)

    if obs.select is None:
        return my_deck
    
    n = len(obs.select.option)
    k = min(obs.select.maxCount, n)

    return random.sample(range(n), k)

wins = 0

for i in range(100):
    obs, start_data = battle_start(my_deck, my_deck)

    if start_data.errorPlayer >= 0:
        print("DECK ERROR")
        break

    while obs["current"]["result"] < 0:
        if obs["current"]["yourIndex"] == 0:
            selected = agent(obs)
        else:
            selected = random_agent(obs)

        obs = battle_select(selected)

    battle_finish()

    if obs["current"]["result"] == 0:
        wins += 1

print("RESULT:", obs["current"]["result"])
print(f"Wins: {wins}/100")