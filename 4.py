class Cars:
    """
        Создание и подготовка к работе класса "Автомобили"

        :param name: Название автомобиля
        :param manufacturer: Производитель автомобиля

        Примеры:
        >>> car = Cars("SUV", "Toyota") # инициализация экземпляра класса
        """
    def __init__(self, name: str, manufacturer: str):
        self._name = name
        self._manufacturer = manufacturer

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    def __str__(self):
        return f"Автомобиль {self.name}. Производитель {self.manufacturer}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r})"

class PassengerCar(Cars):
    """
        Создание и подготовка к работе дочернего класса "Легковой автомобиль"
        Параметры
        :param name: Название автомобиля
        :param manufacturer: Производитель автомобиля
        :param body_type: Тип кузова
        Примеры:
         >>> car = PassengerCar("Sedan", "Ford", "Седан") # инициализация экземпляра класса
    """
    def __init__(self, name: str, manufacturer: str, body_type: str):
        super().__init__(name, manufacturer)
        if not isinstance(body_type, str):
            raise TypeError("'body_type' должен быть типа string")
        self.__body_type = body_type

    @property
    def body_type(self):
        return self.__body_type

    @body_type.setter
    def body_type(self, new_body_type: str):
        if not isinstance(new_body_type, str):
            raise TypeError("'new_body_type' должен быть типа string")
        self.__body_type = new_body_type

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.manufacturer!r}, {self.body_type!r})'

    def __str__(self):
        return f"Автомобиль {self.name}. Производитель {self.manufacturer}, Тип кузова {self.body_type}"

class Truck(Cars):
    """
        Создание и подготовка к работе дочернего класса "Грузовой автомобиль"
        Параметры
        :param name: Название автомобиля        :param manufacturer: Производитель автомобиля
        :param max_load: Максимальная грузоподъемность
        Примеры:
        >>> car = Truck("Dump Truck", "Volvo", "10 tons") # инициализация экземпляра класса
    """
    def __init__(self, name: str, manufacturer: str, max_load: str):
        super().__init__(name, manufacturer)
        if not isinstance(max_load, str):
            raise TypeError("'max_load' должен быть типа string")
        self.__max_load = max_load

    @property
    def max_load(self):
        return self.__max_load

    @max_load.setter
    def max_load(self, new_max_load: str):
        if not isinstance(new_max_load, str):
            raise TypeError("'max_load' должен быть типа string")
        self.__max_load = new_max_load

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.manufacturer!r}, {self.max_load!r})'

    def __str__(self):
        return f"Автомобиль {self.name}. Производитель {self.manufacturer}, Максимальная грузоподъемность {self.max_load}"
