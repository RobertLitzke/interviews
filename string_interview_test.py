import unittest
from string_interview_questions import *

class IsPalindromeTest(unittest.TestCase):
    def test(self):
        self.assertEqual(is_palindrome("ABA"),True)
        self.assertEqual(is_palindrome("racecar"),True)
        self.assertEqual(is_palindrome(""),True)
        self.assertEqual(is_palindrome("ABC"),False)
        self.assertEqual(is_palindrome("ABCDEF"),False)
        self.assertEqual(is_palindrome("ABBA"),True)
        self.assertEqual(is_palindrome("1234"),False)

    def runTest(self):
        self.test()

class ReverseTest(unittest.TestCase):
    def test(self):
        self.assertEquals(reverse("ABCDEF"),"FEDCBA")
        self.assertEquals(reverse("RL"),"LR")
        self.assertEquals(reverse(""),"")
        self.assertEquals(reverse("AAAAA"),"AAAAA")
        self.assertEquals(reverse("TESTING"),"GNITSET")

    def runTest(self):
        self.test()

class UnixPathTest(unittest.TestCase):
    def test(self):
        self.assertEquals(unix_path('/home/proc'),'/home/proc')
        self.assertEquals(unix_path('/home/proc/../rob'),'/home/rob')
        self.assertEquals(unix_path('/home/tmp/../.'),'/home')
        self.assertEquals(unix_path('/..'),'/')
        self.assertEquals(unix_path('/home/rob/.././megatron/../../..'),'/')
        self.assertEquals(unix_path('/home/./././.'),'/home')
        self.assertEquals(unix_path('/home/rob/./'),'/home/rob')

    def runTest(self):
        self.test()
                        
