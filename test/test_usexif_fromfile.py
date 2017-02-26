import usexif
from unittest import TestCase
from datetime import datetime


class TestDoit(TestCase):
    def test_class(self):
        r = usexif.fromfile('test/asset/tag.jpg')
        self.assertEqual(float, type(r['latitude']))
        self.assertTrue(r['latitude'] > 0)
        self.assertEqual(float, type(r['longitude']))
        self.assertTrue(r['longitude'] > 0)
        self.assertEqual(float, type(r['altitude']))
        self.assertTrue(r['altitude'] > 0)
        self.assertEqual(datetime, type(r['taken_date']))
        self.assertTrue(r['taken_date'] > datetime(2016, 1, 1))
        self.assertEqual(dict, type(r['tags']))
        self.assertTrue(r['tags'])

    def test_notag(self):
        r = usexif.fromfile('test/asset/notag.jpg')
        self.assertEqual(bool, type(r['latitude']))
        self.assertEqual(bool, type(r['longitude']))
        self.assertEqual(0, r['altitude'])
        self.assertEqual(bool, type(r['taken_date']))
        self.assertEqual(dict, type(r['tags']))
        self.assertFalse(r['tags'])

