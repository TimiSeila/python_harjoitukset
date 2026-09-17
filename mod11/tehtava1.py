class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Kirjan nimi: {self.name}")
        print(f"Julkaisija: {self.author}")
        print(f"Sivumäärä: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Lehden nimi: {self.name}")
        print(f"Päätoimittaja: {self.chief_editor}")

donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_six = Book("Compartment No. 6", "Rosa Liksom", 192)

compartment_no_six.print_information()
donald_duck.print_information()
