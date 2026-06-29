import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from collections import defaultdict

from cg.api import AreaType, CardType, Log, Observation, OptionType, Card, Pokemon, all_card_data, to_observation_class

"""
Dragapult ex / Dusknoir Deck

"""

#Load deck.csv in the dataset
file_path = "deck.csv"
if not os.path.exists(file_path):
    file_path = "/kaggle_simulations/agent/" + file_path
with open(file_path, "r") as file:
    csv = file.read().split("\n")
my_deck = []
for i in range(60):
    my_deck.append(int(csv[i]))

#Load all card data from the API
all_card = all_card_data()

#Create a lookup table (dictionary) to quickly access card data by its cardId
card_table = {c.cardId:c for c in all_card}

#Decklist
Dreepy = 119 # x4
Drakloak = 120  # x4
Dragapult_ex = 121  # x3
Duskull = 131 # x2
Dusclops = 132 # x2
Dusknoir = 133 # x1
Budew = 235 # x2
Munkidori = 112 # x1
Latias_ex = 184 # x1
Fezandipiti_ex = 140 # x1
Bloodmoon_Ursaluna_ex = 44 # x1
Hawlucha = 1055 # x1
Lillie_s_Determination = 1227 # x4
Boss_s_Orders = 1182 # x3
Bianca_s_Devotion = 1190 # x1
Judge = 1213 # x3
Hilda = 1225 # x1
Lucian = 1237 # x1
Buddy_Buddy_Poffin = 1086 # x4
Poké_Pad = 1152 # x4
Night_Stretcher = 1097  # x2
Switch = 1123 # x1
Ultra_Ball = 1121 # x1
Enhanced_Hammer = 1081 # x1
Crushing_Hammer = 1120 # x3
Unfair_Stamp = 1080 # x1
Basic_Psychic_Energy = 5 # x7

UNNECESSARY = -100000

class AttackPlan:
    def __init__(self):
        self.attack: int = -1
        self.counter: list[int] = []

can_switch = False
can_attack = False
can_main_attack = False
can_energy_attach = False
use_support = 0
bench_attacker = False
pre_turn_log: list[Log] = []
current_turn_log: list[Log] = []

prize: list[int] = []
card_counts: defaultdict[int, int] = defaultdict(int)
serial_set: set[int] = set()
plan_a = AttackPlan()
plan_b = AttackPlan()

def no_damage_dex(id: int) -> bool:
    return False

def no_damage_counter(pokemon: Pokemon) -> bool:
    return False

def prize_count(pokemon: Pokemon, is_attack_damage: bool) -> int:
    return 1

def pokemon_score(pokemon: Pokemon, is_attack_damage: bool) -> int:
    return 0

def add_card_count(card: Card | Pokemon | None, my_index: int):
    pass

def set_card_counts(obs: Observation, my_index: int):
    pass

def get_card(obs: Observation, area: AreaType, index: int, player_index: int) -> Pokemon | Card | None:
    return None

def main_option_proc(obs: Observation, damage: int):
    pass

def agent(obs_dict: dict) -> list[int]:

    obs = to_observation_class(obs_dict)
    if obs.select == None:
        return my_deck
    
    global pre_turn_log
    global current_turn_log
    
    state = obs.current
    select = obs.select
    my_index = state.yourIndex
    my_state = state.players[my_index]
    op_state = state.players[1-my_index]

    global bench_attacker

    field_counts = defaultdict(int)
    hand_counts = defaultdict(int)
    discard_counts = defaultdict(int)

    active_id = 0
    bench_attacker = False
    can_evolve_dreepy = False
    evolve_dreepy_count = 0
    can_evolve_drakloak = False
    for card in my_state.active:
        if card is None:
            continue
        active_id = card.id
        field_counts[card.id] += 1
        if not card.appearThisTurn:
            if card.id == Dreepy:
                can_evolve_dreepy = True
                evolve_dreepy_count += 1
            elif card.id == Drakloak:
                can_evolve_drakloak = True

    for card in my_state.bench:
        field_counts[card.id] += 1
        if not card.appearThisTurn:
            if card.id == Dreepy:
                can_evolve_dreepy = True
                evolve_dreepy_count += 1
            elif card.id == Drakloak:
                can_evolve_drakloak = True
        if card.id == Dragapult_ex and len(card.energies) >= 2:
            bench_attacker = True

    for card in my_state.hand:
        if card is None:
            continue
        hand_counts[card.id] += 1
    
    for card in my_state.discard:
        if card is None:
            continue
        discard_counts[card.id] += 1

    scores = []

    for option in select.option:
        score = 0
        
        if option.type == OptionType.NUMBER:
            score = option.number
        elif option.type == OptionType.YES:
            score = 1
        elif option.type == OptionType.EVOLVE:
            score = 50000
        elif option.type == OptionType.ATTACK:
            score = 50000 
        elif option.type == OptionType.RETREAT:
            if bench_attacker:
                score = 5000
            else:
                score = -1000 #assign a bad score
        elif option.type == OptionType.ABILITY:
            score = 40000
        elif option.type == OptionType.ATTACH:
            score = 20000
        elif option.type == OptionType.PLAY:
            card = None
            if option.index < len(my_state.hand):
                card = my_state.hand[option.index]
            if card:
                data = card_table.get(card.id)
                if data:
                    if data.cardType == CardType.POKEMON:
                        score = 30000
                    elif data.cardType == CardType.SUPPORTER:
                        score = 25000
                    elif data.cardType == CardType.ITEM:
                        score = 20000
                    elif data.cardType == CardType.TOOL:
                        score = 18000
                    elif data.cardType == CardType.STADIUM:
                        score = 17000
                    elif data.cardType == CardType.BASIC_ENERGY:
                        score = 15000
                    else:
                        score = 10000
        elif option.type == OptionType.CARD:
            score = 100
        
        scores.append(score)

    desc = [i for i, _ in sorted(enumerate(scores), key=lambda x: x[1], reverse=True)]

    return desc[:select.maxCount]