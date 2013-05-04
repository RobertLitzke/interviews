import unittest
from math_interview_questions import *

class DigitalRootTest(unittest.TestCase):
    def test(self):
        for x in [digital_root,digital_root_s]:
            self.assertEquals(x(5),5)
            self.assertEquals(x(31337),8)
            self.assertEquals(x(15),6)
            self.assertEquals(x(199),1)
            self.assertEquals(x(700),7)

    def runTest(self):
        self.test()
