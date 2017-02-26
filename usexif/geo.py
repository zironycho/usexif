__author__ = 'zirony'


def _ratio2float(ratio):
    return float(ratio.num / ratio.den)


def latitude(tags):
    if 'GPS GPSLatitude' not in tags:
        return False

    neg = False
    if 'GPS GPSLatitudeRef' in tags:
        ref = str(tags['GPS GPSLatitudeRef'].values)
        neg = (ref == 'S')

    lat = _ratio2float(tags['GPS GPSLatitude'].values[0])
    lat += _ratio2float(tags['GPS GPSLatitude'].values[1]) / 60
    lat += _ratio2float(tags['GPS GPSLatitude'].values[2]) / 3600
    return -lat if neg else lat


def longitude(tags):
    if 'GPS GPSLongitude' not in tags:
        return False

    neg = False
    if 'GPS GPSLongitudeRef' in tags:
        ref = tags['GPS GPSLongitudeRef'].values
        neg = (ref == 'W')

    long = _ratio2float(tags['GPS GPSLongitude'].values[0])
    long += _ratio2float(tags['GPS GPSLongitude'].values[1]) / 60
    long += _ratio2float(tags['GPS GPSLongitude'].values[2]) / 3600
    return -long if neg else long


def altitude(tags):
    if 'GPS GPSAltitude' not in tags:
        return False

    neg = False
    if 'GPS GPSAltitudeRef' in tags:
        ref = tags['GPS GPSAltitudeRef'].values
        neg = (ref == 1)

    alt = _ratio2float(tags['GPS GPSAltitude'].values[0])
    return -alt if neg else alt
