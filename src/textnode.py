from leafnode import LeafNode

text_types = [
    "text",
    "bold",
    "italic",
    "code",
    "link",
    "image",
]
    
class TextNode:
    def __init__(self, text: str, text_type: str, url: str = ""):
        if not text_type in text_types: 
            raise ValueError("invalid text_type. must be text, bold, italic, code, link or image.")

        if not isinstance(text, str):
            raise ValueError("invalid text. must a string")

        if not isinstance(url, str):
            raise ValueError("invalid url. must a string")

        self.text = str(text)
        self.text_type = str(text_type)
        self.url = str(url)

    def convert_to_html_node(self):
        match self.text_type:
            case "text":
                return LeafNode(value=self.text)
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                return LeafNode("a", self.text, {"href": self.url})
            case "image":
                return LeafNode("img", props={"src": self.url, "alt": self.text}, self_closing=True)
            case _:
                raise ValueError("invalid text_type. must be text, bold, italic, code, link or image.")

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode): return False

        return self.url == value.url and self.text_type == value.text_type and self.text == value.text

    def __repr__(self) -> str:
        return f"TextNode(\"{self.text}\", \"{self.text_type}\", \"{self.url}\")"
