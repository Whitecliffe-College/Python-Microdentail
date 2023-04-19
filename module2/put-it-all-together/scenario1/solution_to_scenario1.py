# assume our keywords dataset is predefined as below
keywords_dataset = ['python', 'java', 'c++', 'javascript', 'ruby', 'c#', 'php', 'c', 'go',  'apple', 'AI', 'ChatGPT', 'Deep learning', 'EV']

 # create an index for each keyword user searches for
import unittest
keyword_index = []
    
def create_index(keyword):
    if keyword in keywords_dataset:
        keyword_index.append(keyword)
    return keyword_index



# write unit test by using unittest library for create_index function
class TestCreateIndex(unittest.TestCase):
    def test_create_index_for_exising_keyword(self):
        keyword = 'c#'
        self.assertIn(keyword, create_index(keyword))
        # or you can use self.assertTrue(keyword in create_index(keyword))
    
    def test_create_index_for_non_exising_keyword(self):
        # you should expect this test to fail
        keyword = 'c++'
        self.assertNotIn(keyword, create_index(keyword), "keyword is not in the dataset")
        # or you can use self.assertFalse(keyword in create_index(keyword))

if __name__ == '__main__':
    unittest.main()

"""
    write unit test for create_index function by using pytest library

def test_create_index_for_exising_keyword():
    keyword = 'ChatGPT'
    assert keyword in create_index(keyword)

def test_create_index_for_non_exising_keyword():
    keyword = 'julia'
    assert keyword not in create_index(keyword)
    
"""