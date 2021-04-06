import unittest
from Vector import Vector


class MyTestCase(unittest.TestCase):
    def test_betrag(self):
        test_V: Vector = Vector(3, 2, 6)
        betrag = test_V.betrag_A()
        self.assertEqual(7, betrag)

    def test_multi_Vector_Number(self):
        test_V: Vector = Vector(3, 2, 6)
        test_V_compare: Vector = Vector(6, 4, 12)
        var_Number = 2
        test_V.mutli_Vector_Number(var_Number)

        self.assertEqual(test_V.x, test_V_compare.x)
        self.assertEqual(test_V.y, test_V_compare.y)
        self.assertEqual(test_V.z, test_V_compare.z)

    def test_scalar(self):
        test_V: Vector = Vector(3, 2, 6)
        test_V_two: Vector = Vector(-1, -1, -1)
        var_compare = -11
        var_sum = test_V.scalarProduct(test_V_two)

        self.assertEqual(var_compare, var_sum)

    def test_addition(self):
        test_V: Vector = Vector(3, 2, 6)
        test_V_two: Vector = Vector(1, 1, 1)
        test_V_final = test_V.addition_Vector(test_V_two)
        test_V_compare: Vector = Vector(4, 3, 7)

        self.assertEqual(test_V_final.x, test_V_compare.x)
        self.assertEqual(test_V_final.y, test_V_compare.y)
        self.assertEqual(test_V_final.z, test_V_compare.z)

    def test_subtract(self):
        test_V: Vector = Vector(3, 2, 6)
        test_V_two: Vector = Vector(1, 1, 1)
        test_V_final = test_V.subtract_Vector(test_V_two)
        test_V_compare: Vector = Vector(2, 1, 5)

        self.assertEqual(test_V_final.x, test_V_compare.x)
        self.assertEqual(test_V_final.y, test_V_compare.y)
        self.assertEqual(test_V_final.z, test_V_compare.z)

    def test_normalize_Vector(self):
        test_V: Vector = Vector(3, 2, 6)
        var_Vector: Vector = test_V.normalize_Vector
        var_tmp = var_Vector.betrag_A()
        var_new_tmp = round(var_tmp)
        self.assertEqual(1, var_new_tmp)

    def test_divide(self):
        number = 2
        test_V: Vector = Vector(3, 2, 6)
        test_V.divide_Vector_number(number)

        self.assertEqual(1.5, test_V.x)
        self.assertEqual(1, test_V.y)
        self.assertEqual(3, test_V.z)


if __name__ == '__main__':
    unittest.main()
