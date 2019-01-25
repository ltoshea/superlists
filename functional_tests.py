from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Barry checks out the new to-do list app homepage
        self.browser.get('http://localhost:8000')

        #They notice the page title and header mention to-do lists
        self.assertIn ('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        #He types "Buy peacock feather" into a text box (For fly fishing)
        inputbox.send_keys('Buy peacock feathers')
        
        #When He hits enter, the page updated, and now the page lists
        # 1: Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New Item did not appear in table"
        )
        
        #There is still a text box inviting him to add another item
        #He enters "use feathers to make a fly"
        self.fail('finish the test!')
        #The page updates again, and now shows both items on the list

        #Barry woners whether the site will remember his list. Then he sees the site had generated a unique URL for him
        #some tet explains this/

        #He visist that URL - the to-do list is still there

        #Happy he goes to sleep
if __name__ == '__main__':
    unittest.main()
