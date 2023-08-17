import unittest


class Test(unittest.TestCase):

    # suprascriem metoda setUp din clasa TestCase care va rula INAINTE fiecare test
    def setUp(self):
        print("Se executa metoda setUp()...")

    # suprascriem metoda tearDown din clasa TestCase care va rula DUPA fiecare test
    def tearDown(self):
        print("Se executa metoda tearDown()...")
        print("\n")

    def test_A(self):
        print("Se executa testul A")
        expected = 8
        actual = 4 + 3

        assert expected == actual

    def test_B(self):
        print("Se executa testul B")

    def test_C(self):
        print("Se executa testul C")

    @unittest.skip
    def test_D(self):
        print("Se executa testul D")
