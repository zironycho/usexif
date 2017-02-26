import usexif
from unittest import TestCase
import exifread


class TestNoExif(TestCase):
    def setUp(self):
        with open('test/asset/notag.jpg', 'rb') as f:
            self._tags = exifread.process_file(f)

    def test_notag(self):
        self.assertFalse(usexif.geo.latitude(self._tags))
        self.assertFalse(usexif.geo.longitude(self._tags))
        self.assertFalse(usexif.geo.altitude(self._tags))
        self.assertFalse(usexif.date.takendate(self._tags))
