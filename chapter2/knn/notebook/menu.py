import sys
from notebook.notebook import Notebook
from notebook.note import Note


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choice = {
            "1": self.show_notes,
            "2": self.search_note,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
    def display_menu(self):
        print("""
        Notebook Menu

        1. Show all note
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    
    def run(self):
        """display menu and responese to choices"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_note(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()