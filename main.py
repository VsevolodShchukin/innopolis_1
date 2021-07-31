"""Импорт модуля random и sys."""
import random
import sys

monster_counter = 0
hp = random.randint(10, 20)
attack = random.randint(10, 15)


def start_game() -> None:
    """Функция, отображающая стартовые показатели игрока."""
    print(f"Твое здоровье - {hp}, твоя атака - {attack}")


def get_apple() -> None:
    """Функция, генерирующая яблоко. Оно добавляет ед. жизни к показателю hp."""
    global hp
    apple = random.randint(1, 3)
    hp = hp + apple
    print(f"Ты нашел яблоко! Оно увеличило количество жизней на {apple}. Теперь твое количество жизней: {hp}")


def get_sword() -> None:
    """Функция, генерирующая меч. Меч изменяет показатели attack игрока."""
    global attack
    sword = random.randint(10, 25)
    print(f"Ты нашел MEЧ! Его сила атаки - {sword}.")
    decision = input("Введи 1 - чтобы взять, 2 - чтобы пройти мимо: ")
    while decision not in ("1", "2"):
        print("Некорректный ввод")
        decision = input("Введи 1 - чтобы взять, 2 - чтобы пройти мимо: ")
    if decision == "1":
        attack = sword
        print(f"Ты взял себе этот меч. Теперь твоя сила твоей атаки: {attack}")
    elif decision == "2":
        pass


def fight_with_monster() -> None:
    """Функция, генерирующая чудовища. Обрабатывает логику боя."""
    global hp
    global attack
    global monster_counter
    monster_hp = random.randint(5, 10)
    monster_attack = random.randint(3, 10)
    print(f"БОЙ! Ты встретил чудовище c {monster_hp} жизнями и с силой удара {monster_attack}.")
    decision = input("Введи 1 - чтобы принять бой, 2 - чтобы убежать и набраться сил: ")
    while decision not in ("1", "2"):
        print("Некорректный ввод")
        decision = input("Введи 1 - чтобы принять бой, 2 - чтобы убежать и набраться сил: ")
    if decision == "1":
        while hp > 0 or monster_hp > 0:
            hp = hp - monster_attack
            monster_hp = monster_hp - attack
            if hp <= 0:
                continue
            if monster_hp <= 0:
                if monster_counter == 9:
                    monster_counter = monster_counter + 1
                    break
                monster_counter = monster_counter + 1
                print("Ты победил!")
                print(f"Тебе осталось уничтожить еще {10 - monster_counter}...")
                print(f"Твое количество жизней - {hp},твоя атака - {attack}.")
            break
    elif decision == "2":
        pass


def game() -> None:
    """Функция, генерирующая случайность событий. Запускает и завершает игру."""
    global hp
    global monster_counter
    start_game()
    while hp > 0 and monster_counter != 10:
        i = random.randint(1, 11)
        if i in range(1, 6):
            fight_with_monster()
        elif i in range(6, 8):
            get_apple()
        elif i in range(8, 11):
            get_sword()
    if hp <= 0:
        print("ПОРАЖЕНИЕ! Игра окончена!")
        sys.exit()
    if monster_counter == 10:
        print("ПОБЕДА! Ты победил всех чудовищ")
        sys.exit()


game()
