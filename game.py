from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Cirle Arena"

def battle(hero: Hero, enemy):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")
    

    goblin = Goblin("Gubble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Scribble")

    bianca = Hero("bianca")
    bianca.AttackNumber = bianca.attack()
    print("Bianca screams: GOTCHA")
    if goblin.health > 0:
        goblinAttackNumber = goblin.attack()
        print("WATCH OUT BIANCA IT'S COMING FOR YOU")
        bianca.take_damage(goblinAttackNumber)
    battle(bianca,goblin)


    aragorn = Hero("Aragorn")
    heroAttack = aragorn.attack()

if __name__ == "__main__":
    main()
