"""class notebook"""
from notebook.note import Note

class Notebook:
    def __init__(self):
        self.notes = []
    
    def search(self, filter: str):
        return [note for note in self.notes if note.match(filter)]

    def new_note(self, memo, tag=""):
        self.notes.append(Note(memo, tag))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo

    def modify_tag(self, note_id, tag):
        for note in self.notes:
            if note.id == note_id:
                note.tag = tag