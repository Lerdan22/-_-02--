import random

import self as self


class Car:
    """
    Документация на класс.
    Класс описывает Автомобиль.
    """

    def __init__(self, model: str, lvl: int, capacity: int, ExperiencePoints: int):
        """
        Инициализация экземпляра класса.
        :param model: Название модели
        :param lvl: Уровень автомобиля
        :param capacity: Мощность модели
        :param ExperiencePoints: Опыт игрока
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model

        if not isinstance(lvl, int):
            raise TypeError("Уровень должен быть типа int")
        if lvl <= 0:
            raise ValueError("Уровень должен быть положительным числом")
        self.lvl = lvl

        if not isinstance(capacity, int):
            raise TypeError("Мощность должна быть типа int")
        if capacity <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.capacity = capacity

        if not isinstance(ExperiencePoints, int):
            raise TypeError("Опыт должен быть типа int")
        if ExperiencePoints < 0:
            raise ValueError("Опыт не может быть отрицательным числом")
        self.ExperiencePoints = ExperiencePoints


    def __str__(self):
        """
        Метод возвращает строку для чтения.
        """
        return f"Воин {self.model}; Уровень {self.lvl}; Сила {self.capacity}; Опыт {self.ExperiencePoints}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
        """
        return f"{self.__class__.__name__}(Имя={self.model!r}, Уровень={self.lvl!r}, Сила={self.capacity!r}, Опыт={self.ExperiencePoints!r})"

    def lvl_up(self):
        """
        Метод определяет уровень героя по имеющемуся опыту.
        """
        Experience_of_lvl = [0, 300, 900, 2700, 6500, 14400, 23000, 34000, 48000, 64000, 85000, 100000]
        for exp in Experience_of_lvl:
            if self.ExperiencePoints < exp:
                self.lvl = Experience_of_lvl.index(exp)
                print("Уровень автомобиля", self.lvl)
                break

        return self.lvl

    def exp_up(self, Experience: int):
        """
        Метод увеличивает количество имеющегося опыта.
        """
        self.Experience = Experience
        self.ExperiencePoints += self.Experience
        print("Получено опыта", self.ExperiencePoints)
        return self.ExperiencePoints

    def nitro(self):
        """
        Метод позволяет применить ускорение NO2. Ускорение считается успешным, если число на кубике больше 10.
        """
        hit = random.randint(1, 20)
        print("Бросаем кубик... Выпало:", hit)
        if hit > 10:
            print("Ускорение")
        else:
            print("Не хватает ускорителя")

class Racing_car(Car):
    """
    Документация на дочерний класс.
    Класс описывает подкласс Автомобиля -- Гоночный.
    """
    def __init__(self, model: str, lvl: int, capacity: int, ExperiencePoints: int, TurboEngine = None):
        """
        Инициализация экземпляра подкласса.
        :param model: Модель автомобиля
        :param lvl: Уровень автомобиля
        :param strength: Мощность автомобиля
        :param ExperiencePoints: Опыт игрока
        :param TurboEngine: Дополнительная надбавка к мощности автомобиля. Приравнивается к уровню автомобиля.
        """
        super().__init__(model, lvl, capacity, ExperiencePoints)
        if TurboEngine is None:
            TurboEngine = self.lvl
        self.TurboEngine = TurboEngine

        if not isinstance(TurboEngine, int):
            raise TypeError("Дополнительная мощность должна быть больше 0")
        if Inspiration <= 0:
            raise ValueError("Дополнительная мощность должна быть положительным числом")

    def __str__(self):
        """
        Метод возвращает строку для чтения.
        Перегрузку метода реализовали из-за необходимости указания подкласса автомобиля.
        """
        s_str = super().__str__()
        return f"{s_str}; Подкласс: {self.__class__.__name__}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
        Перегрузку метода реализовали из-за необходимости указания подкласса автомобиля.
        """
        s_repr = super().__repr__()
        return f"{s_repr}; Подкласс={self.__class__.__name__!r}"

    def nitro(self):
        """
        Метод позволяет применить ускорение. Ускорение считается успешным, если число на кубике больше 10.
        Перегрузка метода реализовали из-за того, что подкласс Гоночная имеет возможность два раза применить нитро.
        """
        s_attack = super().nitro()
        hit_2 = random.randint(1, 20)
        print("Ускоряемся ещё раз?")
        answer = input()
        if answer == "Да":
            print("Бросаем кубик... Выпало:", hit_2)
            if hit_2 > 10:
                print("Ускорение")
            else:
                print("Не хватает ускорения")
        elif answer == "Нет":
            print("Дополнительное ускорение не применено")
        else:
            print("Не могу тебя понять")

if __name__ == "__main__":
    Car = Car("Форд", 1, 16, 0)
    #Car.lvl_up()
    #Car.exp_up(1000)
    Racing_car = Racing_car("Форд Мустанг", 3, 16, 899)
    #Racing_car.nitro()
    pass