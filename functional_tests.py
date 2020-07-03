from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class CreateCVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
            table = self.browser.find_element_by_id('cv_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])

    def test_create_CV(self):
        # Q wants to create his CV using the CV section of the site
        self.browser.get('http://localhost:8000')

        # He notices that there is a CV button at the top of the screen next to the title 'Sam's Blog'
        self.assertIn("Sam's Blog", self.browser.title)
        self.assertIn("CV", (self.browser.find_element_by_id('cvLink').text))

        # He clicks the CV button and it takes him to a new page
        self.browser.find_element_by_id('cvLink').click()
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

        # He fills in the fields
        name_input.send_keys('Sam Bird')
        phone_input.send_keys('07980390533')
        email_input.send_keys('Samcbird3@gmail.com')

        intro_text = 'A highly motivated and hardworking individual, who has successfully completed one year of a four year Msci Computer Science degree at The University of Birmingham./nPractically minded with a methodical approach to working and an eagerness to learn, whilst developing personal skills in a practical setting.'
        for intro in intro_text.split('/n'):
            intro_input.send_keys(intro)
            intro_input.send_keys(Keys.ENTER)

        education_input.send_keys('A-levels: A - Computer Science, A - German, A - Maths, C - Physics')
        experience_text = "Hack The Midlands       3.0 and 4.0                     2018 and 2019/nCollaborated, at this 24 hour hackathon, in a team of four to create a web service to report crimes in a mainly student-populated residential area near our University/nin 2018, then create a web-based game this year. Furthering my team-working, coding and public speaking skills were the main advantages of these experiences./n/nArtificial Intelligence - Robotics Assignment               2018/nCreated and programmed a robot to complete a variety of tasks, one being traversing a maze. This team project enhanced my understanding of artificial intelligence,/nas well as improving my team-working skills; we split tasks into subtasks for each member in order to meet deadlines, therefore requiring regular communication. /n/nA&H Accountants                                 2017/nChoosing to go to A&H Accountants for a one week placement was inspired by my experience being Financial Director of the Friesland School Young Enterprise team./nDuring the week, my duties involved entering and organising customers’ accounts and receipts, as I gained more knowledge of the workings of an office./n/nYoung Enterprise                                    2016 - 2017/nFinancial Director for the Friesland School Young Enterprise company, Quantum. The team progressed to the County Finals and received the following awards throughout/nthe process: Best Company Report, Best Financial Management, Best Presentation, Best Company and the Creativity and Innovation Award./nThe company has made a healthy profit through selling our self-designed and written childrens’ books. Facebook – Team Quantum 2016. Instagram - teamquantum2016/n/nENSEK                                       2015/nJoining the ENSEK team for a week helped me to understand how to work with others in a professional environment, at this local software company specialising in the/noptimisation of billing, data collection etc. for energy providers./n/nFootball Referee                                2014 - present/nReferee for mini soccer, 9v9, 11v11, youth, ladies and open-age football. Duties include:/nHelping all young players develop/nClaim responsibility for the pitch/players safety/nEnsure FA Respect procedures of all spectators and players are adhered to/nEnsure FA Laws of the game are followed/n/nMember of the Derbyshire FA Referee Academy from 2016-2017 attending regular meetings and coaching sessions to help improve skills, before deciding to leave in order/nto focus on my studies. Refereed at Saint George’s Park and was assistant referee at Derby County Academy and the Nottingham Young Elizabethan League Cup Final 2016/2017./nCurrently referee in the Birmingham AFA League and CWYL.'"
        #experience_text = experience_text.replace("\n", "<br>")
        #ActionChains(self.browser).key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform() send_keys(Keys.SHIFT + Keys.ENTER)
        for part in experience_text.split('/n'):
            experience_input.send_keys(part)
            experience_input.send_keys(Keys.ENTER)
            #ActionChains(self.browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
        
        skills_text = 'Accomplished communication skills, both written and verbal, developed through regular essays and presentations/nAbility to take initiative and work well under pressure, ensuring strict deadlines are met, as successfully demonstrated in last exam results/nExperienced using Java, Python, Haskell and some basic C, HTML, CSS, JavaScript and SQL/nProficient in using systems on both the Windows and Linux operating systems, with small experience on Android OS and mac OS'
        for skill in skills_text.split('/n'):
            skills_input.send_keys(skill)
            skills_input.send_keys(Keys.ENTER)
        
        interests_text = 'Football Coaching/nVolunteering with the Under 13 Breaston Park FC team of 15 players. Responsibility for running coaching drills and developing the young players skills whilst ensuring/ntheir safety and helping to build their confidence./n/nLong Eaton Operatic Society (LEOS) / The Cast / Carlton Operatic Society/nActive member of backstage team for both adult and youth group productions. Building and dismantling scenery and staging for the performances. Completing backstage/nduties at The Theatre Royal Nottingham, The Nottingham Playhouse, Duchess Theatre Long Eaton and May Hall. Received 6 year NODA (National Operatic Drama Association)/naward for voluntary contribution to amateur theatre./n/nSnooker and Pool Society/nCurrent member of the snooker and pool society at the University of Birmingham, this involves weekly commitment to practice sessions plus competing in tournaments/nthroughout the year.'
        for interest in interests_text.split('/n'):
            interests_input.send_keys(interest)
            interests_input.send_keys(Keys.ENTER)

        # After filling in these boxes he notices a save button and clicks it
        self.browser.find_element_by_id('cv_save').click()

        # The CV should now have been updated with the information that Q has just entered
        time.sleep(5)
        #self.check_for_row_in_table("Sam Bird")
        #self.check_for_row_in_table("07980390533")
        #self.check_for_row_in_table("Samcbird3@gmail.com")
        #self.check_for_row_in_table("A highly motivated and hardworking individual, who has successfully completed one year of a four year Msci Computer Science degree at The University of Birmingham. Practically minded with a methodical approach to working and an eagerness to learn, whilst developing personal skills in a practical setting.")
        #self.check_for_row_in_table("A-levels: A - Computer Science, A - German, A - Maths, C - Physics")
        #self.check_for_row_in_table(experience_text)
        #self.check_for_row_in_table(skills_text)
        #self.check_for_row_in_table(interests_text)

        
if __name__ == '__main__':  
    unittest.main(warnings='ignore') 