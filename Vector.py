import math

from numpy import double


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def betrag_A(self):
        var = self.x ** 2 + self.y ** 2 + self.z ** 2
        tmp: double = math.sqrt(var)
        return double(tmp)

    def mutli_Vector_Number(self, number):
        self.x = self.x * number
        self.y = self.y * number
        self.z = self.z * number

    def scalarProduct(self, vector):
        #       print(f"vector ? ? {vector.x, vector.y, vector.z}")
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def cross_Vectorproduct(self, other):
        var0 = self.y * other.z
        var1 = self.z * other.y
        var2 = self.z * other.x
        var3 = self.x * other.z
        var4 = self.x * other.y
        var5 = self.y * other.x

        var01 = var0 - var1
        var23 = var2 - var3
        var45 = var4 - var5

        vector_New = Vector(var01, var23, var45)

        return vector_New

    def addition_Vector(self, other):
        new_X = self.x + other.x
        new_Y = self.y + other.y
        new_Z = self.z + other.z

        vector_New = Vector(new_X, new_Y, new_Z)
        return vector_New

    def subtract_Vector(self, other):
        new_X = self.x - other.x
        new_Y = self.y - other.y
        new_Z = self.z - other.z

        vector_New = Vector(new_X, new_Y, new_Z)
        return vector_New

    #  Funktion zum Normalisieren eines Vectors (Länge Vektor = 1)
    def normalize_Vector(self):
        norm: double = double(1.0) / self.betrag_A()

        new_X: double = self.x * norm
        new_Y: double = self.y * norm
        new_Z: double = self.z * norm

        return Vector(new_X, new_Y, new_Z)

    def divide_Vector_number(self, number):
        self.x = self.x/number
        self.y = self.y/number
        self.z = self.z/number
        print(f"ERGEBNIS{self.x, self.y, self.z}")
