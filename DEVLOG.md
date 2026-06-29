## June 21, 2026

### SLOT 1

### What I Did:
I read all the 5 started notebooks that were available on the contest discussion tab. Created a Github Repo, MIT License, folder structure, DEVLOG.md and I also played the pokemon tcg game to get better understanding of what this game is about.

### What I Understood:
The competition uses a cabt engine that handles all game rules. Our agent just picks from a list of legal options each turn. The official RL+MCTS kit already has a working Transformer + MCTS.
The gap I found in the kit is that the opponents cards get filled with snorlax dummies.

### Next:
Install cg-lib locally and run the random agent, explore all_card_data().


## June 26-27, 2026

### SLOT 1

### What I Did:
Installed cg-lib from competition sample_submission folder, Ran 01_explore_cards.ipynb and inspected card data API

### What I Understood:
- 1267 total cards
- Card object fields: cardId, name, cardType, hp, retreatCost,
weakness, resistance, energyType, basic/stage1/stage2/ex/megaEx/tera aceSpec flags, evolvesFrom, skills, attacks
- cardType values: 0=Pokemon, 5=Basic Energy, 6=Special Energy, 3=Trainer (to confirm)
- attacks on a card = list of integer IDs, not objects
- Attack object fields: attackId, name, text, damage, energies (list of energy type IDs, 0=colorless)
- energyType integers: 1=Grass, 2=Fire, 3=Water, 4=Lightning, 5=Psychic, 6=Fighting, 7=Darkness, 8=Metal, 9=Dragon, 0=Colorless
- skills = Abilities, stored as Skill objects with name and text
- all_card_data() and all_attack() are the two main API calls for card metadata

### Next:
Read sample main.py from data/sample to understand how obs_dict is structured and how the agent() function works.

## June 28, 2026

### SLOT 1

### What I Did:
- Studied the 5 starter notebooks and analysed them
- Verified all required cards and their Id's from the competition pool
- Constructed a legal 60-card Dragapult ex/ Dusknoir deck
-  Created the initial deck.csv file containing the deck list

### What I Understood:
- Choosing a strong, established meta deck reduces uncertainty when evaluation AI performance
- Dragapult ex/ Dusknoir has a clear starategic game plan, strong choice for MCTS and opponent modelling.
- Competition deck are represented as a list of 60 card ID's
- Before implementing the agent, all card ID's must be verified against the competition card database.

### Next:
- Read the sample main.py
- Understand the strucutre of agent(obs_dict)
- Create the first minimal main.py that loads deck.csv and successfully runs a game without crashing.

## June 29, 2026

### SLOT 1

### What I Did:
- Created the initial `main.py` agent architecture.
- Added deck loading and card database lookup system.
- Defined deck constants and global game-state variables.
- Implemented the core `agent()` function skeleton.
- Added basic game state parsing:
    - Active Pokemon
    - Bench
    - Hand
    - Discard pile
- Implemented a simple heuristic scoreing system for:
    - Attack
    - Evolution
    - Ability
    - Retreat
    - Energy attachment
    - Card play actions
- Added placeholder helper functions for future strategic logic

**Status:** Base agent framework completed

### What I Understood:
- CABT agents operate as a rule-based scoring systems over legal actions.
- `obs.select.option` contains all legal actions available during a decision step
- The Dragapult/Dusknoir strategy can be added incrementally on top of a generic action-selection engine.

### Next:
- Implement setup heuristicsL
    - Other pokemons opening strategies and search and evolution priorities
    - Basic energy attachment logic
