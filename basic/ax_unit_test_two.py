import unittest
import ax_unit_test_one

class TestCap(unittest.TestCase):
    # unit test case names should start with test_
    def test_one_word(self):
        text='python'
        result=ax_unit_test_one.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multi_word(self):
        text='raj karan'
        result=ax_unit_test_one.cap_text(text)
        self.assertEqual(result,'Raj Karan')

    

if __name__=='__main__':
    unittest.main()


# first run error AssertionError: 'Raj karan' != 'Raj Karan'
# Ran 2 tests in 0.001s
#
# FAILED (failures=1)


#after fix:
# Ran 2 tests in 0.000s
#
# OK

print(test_multi_word)