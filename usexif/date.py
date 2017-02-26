from datetime import datetime

__author__ = 'zirony'


def takendate(tags):
    if ('EXIF DateTimeOriginal' in tags) and (0 < len(tags['EXIF DateTimeOriginal'].values)):
        taken = tags['EXIF DateTimeOriginal'].values
    elif ('EXIF DateTimeDigitized' in tags) and (0 < len(tags['EXIF DateTimeDigitized'].values)):
        taken = tags['EXIF DateTimeDigitized'].values
    elif ('Image DateTime' in tags) and (0 < len(tags['Image DateTime'].values)):
        taken = tags['Image DateTime'].values
    else:
        return False

    return datetime.strptime(taken, '%Y:%m:%d %H:%M:%S')
