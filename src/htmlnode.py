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

        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props

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
        if not isinstance(value, HTMLNode):
            return False

        return self.tag == value.tag and self.children == value.children and self.props == value.props
