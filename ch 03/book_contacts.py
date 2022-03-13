"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 3, When Objects Are Alike.
"""
from __future__ import annotations
from typing import Optional, Protocol, Any

## Extending built-ins


class ContactList(list):
    def search(self, name: str) -> list["Contact"]:
        """All contacts with search name in name."""
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, /, name: str = "", email: str = "", **kwargs: Any) -> None:
        super().__init__(**kwargs)  # type: ignore [call-arg]
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" f"{self.name!r}, {self.email!r}" f")"


test_search = """
Contact.all_contacts = ContactList()

Contact("John A", "johna@example.net")
Contact("John B", "johnb@sloop.net")
Contact("Jenna C", "cutty@sark.io")
[c.name for c in Contact.all_contacts.search('John')]
['John A', 'John B']
"""

