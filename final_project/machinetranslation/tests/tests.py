import unittest

from translator import english_to_french, french_to_english

class Test_English_To_French(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')
    def test2(self): 
        self.assertIsNotNone(english_to_french('Hello')) 


class Test_French_To_English(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
    def test2(self):
        self.assertIsNotNone(french_to_english('Bonjour'))        

if __name__ == '__main__':
    
    unittest.main()