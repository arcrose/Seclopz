import unittest

import seclopzapi


class SeclopzapiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = seclopzapi.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to seclopz-api', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
