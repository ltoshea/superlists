from selenium import webdriver
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
        self.fail('Finish the test!')

        #He is invited to enter a to-do item straight away

        #He types "Buy peacock feather" into a text box (For fly fishing)

        #When He hits enter, the page updated, and now the page lists
        # 1: Buy peacock feathers as an item in a to-do list

        #There is still a text box inviting him to add another item
        #He enters "use feathers to make a fly"

        #The page updates again, and now shows both items on the list

        #Barry woners whether the site will remember his list. Then he sees the site had generated a unique URL for him
        #some tet explains this/

        #He visist that URL - the to-do list is still there

        #Happy he goes to sleep
if __name__ == '__main__':
    unittest.main()
