from unittest import TestCase

import usexif


class TestStrange(TestCase):
    def test_strange_1(self):
        ret = usexif.fromfile('test/asset/tag_without_ref.jpg')
        self.assertTrue(ret['latitude'] > 0)
        self.assertTrue(ret['longitude'] > 0)
        self.assertTrue(ret['altitude'] > 0)
