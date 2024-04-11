import unittest

ONLY_LAST = False


class TestAPI(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(42, 42)

    def test_fail(self):
        self.assertEqual(42, 43)

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_states_mean(self):
        self.helper_test_endpoint("states_mean")

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_state_mean(self):
        self.helper_test_endpoint("state_mean")

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_best5(self):
        self.helper_test_endpoint("best5")

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_worst5(self):
        self.helper_test_endpoint("worst5")

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_global_mean(self):
        self.helper_test_endpoint("global_mean")

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_diff_from_mean(self):
        self.helper_test_endpoint("diff_from_mean")

    @unittest.skipIf(ONLY_LAST, "Checking only the last added test")
    def test_state_diff_from_mean(self):
        self.helper_test_endpoint("state_diff_from_mean")

if __name__ == '__main__':
    unittest.main()
    
