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

    	# He clicks the CV button and it takes him to a new page
    	# This page will display the CV and allow Q to edit it if he has admin access by pressing the edit button at the top of the page
    	# A form with fields for name, phone number, email address, intro, education, experience, skills and interests appears on the page
    	# After filling in these boxes he notices a save button at the bottom of the screen
    	# He presses the save button
    	# This redirects him to the view of the CV, which should now be filled with the information he just entered.


if __name__ == '__main__':  
    unittest.main(warnings='ignore') 