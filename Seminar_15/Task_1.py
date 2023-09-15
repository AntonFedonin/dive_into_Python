# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.

import logging


class NegativeWidthError(ValueError):
    def __init__(self, value):
        self.value = value
        self.message = f"Invalid width: {value}. Width cannot be negative."


class NegativeHeightError(ValueError):
    def __init__(self, value):
        self.value = value
        self.message = f"Invalid height: {value}. Height cannot be negative."


class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeWidthError(value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeHeightError(value)
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


if __name__ == '__main__':
    logging.basicConfig(filename='logFile', filemode='w', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    rectangle = Rectangle(4, 5)
    logger.info(f'"Width:", {rectangle.width}')
    logger.info(f'"Height:", {rectangle.height}')
    logger.info(f'"Area:", {rectangle.area}')
    logger.info(f'"Perimeter:", {rectangle.perimeter}')

    rectangle.width = 6
    rectangle.height = 8

    logger.info(f'"Updated Width:", {rectangle.width}')
    logger.info(f'"Updated Height:", {rectangle.height}')
    logger.info(f'"Updated Area:", {rectangle.area}')
    logger.info(f'"Updated Perimeter:", {rectangle.perimeter}')

    try:
        rectangle.width = -2
    except NegativeWidthError as e:
        logger.error(e.message)

    try:
        rectangle.height = -3
    except NegativeHeightError as e:
        logger.error(e.message)
