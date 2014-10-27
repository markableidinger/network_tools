from echo_server import *
from echo_client import *
import unittest


class EchoTestCase(unittest.TestCase):
    '''Tests for echo_client.py and echo_server.py'''
    def test_echo(self):
        self.assertTrue(echo_client('test passed')[1] == 'test passed')

    def test_unicode_echo(self):
        self.assertTrue(echo_client(u'test passed')[1] == 'test passed')
