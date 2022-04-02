from ast import walk
from turtle import distance 


class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        self.distance_km = self.action * self.LEN_STEP / self.M_IN_KM 
        return self.distance_km

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        self.mean_speed = self.distance_km / self.duration
        return self.mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self)


class Running(Training):
    """Тренировка: бег."""
    
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20 

    def _init_(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super()._init_(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.spent_calories = (self.coeff_calorie_1 * self.mean_speed - self.coeff_calorie_2) * self.weight / self.M_IN_KM * (self.duration * self.MIN_IN_HOUR)
        return self.spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029

    def _init_(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int
                 ) -> None:
        super()._init_(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.spent_calories = (self.coeff_calorie_1 * self.weight + (self.mean_speed**2 // self.height) * self.coeff_calorie_2 * self.weight) * (self.duration * self.MIN_IN_HOUR)
        return self.spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38    #переназначаем для дистанции гребка
    coeff_calorie_1 = 1.1
    coeff_calorie_2 = 2

    def _init_(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: float,
                 count_pool: int
                 ) -> None:
        super()._init_(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость плавания."""
        self.mean_speed = self.lenght_pool * self.count_pool / self.M_IN_KM / self.duration
        return self.mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.spent_calories = (self.mean_speed + self.coeff_calorie_1) * self.coeff_calorie_2 * self.weight
        return self.spent_calories



def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        return Swimming(data)
    elif workout_type == 'RUN':
        return Running(data)
    elif workout_type == 'WLK':
        return SportsWalking(data)


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

