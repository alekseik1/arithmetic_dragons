# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    _color = 'NonColored'
    __answer = 'NonAns'
    __quest = 'NonQuest'

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Povar(Dragon):
    def __init__(self):
        self._health = 1
        self._attack = 1000
        self._color = 'Повар'

    def question(self):
        self.__quest = "Какова моя профессия?"
        self.set_answer('повар')
        return self.__quest


class Troll_gen(Dragon):
    def __init__(self):
        self._heath = 100
        self._attack = 10
        self._color = 'Тролль-угадайка'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Какое число я загадал от 1 до 5?'
        self.set_answer(x)
        return self.__quest


class Troll_easy_of_chislo(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'Тролль-простое-число'

    def isPrime(self, n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2

        return d * d > n

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Простое ли число ' + str(x) + '?'
        if self.isPrime(x):
            self.set_answer('да')
        else:
            self.set_answer('нет')
        return self.__quest


class Troll_razlogi_chislo_ples(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'Тролль-разлагатель-чисел'

    def get_answer(self, n):
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        res = ''
        for i in Ans:
            res += i
            res += ','
        res = res[:-2]
        return res

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Разложи мне число, голубчик, и напиши множители через запятую в порядке возрастания: ' + x
        self.set_answer(self.get_answer(x))
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon, Povar, Troll_gen, Troll_easy_of_chislo, Troll_razlogi_chislo_ples]
