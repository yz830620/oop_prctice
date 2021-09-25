"""define user and host forming it"""
#python built-in
import hashlib
import datetime as dt
from typing import List
from calendar import Session

class User:
    """class to define user"""
    all_user = []
    def __init__(self, name: str, password: str, email: str, skype: str, line: str):
        self.name = name
        self.password = self._encrypt_pw(password)
        self.email = email
        self.skype = skype
        self.line = line
        self.points = 100
        self.enroll_list = []
        self.host_list = []
        self.create_date = dt.date
        User.all_user.append(self)

        self.is_logged_in = False

    def _encrypt_pw(self, password):
        "return encrypted password"
        hash_string = self.username + password
        hash_string = hash_string.encode("utf-8")
        return hashlib.sha256(hash_string).hexdigest()
    
    def enroll(self, session: Session):
        self.enroll_list.append(session)
        session.attendee.append(self)
        if len(session.attendee) > 4:
            print("Alert! Might not be host by the {session.host.name} shown.")
    
    def host(self, session: Session):
        # TODO: consider dt issue
        if not session.host:
            session.host = self
            print("Session: {session.time}\n host has been set to {session.host.name}")
            return True
        else:
            print("Session: {session.time}\n host has been occupied by {session.host.name}")
            return False

    def host_set_topic(self, session, topic, topic_link):
        # TODO: consider dt issue
        if session.host.name != self.name:
            raise ValueError("Topic only can be setup by host! Please be the host first or pick another session")
        else:
            session.topic = topic
            session.topic_link = topic_link

    def record(self, session, record):
        # TODO: consider dt issue
        session.record[self.name] = record







