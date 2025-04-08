from hero import Hero
from monster import Monster

def start_fight(hero, monster):
    print("Fight begins!")
    # Hero attacks and gets the attack value
    hero_attack = hero.hero_attacks()
    # Monster attacks and gets the attack value
    monster_attack = monster.monster_attacks()
    
    # Compare the attack values and print the outcome of the fight
    if hero_attack > monster_attack:
        print("Hero wins the round!")
    elif monster_attack > hero_attack:
        print("Monster wins the round!")
    else:
        print("It's a tie!")