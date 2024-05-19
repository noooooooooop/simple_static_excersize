from typing import List, Any, Dict

class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: Any = None,
        children: object | List[object] | None = None,
        props: Dict[str, Any] | None = None
    ):
        #Validate that children are proper HTML nodes
        if not isinstance(children, (list, HTMLNode)) and children != None:
            raise ValueError("children must be of type HTMLNode, List[HTMLNode] or None")

        if isinstance(children, list):
            for child in children:
                if not isinstance(child, HTMLNode) and child != None:
                    raise ValueError("children must be of type HTMLNode, List[HTMLNode] or None")

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None: return ""

        return "".join(map(lambda item: f" {item[0]}=\"{item[1]}\"", self.props.items()))

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, HTMLNode):
            return False

        #return f"{self}" == f"{value}"

        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props
