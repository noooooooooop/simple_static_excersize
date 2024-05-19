from htmlnode import HTMLNode
from typing import Dict, Any

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value = None,
        props: Dict[str, Any] | None = None
    ):
        if value == None:
            raise ValueError("LeafNode requires a value to be defined")

        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag == None: return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, HTMLNode):
            return False

        return self.tag == value.tag and self.value == value.value and self.props == value.props
