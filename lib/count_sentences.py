#!/usr/bin/env python3

class MyString:
    def __init__(self, value: str = ""):
        # Use the property setter for validation
        self.value = value

    @property
    def value(self) -> str:
        return getattr(self, "_value", "")

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self) -> bool:
        return self.value.endswith(".")
    
    def is_question(self) -> bool:
        return self.value.endswith("?")

    def is_exclamation(self) -> bool:
        return self.value.endswith("!")
    
    def count_sentences(self) -> int:
        import re
        # Split the string by sentence-ending punctuation followed by whitespace or end of string
        sentences = re.split(r'[.!?]+(?=\s|$)', self.value)
        # Filter out any empty strings that may result from the split
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)