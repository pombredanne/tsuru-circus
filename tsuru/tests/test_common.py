import os
import unittest

from tsuru import common


class CommonTestCase(unittest.TestCase):

    def test_load_envs(self):
        path = os.path.join(os.path.dirname(__file__), "testdata", "apprc")
        want = {
            "VAR1": "value-1",
            "VAR2": "value2",
            "TSURU_APPNAME": "appname1",
            "TSURU_HOST": "host1",
        }
        got = common.load_envs(path)
        self.assertEqual(want, got)

    def test_load_envs_unknown_file(self):
        path = "/something/that/user/does/not/know"
        self.assertEqual({}, common.load_envs(path))
