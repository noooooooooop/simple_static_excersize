# from typing import Type

class TextNode:
    def __init__(self, text: str, text_type:str , url: str = ""):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode): return NotImplemented

        return self.url == value.url and self.text_type == value.text_type and self.text == value.text

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
