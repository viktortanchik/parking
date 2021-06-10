#Система для контроля парковки автомобилей

class Parking:
    parking = [[], [], []]# двумерная матрица парковки
    def matrix(self,parking):# Функция для вывода в виде матрици
        self.parking =parking
        for i in parking:# проход по спискам
            for j in i:# проход по елементам
                print(j, end=' ') # после вывода елемента мы не переходим на новую строчку
            print()# Переход на новую строчку.

    def park(self, parking, motorcycle, car, bus):# Функция для настройки парковочных мест, принемает количество
                                                  # необходимых парковочных мест для конкретного типа транспорта
        self.parking =parking
        for i in range(motorcycle):# Настройка парковочного места  только для мотоциклов
            parking[0].append(0)
        for i in range(car):# Настройка  компактных мест -> может вместить мотоцикл или автомобиль
            parking[1].append(0)
        for i in range(bus):# Настройка большого места -> может вместить мотоцикл или автомобиль
                            #Автобусу для парковки требуется наличие 5 больших парковочных мест.
            parking[2].append(0)
        print(parking)

    def motorcycleAdd(self,parking,transport):# Функция для добавления на парковку мотоциклов, принемает 2 параметра
                                              # масив и количество новых мотоциклов
        for i in range(transport):# добавления необходимого количества транспорта
            self.parking = parking
            flag = True # флаг для работы с условием
            for i in range(len(parking)):
                for j in range(len(parking[i])):
                    if parking[i][j] == 0 and flag == True:# проверка на свободное место
                        flag = False # меняем состояния флага
                        print("Мы можем добавить мотоцикл в ячейку",i, j)
                        parking[i][j] = 'M'# добавляем транспорт на стоянку
            if flag == True: # Если флаг не изменился значит свободных мест на парковке для этого вида транспорта нет
                print("Свободных мест нет")

    def motorcycleDel(self,parking,transport):# Функция для удаления ( освобождения ) парковочного места от транспорта
                                              # принемает 2 параметра масив и количество  транспорта
        for i in range(transport):# освобождения необходимого количества парковочных мест
            flag = True# флаг для работы с условием
            for i in reversed(range(len(parking))):
                for j in reversed(range(len(parking[i]))):
                    if parking[i][j] == 'M' and flag == True:# проверка на занятое место
                        flag = False # меняем состояния флага
                        print("Я чейка освободилась ",i, j)
                        parking[i][j] = 0 # освобождаем парковочное место
            if flag == True: # Если флаг не изменился значит занятых мест на парковке для этого вида транспорта нет
                print("Мотоциклов на стоянке нет")

    def carAdd(self,parking,transport):# Функция для добавления на парковку автомобилей, принемает 2 параметра
                                              # масив и количество новых автомобилей
        for i in range(transport):# добавления необходимого количества транспорта
            flag = True# флаг для работы с условием
            for i in range(1, len(parking)):
                for j in range(len(parking[i])):
                    if parking[i][j] == 0 and flag == True:# проверка на свободное место
                        flag = False# меняем состояния флага
                        print("Мы можем добавить машину в ячейку",i, j)
                        parking[i][j] = 'C'# добавляем транспорт на стоянку
            if flag == True:# Если флаг не изменился значит свободных мест на парковке для этого вида транспорта нет
                print("Свободных мест нет")

    def carDel(self,parking,transport):# Функция для удаления ( освобождения ) парковочного места от транспорта
                                              # принемает 2 параметра масив и количество  транспорта
        for i in range(transport):# освобождения необходимого количества парковочных мест
            flag = True# флаг для работы с условием
            for i in reversed(range(len(parking))):
                for j in reversed(range(len(parking[i]))):
                    if parking[i][j] == 'C' and flag == True:# проверка на занятое место
                        flag = False# меняем состояния флага
                        print("Я чейка освободилась",i, j)
                        parking[i][j] = 0# освобождаем парковочное место
            if flag == True:# Если флаг не изменился значит занятых мест на парковке для этого вида транспорта нет
                print("Машин на стоянке нет")

    def busAdd(self,parking,transport):# Функция для добавления на парковку автомобилей, принемает 2 параметра
                                            # масив и количество новых автомобилей
        for i in range(transport):          # добавления необходимого количества транспорта
            countBus = parking[2].count(0)  # Возвращает количество элементов со значением 0
            flag = True# флаг для работы с условием
            m = []# Будет хранить номера парковочных мест для абвтобуса
            a = 0 # Необходима для работы условия
            if (countBus - 5) >= 0:# проверяем есть ли необходимое количество свободных мест
                for j in range(len(parking[2])):
                    if parking[2][j] == 0 and flag == True:# Поиск свободных мест
                        a += 1 # если свободное место есть увеличиваем переменую на 1
                        m.append(j) # записеваем номер места парковки для дальнейшего что бы правельно установить
                                    # автобус
                        if a == 5:#
                            flag = False# меняем состояния флага
                            print("Автобус добавлен в", m, 'ячейки')
                            for i in range(len(m)):# Размещяем автобус на парковке
                                parking[2][m[i]] = "B"
                            a = 0
        if flag == True:# Если флаг не изменился значит свободных мест на парковке для этого вида транспорта нет
            print("Свободных мест нет")
            a = 0
            m.clear()

    def busDel(self,parking,transport):# Функция для удаления ( освобождения ) парковочного места от транспорта
                                              # принемает 2 параметра масив и количество  транспорта
        for i in range(transport):# освобождения необходимого количества парковочных мест
            flag = True# флаг для работы с условием
            m = []# Будет хранить номера парковочных мест для абвтобуса
            a = 0
            for i in reversed(range(len(parking))):
                for j in reversed(range(len(parking[i]))):
                    for j in range(len(parking[2])):
                        if parking[2][j] == "B" and flag == True:# Поиск Занятых мест автобусом
                            a += 1
                            m.append(j)
                            if a == 5:
                                flag = False
                                print("Я чейки освободились", m)
                                for i in range(len(m)):
                                    parking[2][m[i]] = 0
                                a = 0
            if flag == True:
                print("Автобусов на стоянке нет")

    def status(self,parking):# Функция позволяет отобразить количество транспортных средств каждого вида, которые находятся на парковке
        self.parking =parking
        motorcycle = parking[0].count('M')+parking[1].count('M')+parking[2].count('M')# находим количество мотоциклов
        car = parking[1].count('C')+parking[2].count('C')# находим количество машин
        bus = parking[2].count('B')# находим количество автобусов
        print("На стоянке находится ", motorcycle, "мотоциклов")
        print("На стоянке находится ", car, "машин")
        print("На стоянке находится ", int(bus/5), "автобус(ов)")

    def testMotorcycleAdd(self, parking, transport):# функция позволяет проверить доступность парковки для заданного
                                                    # транспортного средства
        for x in range(transport):# добавления необходимого количества транспорта
            self.parking = parking
            flag = True# флаг для работы с условием
            for i in range(len(parking)):
                for j in range(len(parking[i])):
                    if parking[i][j] == 0 and flag == True:# проверка на свободное место
                        flag = False
                        print("Мы можем добавить мотоцикол в ячейку",i, j)
            if flag == True:
                print("Свободных мест нет")
        self.matrix(parking)

    def testCarAdd(self, parking, transport):# функция позволяет проверить доступность парковки для заданного
        # транспортного средства
        for i in range(transport):
            flag = True
            for i in range(1, len(parking)):
                print(i)
                for j in range(len(parking[i])):
                    if parking[i][j] == 0 and flag == True:
                        flag = False
                        print("Мы можем добавить машину в ячейку",i, j)
            if flag == True:
                print("Свободных мест нет")
        self.matrix(parking)

    def testBusAdd(self,parking,transport):# функция позволяет проверить доступность парковки для заданного
                                          # транспортного средства
        for i in range(transport):
            countBus = parking[2].count(0)  # Возвращает количество элементов со значением 0
            flag = True
            m = []
            a = 0
            if (countBus - 5) >= 0:
                for j in range(len(parking[2])):
                    if parking[2][j] == 0 and flag == True:
                        a += 1
                        m.append(j)
                        if a == 5:
                            flag = False
                            print("Мы можем добавить автобус в ячейки",m)
                            a = 0
            if flag == True:
                print("Свободных мест нет")
                a = 0
                m.clear()

        self.matrix(parking)

    def place(self,parking,m,n):# функция позволяет проверить доступность конкретного парковочного места принемает
                                # несколько параметров
        self.parking =parking
        place = parking[m][n]
        if place !=0:
            print("Место занято")


test = Parking()
test.park(test.parking,5,10,5)
test.motorcycleAdd(test.parking,4)
test.carAdd(test.parking,9)
test.busAdd(test.parking,2)
test.place(test.parking,1,1)
test.status(test.parking)
