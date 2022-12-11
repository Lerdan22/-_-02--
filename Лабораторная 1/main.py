import doctest


class Rod:
    def __init__(self, first_coordinate: int, second_coordinate: int, section: str):
        """
              Создание и подготовка к работе объекта "Стержень"
              :param first_coordinate: Первая точка стержня
              :param second_coordinate: Вторая точка стержня
              :param section: Форма поперечного сечения
              Примеры:
              >>> rod = Rod(10, 20, "Двутавр")  # инициализация экземпляра класса
              """
        if not isinstance(first_coordinate or second_coordinate, (int, float)):
            raise TypeError("Координаты должны быть числами")
        if first_coordinate or second_coordinate <= 0:
            raise ValueError("Работаем в положительных координатах")
        self.first_coordinate = first_coordinate
        self.second_coordinate = second_coordinate
        self.section = section

    def length(self):
        """
        Метод определяет длину стержня по координатам его концов
        :return: длина полученного стержня

        Примеры:
        >>> rod = Rod(10, 20, "Двутавр")
        >>> rod.length()
        """
        ...

    def orietation(self):
        """
        Метод определяет, в какую сторону ориентирован стержень (в положительную или отрицательную)
        Если second_coordinate > fisrt_coordinate - отрицательная ориентация
        :return: ориентация стержня
        >>> rod = Rod(10, 20, "Двутавр")
        >>> rod.orietation()
        """


class Contour:
    def __init__(self, number_of_members: int, length_of_members: int):
        """
            Создание и подготовка к работе объекта "Контур"
            :param number_of_members: определяет количество стержней в контуре
            :param length_of_members: значение длины стержней в контуре
            Примеры:
            >>> contour = Contour(10, 3)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_members or length_of_members, (int, float)):
            raise TypeError("Количество элементов и их длина - это численные параметры")
        if number_of_members or length_of_members <= 0:
            raise ValueError("Контур не может состоять из отрицательного кол-ва эл-тов или эл-тов с отрицательными длинами")

    def is_closed(self, angle):
        """
        Метод проверяет, может ли контур существовать при заданном угле между эл-тами.
        Сумма углов (в градусах) <= 360
        :param angle: Запрашивает у пользователя значение угла между всеми элементами (угол один, т.к. длины одинаковые)
        :return: Замкнут ли контур
        >>> contour = Contour(10, 3)
        >>> contour.is_closed(15)
        """
        ...

    def square(self):
        """
        Метод считает площадь под контуром
        :return: значение площади контура
        >>> contour = Contour(10, 3)
        >>> contour.square()
        """


class Wall:
    def __init__(self, height: int, wight: float, material: str):
        """
        Создание и подготовка к работе объекта "Стена"
        :param height: Высота стены
        :param wight: Толщина стены
        :param material: Материал стены
        >>>wall = Wall(5, 0.3, "железобетон")
        """
        if not isinstance(height or wight, (int, float)):
            raise TypeError("Высота и толщина стены не могут быть заданы никак кроме как числами")
        if height < 10 * wight:
            raise ValueError("Это уже не стена, а балка или плита")

    def unit_volume(self):
        """
        Метод определяет объем затраченных материалов на 1 единицу длины стены
        >>>wall = Wall(5, 0.3, "железобетон")
        >>>wall.unit_volume()
        :return: Объем на единицу длины
        """
        ...
    def pressure(self, density: float):
        """
        Метод определяет давление от стены на нижележащие конструкции
        :param density: пользователь вводит плотность материала стены
        :return: нагрузку от стены на единицу длины
        >>>wall = Wall(5, 0.3, "железобетон")
        >>>wall.pressure(2100)
        """

if __name__ == "__main__":
    doctest.testmod()
    pass
