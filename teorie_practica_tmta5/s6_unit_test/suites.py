import unittest
import HtmlTestRunner
from teorie_practica_tmta5.s6_unit_test.s6_unittest_selenium import Login, DemoMultipleClassesTestSuite
# from s6_unittest_selenium import (
#     Test,
#     Test2,
# )
# cream clasa suitei de teste
class TestSuite(unittest.TestCase):

    # cream metoda pentru executie
    def test_suite(self):
        #instantiem obiect din suita
        test_de_rulat = unittest.TestSuite()
        #adaugam clasele de teste care vrem sa fie incluse in executie
        test_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Login),
                                unittest.defaultTestLoader.loadTestsFromTestCase(DemoMultipleClassesTestSuite)])

        #cream raportul de executie
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports= True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )
        #rularea raportului
        runner.run(test_de_rulat)