"""class note"""
import datetime

last_id=0

class Note:
    def __init__(self, memo: str, tags: str=""):
        self.memo = memo
        self.tags = tags
        self.creation_data = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, search_filter:str) -> bool:
        return search_filter in self.memo or search_filter in self.tags
