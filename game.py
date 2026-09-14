from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Cirle Arena"


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
    goblin.take_damage(bianca.AttackNumber)
    if goblin.health > 0:
        goblinAttackNumber = goblin.attack()
        print("WATCH OUT BIANCA IT'S COMING FOR YOU")
        bianca.take_damage(goblinAttackNumber)
    


    aragorn = Hero("Aragorn")
    heroAttack = aragorn.attack()

if __name__ == "__main__":
    main()
