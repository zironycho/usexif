import json
import exifread

from . import date
from . import geo


def fromfile(jpg_file):
    with open(jpg_file, 'rb') as f:
        tags = exifread.process_file(f)
        return {
            'latitude': geo.latitude(tags),
            'longitude': geo.longitude(tags),
            'altitude': geo.altitude(tags),
            'taken_date': date.takendate(tags),
            'tags': tags
        }
