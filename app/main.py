import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintBookConsole(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookReverse(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class DisplayBookConsole:
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayBookReverse:
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class SerializeBookJson:
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookXml:
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


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
            if method_type == "xml":
                xml_serialize = SerializeBookXml()
                return xml_serialize.serialize(book)
            if method_type == "json":
                json_serialize = SerializeBookJson()
                return json_serialize.serialize(book)
        else:
            raise ValueError("Unknown data type")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
