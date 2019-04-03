import unittest
import HTMLTestRunner

suit = unittest.TestSuite()
all_cases = unittest.defaultTestLoader.discover('.','test_*.py')

for case in all_cases:
    suit.addTest(case)
fp = open('res.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(fp,title='all_cases',description='所有用例')
runner.run(suit)
