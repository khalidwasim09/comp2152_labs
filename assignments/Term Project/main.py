# Aisha Shali
#101443265

from hero import Hero
from monster import Monster
from function import start_fight

def main():
    # Create a Hero object
    hero = Hero()
    # Create a Monster object
    monster = Monster()

    # Print out initial combat stats for both hero and monster
    print(f"Hero's Combat Strength: {hero.combat_strength}, Health Points: {hero.health_points}")
    print(f"Monster's Combat Strength: {monster.combat_strength}, Health Points: {monster.health_points}")
    
    # Start the fight between hero and monster
    start_fight(hero, monster)

if __name__ == "__main__":
    # Run the main function
    main()