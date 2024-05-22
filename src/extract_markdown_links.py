from textnode import TextNode
from typing import List
import re

def split_markdown_links(old_nodes: object | List[object], is_image: bool = False):
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

    new_nodes = []

    #transformation
    for node in nodes:
        if node.text_type == "text":
            new_nodes.extend(__split_markdown_links(node, is_image))
        else:
            new_nodes.append(node)

    return new_nodes

def __split_markdown_links(old_node: object, is_image: bool = False):
    #Validation
    if not isinstance(old_node, TextNode):
        raise ValueError("Only text nodes should be passed in to split_nodes_delimiter.")

    matches = extract_markdown_links(old_node, is_image)

    new_nodes = []
    node = old_node

    for (text, link) in matches:
        split = node.text.split(f"{"!" if is_image == True else ""}[{text}]({link})", 1)

        before = split[0]
        after = ""
        if len(split) > 1: after = split[1]

        if before != "":
            new_nodes.append(TextNode(before, old_node.text_type, old_node.url))

        new_nodes.append(TextNode(text, "image" if is_image == True else "link", link))

        node.text = after

    if node.text != "": new_nodes.append(TextNode(node.text, old_node.text_type))

    return new_nodes

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
        matches = list(map(lambda x: (x[1], x[2]), matches))

    return matches
