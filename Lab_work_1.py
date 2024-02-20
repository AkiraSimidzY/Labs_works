import doctest
class Book:
    def __init__(self, total_pages: int, current_page: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param total_pages: Общее количество страниц в книге
        :param current_page: Текущая страница, на которой открыта книга
        Примеры:
        >>> book = Book(300, 1)  # инициализация экземпляра класса
        """
        if not isinstance(total_pages, int):
            raise TypeError("Общее количество страниц должно быть типа int")
        if total_pages <= 0:
            raise ValueError("Общее количество страниц должно быть положительным числом")
        self.total_pages = total_pages

        if not isinstance(current_page, int):
            raise TypeError("Текущая страница должна быть типа int")
        if current_page <= 0 or current_page > total_pages:
            raise ValueError(
                "Текущая страница должна быть положительным числом и не превышать общее количество страниц")
        self.current_page = current_page

    def is_book_finished(self) -> bool:
        """
        Функция которая проверяет закончена ли книга
        :return: Закончена ли книга
        Примеры:
        >>> book = Book(300, 300)
        >>> book.is_book_finished()
        """
        return self.current_page == self.total_pages

    def turn_page(self, pages_to_turn: int) -> None:
        """
        Перелистывание страниц в книге.
        :param pages_to_turn: Количество страниц для перелистывания
        :raise ValueError: Если количество страниц для перелистывания приводит к некорректной позиции страницы,
        то вызываем ошибку
        Примеры:
        >>> book = Book(300, 1)
        >>> book.turn_page(10)
        """
        if not isinstance(pages_to_turn, int):
            raise TypeError("Количество страниц для перелистывания должно быть типа int")
        if pages_to_turn < 1 or self.current_page + pages_to_turn > self.total_pages:
            raise ValueError("Некорректное количество страниц для перелистывания")
        self.current_page += pages_to_turn


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации