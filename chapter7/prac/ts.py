import datetime


def frame_to_time(frame_idx, fps):
    """frame_to_time: convert frame_idx to video time with micro seconds.
    Arguments:
        frame_idx: int, frame index of video.
        fps: int, frames per second of video.
    Returns:
        datetime: str, time with formate hh:mm:ss of video.
    """
    second = frame_idx/fps
    # %f is micro seconds
    time_format = "%H:%M:%S.%f"
    # if integer, we don't need micro seconds
    if second.is_integer():
        time_format = "%H:%M:%S"
    return datetime.datetime.strftime(datetime.datetime.strptime(str(datetime.timedelta(seconds=frame_idx/fps)), time_format), time_format)

def frame_to_time1(frame_idx, fps):
    """frame_to_time: convert frame_idx to video time with micro seconds.
    Arguments:
        frame_idx: int, frame index of video.
        fps: int, frames per second of video.
    Returns:
        datetime: str, time with formate hh:mm:ss of video.
    """
    second = frame_idx/fps
    # %f is micro seconds
    time_format = "%H:%M:%S.%f"
    # if integer, we don't need micro seconds
    if second.is_integer():
        time_format = "%H:%M:%S"
    return datetime.timedelta(seconds=frame_idx/fps)


ftime = frame_to_time(400001, 40)
ftime1 = frame_to_time1(400001, 40)

print(type(ftime))
print(ftime)
print(type(ftime1))
print(ftime1)