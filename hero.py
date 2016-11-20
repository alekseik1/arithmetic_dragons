# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):

    _experience = 0
    _health = 100
    _attack = 50
    _name = 'Anonymus'

    def __init__(self, name):
        self._name = name

    def attack(self, target):
        target._health -= self._attack