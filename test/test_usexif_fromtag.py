import exifread
import usexif
from datetime import datetime
from unittest import TestCase


class TestExif(TestCase):
    def setUp(self):
        with open('test/asset/tag.jpg', 'rb') as f:
            self._tags = exifread.process_file(f)

    def test_latitude(self):
        latitude = usexif.geo.latitude(self._tags)
        self.assertTrue(bool(latitude))
        self.assertTrue(0 < latitude)

        self._tags['GPS GPSLatitudeRef'].values = 'S'
        latitude = usexif.geo.latitude(self._tags)
        self.assertTrue(0 > latitude)

    def test_longitude(self):
        longitude = usexif.geo.longitude(self._tags)
        self.assertTrue(bool(longitude))
        self.assertTrue(0 < longitude)

        self._tags['GPS GPSLongitudeRef'].values = 'W'
        longitude = usexif.geo.longitude(self._tags)
        self.assertTrue(0 > longitude)

    def test_altitude(self):
        altitude = usexif.geo.altitude(self._tags)
        self.assertTrue(bool(altitude))

    def test_date(self):
        taken = usexif.date.takendate(self._tags)
        self.assertEqual(datetime(2016, 4, 18, 10, 41, 6), taken)
