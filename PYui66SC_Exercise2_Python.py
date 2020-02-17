# -*- coding: utf-8 -*-
class Facto :
    def __init__ (self,number=0):
        self.number = int(number)
        self.fac = 1
    def FactorX(self):
        """ This function take a number and return the factorial"""
        for i in range(self.number):
            self.fac = self.fac*(self.number - i)
        return self.fac