import unittest

def fib(n):
    return( 1 if(n<=2) else fib(n-1)+fib(n-2))

def setUpModule():
    print("setup module")

def tearDownModule():
    print("teardown module")

class TestFib(unittest.TestCase):

    def setup(self):
        print("setup")
        self.n = 10

    def tearDown(self):
        print("teardown")
        del self.n

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)
    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)

    if __name__ == "__main__":
        unittest.main()
