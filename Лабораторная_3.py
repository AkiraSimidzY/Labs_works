class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("'pages' должен быть типа integer")
        self.pages = pages
    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(pages, int):
            raise TypeError("'pages' должен быть типа integer")
        if new_pages < 0:
            raise ValueError("'pages' не может быть отрицательным числом")
        self.__pages = new_pages
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.pages!r} )'

class AudioBook(Book):
    def __init__(self, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, int):
            raise TypeError("'duration' должен быть типа integer")
        self.duration = duration
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, new_duration: float):
         if not isinstance(duration, int):
            raise TypeError("'duration' должен быть типа integer")
        if new_duration < 0:
            raise ValueError("'duration' не может быть отрицательным числом")
        self.__duration = new_duration
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.duration!r} )'
