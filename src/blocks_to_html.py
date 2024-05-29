import re
from typing import List

from main import convert_markdown_to_textnodes
from markdown_split_blocks import get_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode

def block_ordered_list_to_html(block: str):
    lines = [re.sub(r"^[0-9][0-9]?[0-9]?\.\s", "", block) for block in block.split("\n")]

    html_nodes = []

    # TODO: each inline node is getting its' own parents, need to be grouped.
    for line in lines:
        text_nodes = convert_markdown_to_textnodes(line)

        html_nodes.append(
            ParentNode(
                "li", [node.convert_to_html_node() for node in text_nodes]
            )
        )

    return ParentNode("ol", html_nodes)

def block_unordered_list_to_html(block: str):
    lines = [re.sub(r"^\*\s", "", block) for block in block.split("\n")]

    html_nodes = []

    # TODO: each inline node is getting its' own parents, need to be grouped.
    for line in lines:
        text_nodes = convert_markdown_to_textnodes(line)

        html_nodes.append(ParentNode(
            "li", [node.convert_to_html_node() for node in text_nodes]
        ))

    return ParentNode("ul", html_nodes)

def block_quote_to_html(block: str):
    lines = [re.sub(r"^\>\s", "", block) for block in block.split("\n")]

    html_nodes = []

    # TODO: each inline node is getting its' own parents, need to be grouped.
    for line in lines:
        text_nodes = convert_markdown_to_textnodes(line)

        html_nodes.append(ParentNode(
            "p", [node.convert_to_html_node() for node in text_nodes]
        ))

    return ParentNode("blockquote", html_nodes)

# TODO: make sure this is formatted correctly, whitespace might be stripped
def block_code_to_html(block: str):
    html = block.replace("```", "")

    return ParentNode("pre", [
         LeafNode("code", html),
    ])

# NOTE: By the time this function is called, headers should already be
#       broken up individually.
#
#       If a string with multiple headings is passed in it is a bug.
def block_headings_to_html(block: str):
    regex = r"^[#]{1,6}\s"

    matches = re.findall(regex, block)

    heading_rank = 0
    
    text_nodes = convert_markdown_to_textnodes(re.sub(regex, "", block))

    if len(matches) > 0:
        heading_rank = len(matches[0]) - 1

        return ParentNode(
            f"h{heading_rank}",
            [node.convert_to_html_node() for node in text_nodes]
        )
    else:
        raise ValueError("Heading not present in heading block")

def block_paragraph_to_html(block: str):
    text_nodes = convert_markdown_to_textnodes(block)

    return ParentNode(
        "p",
        [node.convert_to_html_node() for node in text_nodes]
    )

def blocks_to_html(blocks: List[str]):
    html_nodes = []

    for i in range(0, len(blocks)):
        block_type = get_block_type(blocks[i])

        if block_type == "heading":
            html_nodes.append(block_headings_to_html(blocks[i]))

        if block_type == "code":
            html_nodes.append(block_code_to_html(blocks[i]))

        if block_type == "ordered_list":
            html_nodes.append(block_ordered_list_to_html(blocks[i]))

        if block_type == "unordered_list":
            html_nodes.append(block_unordered_list_to_html(blocks[i]))

        if block_type == "quote":
            html_nodes.append(block_quote_to_html(blocks[i]))

        if block_type == "paragraph":
            html_nodes.append(block_paragraph_to_html(blocks[i]))

    return ParentNode("div", html_nodes)
