from character import Character
from cursor import Cursor


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))
    
if __name__ == "__main__":
    d = Document()
    for i in "apple":
        d.insert(Character(i, bold=True))
    #d.insert(Character('w', italic=True))
    d.insert('\n')
    print('-'*20+'\n'+'first word')
    print(d.string)
    for i in "banana":
        d.insert(Character(i))
    print('-'*20+'\n'+'second word')
    print(d.string)
    d.cursor.home()
    d.insert("*")
    print('-'*20+'\n'+'after insert from head')
    print(d.string)