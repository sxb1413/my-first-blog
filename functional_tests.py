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
    	self.browser.find_element_by_id('cvLink').click();
    	self.assertIn("http://localhost:8000/cv.html", self.browser.current_url)

    	# This page will display the CV and allow Q to input information into the CV
    	# A form with fields for name, phone number, email address, intro, education, experience, skills and interests appears on the page
    	name_input = self.browser.find_element_by_id('cv_name')
    	self.assertIn("Name", name_input.get_attribute('placeholder'))
    	phone_input = self.browser.find_element_by_id('cv_phone')
    	self.assertIn("Phone Number", phone_input.get_attribute('placeholder'))
    	email_input = self.browser.find_element_by_id('cv_email')
    	self.assertIn("Email Address", email_input.get_attribute('placeholder'))
    	intro_input = self.browser.find_element_by_id('cv_intro')
    	self.assertIn("Intro", intro_input.get_attribute('placeholder'))
    	education_input = self.browser.find_element_by_id('cv_education')
    	self.assertIn("Education", education_input.get_attribute('placeholder'))
    	experience_input = self.browser.find_element_by_id('cv_experience')
    	self.assertIn("Experience", experience_input.get_attribute('placeholder'))
    	skills_input = self.browser.find_element_by_id('cv_skills')
    	self.assertIn("Skills", skills_input.get_attribute('placeholder'))
    	interests_input = self.browser.find_element_by_id('cv_interests')
    	self.assertIn("Interests", interests_input.get_attribute('placeholder'))

    	# After filling in these boxes he notices a save button at the bottom of the screen
    	# He presses the save button
    	# The CV should now have been updated with the information that Q has just entered


if __name__ == '__main__':  
    unittest.main(warnings='ignore') 