import random
class Character:
    lvl = 1
    def __init__(self, job, gender, affinity):
        self.job = job
        self.gender = gender
        self.affinity = affinity

class Enemy:
    def __init__(self, lvl, affinity):
        self.lvl = lvl
        self.affinity = affinity
        
class Job:
    def __init__(self, gender, weapon):
        self.gender = gender
        self.weapon = weapon
        if gender == 'Male':
            self.life = 1500
            self.strength = 5
            self.intelligence = 3
            self.charisma = 3
        elif gender == 'Female':
            self.life = 1000
            self.strength = 3
            self.intelligence = 5
            self.charisma = 5

class Weapon:
    def __init__(self, type, affinity, damage):
        self.type = type
        self.damage = damage
        self.affinity = affinity




        
