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

