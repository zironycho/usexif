import usexif
from unittest import TestCase


class TestKwargs(TestCase):
    def test_details(self):
        
        ret = usexif.fromfile(
            'test/asset/detail_is_not_good.jpg',
            details=False
        )

        self.assertTrue(ret['latitude'])
        self.assertTrue(ret['longitude'])
        self.assertTrue(ret['altitude'])
        self.assertTrue(ret['taken_date'])

