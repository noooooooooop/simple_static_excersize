from textnode import TextNode
from typing import List
import re

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
