from math import ceil, floor


def make_readable(seconds):
    
    hours=floor(seconds/3600)
    minutes=floor((seconds/3600-hours)*60)
    new_seconds=round((((seconds/3600-hours)*60)-minutes)*60)
    if new_seconds>=60:
        minutes+=1
        new_seconds=0

    return "{hours}:{minutes}:{seconds}".format(hours=str(hours).zfill(2),minutes=str(minutes).zfill(2),seconds=str(new_seconds).zfill(2))