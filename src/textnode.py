# from typing import Type

class TextNode:
    def __init__(self, text: str, text_type:str , url: str = ""):
        try:
            str(text)
            str(text_type)
            str(url)
        except ValueError:
            raise ValueError("text, text_type and url(if present) must be strings")

        self.text = str(text)
        self.text_type = str(text_type)
        self.url = str(url)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode): return False

        return self.url == value.url and self.text_type == value.text_type and self.text == value.text

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
