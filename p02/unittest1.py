import unittest
import HTMLTestRunner

class Mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有test执行前')

    @classmethod
    def tearDownClass(cls):
        print('所有test执行后')


    def setUp(self):
        print('每个test执行前')

    def tearDown(self):
        print('每个test执行后')

    def test_03(self):
        print('以test_开头，按ascil码排序顺序运行')
        self.assertEqual(23,23)

    def test_02(self):
        self.assertIn(23,[23,43,54])

if __name__ == '__main__':
    # unittest.main()
    test_suit = unittest.TestSuite()
    test_suit.addTest(Mytest('test_02'))
    fp = open('res.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='test_unittest',description='unitest框架使用')

    runner.run(test_suit)

