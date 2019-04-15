# coding: utf-8

from __future__ import absolute_import

from basic.tests import BaseTestCase


class BaseTestAliveController(BaseTestCase):
    def test_get_alive(self):
        response = self.client.open("/v1/basic/ping", method="GET")
        self.assert200(response)


if __name__ == "__main__":
    import unittest

    unittest.main()
