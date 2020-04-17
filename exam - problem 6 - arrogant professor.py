# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:37:26 2020

@author: simon
"""

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')