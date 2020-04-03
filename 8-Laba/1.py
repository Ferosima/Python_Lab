# 2. Створіть клас з ім'ям train, що містить поля: назва пункту призначення, номер поїзда, час відправлення.
# Ввести дані в масив з п'яти елементів типу train, впорядкувати елементи за номерами поїздів.
# Додати можливість виведення інформації про потяг, номер якого введено користувачем.
# Додати можливість сортування масив по пункту призначення,
# причому поїзда з однаковими пунктами призначення повинні бути впорядковані за часом відправлення.

from datetime import datetime
from typing import List


class Train:
    def __init__(self, destination: str, trainNum: str, dateStart):
        self.destination = destination
        self.trainNum = trainNum
        self.dateStart = dateStart

    def print_info(self):
        print('number:', self.trainNum, '| Destination:', self.destination, "| Data start:", self.dateStart)


def sortByDestination(trains: List[Train]) -> List[Train]:
    return sorted(trains, key=lambda train: train.destination)


def getTrainByNum(num, trains: List[Train]):
    for i in range(len(trains)):
        if trains[i].trainNum == num:
            trains[i].print_info()


trains = []
trains.append(Train('Херсон', '02', datetime(2019, 8, 30, 18)))
trains.append(Train('Николаев', '08', datetime(2019, 8, 30, 17)))
trains.append(Train('Берлин', '04', datetime(2019, 8, 30, 14)))
trains.append(Train('Киев', '03', datetime(2019, 8, 30, 22)))
trains.append(Train('Атлантида', '19', datetime(2019, 8, 30, 18)))
trains.sort(key=lambda train: train.trainNum)
getTrainByNum('02', trains)
