import unittest

from pytest_envfiles.plugin import parse_env_file
import os


class EnvFileParsingTests(unittest.TestCase):
    def test_basic_parsing(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'envfile.example'))
        parse_env_file(file_path)

        self.assertEqual(os.environ['STUFF'], '')
        self.assertEqual(os.environ['SNAFU'], 'All your base are belong to us')
        self.assertEqual(os.environ['ANSWER'], '42')
