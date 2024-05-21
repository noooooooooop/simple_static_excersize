from textnode import TextNode
from typing import List, Type
import re

text_types = [
    "text",
    "bold",
    "italic",
    "code",
    "link",
    "image",
]
    
delimiters = {
    "*": "bold",
    "**": "italic",
    "`": "code",
}

def extract_markdown_links(old_nodes: object | List[object], is_image: bool = False):
    #Validation
    if not isinstance(old_nodes, (list, TextNode)):
        raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    if isinstance(old_nodes, list):
        for node in old_nodes:
            if not isinstance(node, TextNode):
                raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    nodes: List[TextNode] = []

    if isinstance(old_nodes, TextNode):
        nodes = [old_nodes]
    else:
        # TODO: type system doesn't account for type narrowing of lists.
        #       either need to typecast or find a way to ignore
        #
        # pyright: ignore
        nodes = old_nodes

    matches = []
    
    #transformation
    for node in nodes:
        matches.extend(__extract_single_markdown_link(node, is_image))

    return matches

def __extract_single_markdown_link(old_node: object, is_image: bool = False):
    #Validation
    if not isinstance(old_node, TextNode):
        raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    matches = []

    if is_image == True:
        matches = re.findall(r"!\[(.*?)\]\((.*?)\)", old_node.text)
    else:
        matches = re.findall(r"(^|[^!])\[(.*?)\]\((.*?)\)", old_node.text)
        matches = map(lambda x: (x[1], x[2]), matches)

    return matches

def split_nodes_delimiter(old_nodes: object | List[object], delimiter, text_type):
    #Validation
    if not isinstance(old_nodes, (list, TextNode)):
        raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    if isinstance(old_nodes, list):
        for node in old_nodes:
            if not isinstance(node, TextNode):
                raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    nodes: List[TextNode] = []

    if isinstance(old_nodes, TextNode):
        nodes = [old_nodes]
    else:
        # TODO: type system doesn't account for type narrowing of lists.
        #       either need to typecast or find a way to ignore
        #
        # pyright: ignore
        nodes = old_nodes

    if delimiter not in delimiters: raise ValueError("Invalid delimiter")

    if text_type not in text_types: raise ValueError("Invalid text_types")

    new_nodes = []

    #transformation
    for node in nodes:
        new_nodes.extend(__split_single_node_delimiter(node, delimiter, node.text_type))

    return new_nodes

def __split_single_node_delimiter(old_node: object, delimiter: str, text_type: str):
    #Validation
    if not isinstance(old_node, TextNode):
        raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    #transformation
    chunks = old_node.text.split(delimiter)

    new_nodes = []

    for i in range(0, len(chunks)):
        new_type = text_type

        if i % 2 == 1: new_type = delimiters[delimiter]

        if chunks[i] != "": new_nodes.append(TextNode(chunks[i], new_type))

    return new_nodes

def main():
    test = TextNode('asdfasdfsfasdf', 'aasdfafsd', 'http://not.a.real.website.asdfasdfasdfasdfasdfadfdasf')
    print(test)

if __name__ == '__main__':
    main()
