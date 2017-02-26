# usexif
Geographic Coordinate(longitude, latitude, and altitude) from raw EXIF data
[![Build Status](https://travis-ci.org/zironycho/usexif.svg?branch=master)](https://travis-ci.org/zironycho/usexif)
[![PyPI version](https://badge.fury.io/py/usexif.svg)](https://badge.fury.io/py/usexif)


## Install
```
pip install usexif
```

## Example
```
import usexif
ret = usexif.fromfile('image/path/here.jpg')

ret['longitude']
# 126.16250277777779

ret['latitude']
# 34.36355833333334

ret['altitude']
# 3.0

ret['taken_date']
# datetime.datetime(2016, 4, 18, 10, 41, 6)
```

## Dependencies
- [exif-py](https://github.com/ianare/exif-py)
