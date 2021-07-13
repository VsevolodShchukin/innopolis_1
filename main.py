import random


def game():

    # Игровые показатели
    monster_counter = 10
    hp = random.randint(10, 20)
    attack = random.randint(10, 15)
    print(
        f"Ты рыцарь, который должен защитить королевство! Твое количество жизней - {hp}. Твоя сила удара - {attack}"
    )

    # Функции оповещения игрока о событии
    class Alarms:
        # Сообщает о встреченном чудовище. Отражает его характеристики.
        def alarm_mosnter(self, monster_hp, monster_attack):
            print(
                f"БОЙ! Ты встретил чудовище c {monster_hp} жизнями и с силой удара {monster_attack}. Будешь с ним сражаться?"
            )

        # Сообщает о найденном мече. Отражает его характеристики.
        def alarm_swrd(self, power_swrd):
            print(
                f"Ты нашел МЕЧ! Его сила атаки - {power_swrd}. Хочешь его взять на замену старому?"
            )

        # Сообщает о найденном яблоке. Показывает, сколько оно прибавило жизней и чему равняется значение жизней теперь.
        def alarm_apple(self, apple):
            print(
                f"Ты нашел яблоко и сразу же съел его! Оно увеличило количество жизней на {apple}. Теперь твое количество жизней: {hp + apple}"
            )

    # Генераторы случайных сущностей и функции с логикой игры
    class Game_logic(Alarms):

        # Генератор случайных монстров с вызовом функций оповещения и выбора
        def generator_monster(self):
            global monster_hp
            global monster_attack
            monster_hp = random.randint(5, 10)
            monster_attack = random.randint(3, 10)
            self.alarm_mosnter(monster_hp, monster_attack)
            self.choose_your_destiny()

        # Генератор случайных мечей с вызовом функции оповещения и функции выбора внутри
        def generator_swrd(self):
            power_swrd = random.randint(10, 25)
            self.alarm_swrd(power_swrd)

            def decision_swrd():
                decision = input("Введи 1 - чтобы взять, 2 - чтобы пройти мимо: ")
                global attack
                if decision == "1":
                    attack = power_swrd
                    print(
                        f"Ты взял себе этот меч. Теперь твоя сила твоей атаки: {attack}"
                    )
                elif decision == "2":
                    pass
                else:
                    print("Некорректный ввод!")
                    decision_swrd()

            decision_swrd()

        # Генератор случайных яблок с вызовом функции оповещения. Изменяет количество жизней
        def generator_apple(self):
            apple = random.randint(1, 3)
            self.alarm_apple(apple)
            global hp
            hp = hp + apple

        # Функция, которая обрабатывает выбор игрока при событии "Бой"
        def choose_your_destiny(self):
            decision = input(
                "Введи 1 - чтобы принять бой, 2 - чтобы убежать и набраться сил: "
            )
            if decision == "1":
                self.battle()
            elif decision == "2":
                print("Ты убежал от чудовища!")
                pass
            else:
                print("Некорректный ввод. Введи 1 или 2")
                self.choose_your_destiny()

        # Функция с логикой боя
        def battle(self):
            global monster_hp
            global monster_attack
            global attack
            global hp
            global monster_counter
            if hp <= 0:
                print("ПОРАЖЕНИЕ! Игра окончена!")
            elif monster_counter == 1 and monster_hp <= 0:
                monster_counter = 0
                print("ПОБЕДА! Ты победил всех чудовищ")
            elif monster_hp <= 0:
                monster_counter = monster_counter - 1
                print(
                    f"Ты победил чудовище! Тебе осталось уничтожить еще {monster_counter}..."
                )
                print(f"Твое количество жизней - {hp},твоя атака - {attack}.")
            else:
                monster_hp = monster_hp - attack
                hp = hp - monster_attack
                self.battle()

    # Генератор случайных событий и инспектор условий
    class Creator(Game_logic):

        # Инспектор условий игры
        def inspector_world(self):
            global hp
            global monster_counter
            while hp > 0 and monster_counter > 0:
                self.random_generator()

        # Генератор случайных событий
        def random_generator(self):
            i = random.randint(1, 3)
            if i == 1:
                self.generator_monster()
            elif i == 2:
                self.generator_apple()
            else:
                self.generator_swrd()
                self.inspector_world()

    a = Creator()
    a.inspector_world()


game()
