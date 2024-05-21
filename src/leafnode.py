from htmlnode import HTMLNode
from typing import Dict, Any

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value = "",
        props: Dict[str, Any] | None = None,
        self_closing: bool = False
    ):
        super().__init__(tag=tag, value=value, props=props, self_closing=self_closing)

    def to_html(self) -> str:
        if self.tag == None: return f"{self.value}"

        if self.self_closing == True:
            return f"<{self.tag}{self.props_to_html()} />"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, LeafNode): return False

        return self.tag == value.tag and self.value == value.value and self.props == value.props and self.self_closing == value.self_closing
