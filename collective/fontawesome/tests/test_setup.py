import unittest
from collective.fontawesome.tests import base


class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_xxx(self):
        self.assertTrue(True)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
