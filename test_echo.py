from echo_server import *
from echo_client import *
import unittest


class EchoTestCase(unittest.TestCase):
    '''Tests for echo_client.py and echo_server.py'''
    def test_echo(self):
        print(echo_client('test passed'))
        self.assertTrue(echo_client('test passed')[1] == 'test passed')
