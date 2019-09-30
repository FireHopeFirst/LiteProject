import random

# Клас для нашего робота
class II:

    def __init__(self, hp):
        self.hp_II = hp
        count = 0
    # Метод для рандомного небольшого диапазона урона
    def min_range(self):
        count = random.randint(18, 25)
        self.hp_II -= count
        print("Игрок нанес", count,"урона")

    # Метод для рандомного небольшого диапазона урона
    def max_range(self):
        count = random.randint(10, 35)
        self.hp_II -= count
        print("Игрок нанес", count,"урона")

    # Метод для рандомного небольшого диапазона
    def min_range_heal(self):
        count = random.randint(18, 25)
        self.hp_II += count
        print("Робот отхилил себя на", count)
        if self.hp_II > 100:
            self.hp_II = 100

# Клас для нашего Игрока
class Player:

    def __init__(self, hp):
        self.hp_Player = hp
        count = 0

    # Метод для рандомного небольшого диапазона урона
    def min_range(self):
        count = random.randint(18, 25)
        self.hp_Player -= count
        print("Робот нанес", count,"урона")

    # Метод для рандомного небольшого диапазона урона
    def max_range(self):
        count = random.randint(10, 35)
        self.hp_Player -= count
        print("Робот нанес", count,"урона")

    # Метод для рандомного небольшого диапазона
    def min_range_heal(self):
        count = random.randint(18, 25)
        self.hp_Player += count
        print("Игрок отхилил себя на", count)
        if self.hp_Player > 100:
            self.hp_Player = 100


def method_Robot():
    # Если число равняеться один то тогда выполняем метод min_range() для вычитания здоровья
    if id_move == 1:
        I.min_range()
        print(Robot.hp_II, "Здоровье у Робот")
        print(I.hp_Player, "Здоровье у Игрок")
        print("----------------------")
    # Если число равняеться два то тогда выполняем метод max_range() для вычитания здоровья
    elif id_move == 2:
        I.max_range()
        print(Robot.hp_II, "Здоровье у Робот")
        print(I.hp_Player, "Здоровье у Игрок")
        print("----------------------")
    # Если число равняеться три то тогда выполняем метод min_range_heal для добавления здоровья
    else:
        Robot.min_range_heal()
        print(Robot.hp_II, "Здоровье у Робот")
        print(I.hp_Player, "Здоровье у Игрок")
        print("----------------------")


def method_Player():
    # Если число равняеться один то тогда выполняем метод min_range() для вычитания здоровья
    if id_move == 1:
        Robot.min_range()
        print(Robot.hp_II, "Здоровье у Робот")
        print(I.hp_Player, "Здоровье у Игрок")
        print("----------------------")
    # Если число равняеться два то тогда выполняем метод max_range() для вычитания здоровья
    elif id_move == 2:
        Robot.max_range()
        print(Robot.hp_II, "Здоровье у Робот")
        print(I.hp_Player, "Здоровье у Игрок")
        print("----------------------")
    # Если число равняеться три то тогда выполняем метод min_range_heal для добавления здоровья
    else:
        I.min_range_heal()
        print(Robot.hp_II, "Здоровье у Робот")
        print(I.hp_Player, "Здоровье у Игрок")
        print("----------------------")


if __name__ == '__main__':
    Flag = True
    # Инициализация экземпляра класса Player
    I = Player(100)
    # Инициализация экземпляра класса II
    Robot = II(100)
    # Переменная для рандомных чисел
    id_move = 0
    # Бесконечный цикл While пока флаг не станет False
    while Flag:
        # Получаем случайное число которое характеризует чей ход
        id_move = random.randint(1, 2)
        # Если число равняется одному то ходит игрок ,а если двум то тогда компютер
        if id_move == 1:
            # Получаем случайное число которое характеризует какой ход будет у Игрока
            id_move = random.randint(1, 3)
            # Переход на метод Игрок
            method_Player()
        else:
            # Если здоровье РоБот больше 35 тогда выполняем метод method_Robot()
            if Robot.hp_II > 35:
                # Получаем случайное число которое характеризует какой ход будет у Робота
                id_move = random.randint(1, 3)
                method_Robot()
            # Если здоровье меньше 35 тогда мы пошаем шанс на метод min_range_heal()
            # Теперь шанс выпадение метода min_range_heal() равняеться 50% а других методов по 25%
            else:
                id_move = random.randint(1, 2)
                # Если нам выпадает один то мы выбираем какую мы атаку будем делать первую или вторую
                if id_move == 1:
                    id_move = random.randint(1, 2)
                    method_Robot()
                # Если нам выпадает два то мы выбираем третий метод
                if id_move == 2:
                    id_move = 3
                    method_Robot()

        # Если здоровье Player меньше 35 то Робот победил и цикл завершился
        if I.hp_Player <= 0:
            I.hp_Player = 0
            print("Robot победил")
            print(Robot.hp_II, "Здоровье у Робот")
            print(I.hp_Player, "Здоровье у Игрок")
            Flag = False
        # Если здоровье Robot меньше 35 то Игрок победил и цикл завершился
        if Robot.hp_II <= 0:
            Robot.hp_II = 0
            print("Player победил")
            print(Robot.hp_II, "Здоровье у Робот")
            print(I.hp_Player, "Здоровье у Игрок")
            Flag = False