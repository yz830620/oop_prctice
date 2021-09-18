"""define calendar and sessions forming it"""
#python built-in
import datetime as dt
from typing import List

#local class import
from user import User

class Session:
    """main object of the system
    Attr:
        session_time: dt
        host: User
        attendee: List[User]
        record: dict[User, (dt, wav)]
        topic: (str, path, dt)
        qestions: List[int, (str, dt)]
    Method:
        contact_time()
        generate_chat_room(host, attendee)
    """
    session_in_the_month = []
    def __init__(self, session_time):
        self.session_time: dt = session_time
        self.host: User = None
        self.attendee: List[User]= []
        #TODO implement wav ...
        self.record: List[Wav] = []
        self.topic: str = None
        self.question: List[str] = []
        Session.session_in_the_month.append(self)


class Calendar:
    """list of Session
    Attr:
        events: List[Session]
    """
    def __init__(self):
        """
        Logic chain:
            1. count monthly weekday arrangement
            2. setup sessions for every day
        """
        pass

class Wav:
    "audio file format"
    pass