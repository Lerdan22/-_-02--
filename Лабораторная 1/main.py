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
        if first_coordinate and second_coordinate <= 0:
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
                     >>> rod = Rod(10, 20, "Двутавр")  # инициализация экземпляра класса
                     """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
