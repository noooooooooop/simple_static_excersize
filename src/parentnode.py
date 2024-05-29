from os import walk
from htmlnode import HTMLNode
from leafnode import LeafNode
from typing import Dict, Any, List

class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        children: object | List[object] = None,
        props: Dict[str, Any] | None = None
    ):
        if children == None:
            raise ValueError("ParentNode requires \"children\" to be defined")

        if tag == None:
            raise ValueError("ParentNode requires a \"tag\" to be defined")

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        children = ""

        if isinstance(self.children, (ParentNode, LeafNode)):
            children = self.children.to_html()

        if isinstance(self.children, list):
            children = f"{"".join(map(lambda child: child.to_html(), self.children))}"

        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, ParentNode):
            return False

        return self.tag == value.tag and self.children == value.children and self.props == value.props


    def __repr__(self) -> str:
        return \
f"""ParentNode(
    tag: {self.tag},
    value: {self.value},
    children: {self.children},
    props: {self.props},
    self_closing: {self.self_closing}
)"""
