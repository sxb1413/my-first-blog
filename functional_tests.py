from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class CreateCVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_CV(self):
    	# Q wants to create his CV using the CV section of the site
    	self.browser.get('http://localhost:8000')

    	# He notices that there is a CV button at the top of the screen next to the title 'Sam's Blog'
    	self.assertIn("Sam's Blog", self.browser.title)
    	self.assertIn("CV", (self.browser.find_element_by_id('cvLink').text))

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 