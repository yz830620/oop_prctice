"""define calendar and sessions forming it"""
#python built-in
import datetime as dt
from typing import List

#local class import
from user import User

class Session:
    """main object of the system
    Attr:
        host: User
        attendee: List[User]
        record: dict[User, (dt, wav)]
        topic: (str, path, dt)
        qestions: List[int, (str, dt)]
    Method:
        contact_time()
        generate_chat_room(host, attendee)
    """
    def __init__():
        
        pass


class calendar:
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