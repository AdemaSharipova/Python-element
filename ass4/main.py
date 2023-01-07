from dataclasses import dataclass


@dataclass
class Driver:
    full_name: str
    experience: int

    def __str__(self) -> str:
        return f'Driver. \nFull name: {self.full_name}, ' \
               f'driving experience: {self.experience}'


@dataclass
class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f'Engine. \nPower: {self.power}, ' \
               f'producer: {self.company}'


@dataclass
class Car:
    car_model: str
    car_class: str
    weight: float
    driver: Driver
    engine: Engine

    def start(self) -> None:
        print('Go')

    def stop(self) -> None:
        print('Stop')

    def turn_right(self) -> None:
        print('Turn right')

    def turn_left(self) -> None:
        print('Turn left')

    def __str__(self):
        return f'Car representation. \nCar model: {self.car_model}, ' \
               f'car class: {self.car_class}, ' \
               f'weight: {self.weight} \n' \
               f'{self.driver} \n' \
               f'{self.engine}'

@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self):
        return f'Lorry. \n' \
               f'Carrying: {self.carrying} \n{super().__str__()}'


@dataclass
class SportCar(Car):
    speed: float

    def __str__(self):
        return f'Sport car. \n' \
               f'Speed: {self.speed} \n{super().__str__()}'


@dataclass
class Person(Driver):
    _age: int

    @property
    def age(self) -> int:
        return self._age

    def set_age(self, age) -> int:
        _age = age
        return self._age

    def __str__(self):
        return f'{super().__str__()}, age: {self.age}'





