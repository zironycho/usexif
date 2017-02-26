__author__ = 'zirony'


def _ratio2float(ratio):
    return float(ratio.num / ratio.den)


def latitude(tags):
    try:
        ref = str(tags['GPS GPSLatitudeRef'].values)
    except KeyError:
        return False

    neg = (ref == 'S')

    lat = _ratio2float(tags['GPS GPSLatitude'].values[0])
    lat += _ratio2float(tags['GPS GPSLatitude'].values[1]) / 60
    lat += _ratio2float(tags['GPS GPSLatitude'].values[2]) / 3600

    return -lat if neg else lat


def longitude(tags):
    try:
        ref = tags['GPS GPSLongitudeRef'].values
    except KeyError:
        return False

    neg = (ref == 'W')

    long = _ratio2float(tags['GPS GPSLongitude'].values[0])
    long += _ratio2float(tags['GPS GPSLongitude'].values[1]) / 60
    long += _ratio2float(tags['GPS GPSLongitude'].values[2]) / 3600
    return -long if neg else long


def altitude(tags):
    try:
        ref = tags['GPS GPSAltitudeRef'].values
    except KeyError:
        return 0

    neg = (ref == 1)

    alt = _ratio2float(tags['GPS GPSAltitude'].values[0])
    return -alt if neg else alt
