import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class PrintBookConsole:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookReverse:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class DisplayBookConsole:
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayBookReverse:
    def display(self, book: Book) -> None:
        print(book.content[::-1])


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display_console = DisplayBookConsole()
                display_console.display(book)
            if method_type == "reverse":
                display_reverse = DisplayBookReverse()
                display_reverse.display(book)
        elif cmd == "print":
            if method_type == "console":
                print_console = PrintBookConsole()
                print_console.print_book(book)
            if method_type == "reverse":
                print_reverse = PrintBookReverse()
                print_reverse.print_book(book)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
