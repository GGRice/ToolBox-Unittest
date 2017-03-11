"""
    Explores unittest and it's functionality

    Author: Gretchen Rice
    Date: March 11, 2017
"""




import unittest

def remove_negs(num_list):
    """
        Removes negative values from a list
    """
    no_negs = [number for number in num_list if number >= 0]

    return no_negs

class TestListMethods(unittest.TestCase):

    def test_sort(self):
        """
            Tests the sort method of list
        """
        word_list = ['apple', 'pineapple', 'bannana', 'turtle']
        word_list.sort()
        self.assertEqual(word_list, ['apple', 'bannana', 'pineapple', 'turtle'])
        number_list = [7, 1, 3, 4, 2]
        number_list.sort()
        self.assertEqual(number_list, [1, 2, 3, 4, 7])

    def test_removenegative(self):
        """
            Tests the method I created to remove negative values
        """
        number_list = [1, 3, -1, -76, 9]
        print(number_list.sort())
        self.assertEqual(remove_negs(number_list), [1, 3, 9])

if __name__ == '__main__':
    unittest.main()
