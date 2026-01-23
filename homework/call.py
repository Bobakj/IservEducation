import classes


enemy = classes.Character(health=100)
enemy_archer = classes.Archer(health=60, arrow_amount=10)

choise = 0
while choise != 4:
    choise = int(input("Напишите:\n1.Если хотите добавить хп персонажу\n2.Нанести урон персонажу\n3.Выстрелить стрелой\n4.Выйти\n\n"))
    if choise == 1:
        health = enemy.add_health(10)
        print(f"[+] Current health: {health}")

    elif choise == 2:
        hit_health = enemy.hit_damage(10)
        print(f"[-] Current health: {hit_health}")

    elif choise == 3:
        shoot = enemy_archer.shoot()
        print(f"Current arrow: {shoot}")